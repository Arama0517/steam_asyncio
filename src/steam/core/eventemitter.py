import asyncio
from collections import OrderedDict, defaultdict
from typing import Any, Awaitable, Callable, Optional


class EventEmitter:
    """
    Implements event emitter using ``asyncio`` module.
    Every callback is executed via an async task.
    """

    __worker: asyncio.Task = None

    def __init__(self):
        self.__callbacks = defaultdict(OrderedDict)
        self.__queue = asyncio.Queue()

    async def emit(self, event: Any, *args: Any):
        """
        Emit event with some arguments

        :param event: event identifier
        :param args: any or no arguments
        """
        # Enqueue the event and its arguments
        await self.__queue.put((event, args))
        await self.__queue.put((None, (event,) + args))

        if self.__worker is None or self.__worker.done():
            self.__worker = asyncio.create_task(self.__emit_worker())

    async def __emit_worker(self):
        while not self.__queue.empty():
            event, args = await self.__queue.get()

            if event in self.__callbacks:
                for callback, once in list(self.__callbacks[event].items()):
                    if once:
                        self.remove_listener(event, callback)
                    if isinstance(callback, asyncio.Future):
                        callback.set_result(args)
                    elif asyncio.iscoroutinefunction(callback):
                        asyncio.create_task(callback(*args))
                    else:
                        asyncio.create_task(asyncio.to_thread(callback, *args))

            await asyncio.sleep(0)

    def on(
        self,
        event,
        callback: Optional[Callable[..., Awaitable[None]] | asyncio.Future] = None,
        once=False,
    ):
        """
        Registers a callback for the specified event

        :param event: event name
        :param callback: callback function

        Can be as function decorator if only ``event`` param is specified.
        """
        # when used function
        if callback:
            self.__callbacks[event][callback] = once
            return

        # as decorator
        def wrapper(callback: Callable[..., Awaitable[None]]):
            self.__callbacks[event][callback] = once
            return callback

        return wrapper

    def once(
        self, event: Any, callback: Optional[Callable[..., Awaitable[None]] | asyncio.Future] = None
    ):
        """
        Register a callback, but call it exactly one time
        """
        return self.on(event, callback, once=True)

    async def wait_event(
        self, event: Any, timeout: Optional[int] = None, raises: Optional[bool] = False
    ):
        """
        Blocks until an event and returns the results

        :param event: event identifier
        :param timeout: (optional)(default: None) seconds to wait
        :param raises: (optional)(default: False) On timeout if ``False`` return ``None``, else raise ``asyncio.TimeoutError``
        :return: returns event arguments in tuple
        """
        future = asyncio.Future()
        self.once(event, future)

        try:
            return await asyncio.wait_for(future, timeout)
        except asyncio.TimeoutError:
            self.remove_listener(event, future)
            if raises:
                raise
            else:
                return None

    def remove_listener(
        self, event: Any, callback: Callable[..., Awaitable[None]] | asyncio.Future
    ):
        """
        Removes callback for the specified event
        """
        if event in self.__callbacks:
            if callback in self.__callbacks[event]:
                del self.__callbacks[event][callback]

                if not self.__callbacks[event]:
                    del self.__callbacks[event]

    def remove_all_listeners(self, event: Optional[Any] = None):
        """
        Removes all registered callbacks, or all registered callbacks for a specific event
        """
        if event is None:
            self.__callbacks.clear()
        else:
            if event in self.__callbacks:
                del self.__callbacks[event]

    def count_listeners(self, event: Any):
        """
        Returns a count of how many listeners are registered for a specific event
        """
        if event in self.__callbacks:
            return len(self.__callbacks[event])

        return 0
