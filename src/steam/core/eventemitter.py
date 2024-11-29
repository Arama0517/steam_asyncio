import asyncio
from collections import OrderedDict, defaultdict


class EventEmitter:
    """
    Implements event emitter using ``asyncio`` module.
    Every callback is executed via :meth:`asyncio.create_task`.
    """
    __worker = None

    def __init__(self):
        self.__callbacks = defaultdict(OrderedDict)
        self.__queue = asyncio.Queue()

    async def emit(self, event, *args):
        """
        Emit event with some arguments

        :param event: event identifier
        :type event: any type
        :param args: any or no arguments
        """
        if hasattr(self, '_EventEmitter__callbacks'):
            await self.__queue.put((event, args))
            await self.__queue.put((None, (event,) + args))

            if self.__worker is None or self.__worker.done():
                self.__worker = asyncio.create_task(self.__emit_worker())

    async def __emit_worker(self):
        while not self.__queue.empty():
            event, args = await self.__queue.get()
            if hasattr(self, '_EventEmitter__callbacks'):
                if event in self.__callbacks:
                    for callback, once in list(self.__callbacks[event].items()):
                        if once:
                            self.remove_listener(event, callback)
                        if isinstance(callback, asyncio.Future):
                            callback.set_result(args)
                        else:
                            asyncio.create_task(callback(*args))

    def on(self, event, callback=None, once=False):
        """
        Registers a callback for the specified event

        :param event: event name
        :param callback: callback function
        """
        # when used function
        if callback:
            self.__callbacks[event][callback] = once
            return

        # as decorator
        def wrapper(callback):
            self.__callbacks[event][callback] = once
            return callback
        return wrapper

    def once(self, event, callback=None):
        """
        Register a callback, but call it exactly one time

        See :meth:`eventemitter.EventEmitter.on`
        """
        return self.on(event, callback, once=True)

    async def wait_event(self, event, timeout=None, raises=False):
        """
        Blocks until an event and returns the results

        :param event: event identifier
        :param timeout: (optional)(default:None) seconds to wait
        :param raises: (optional)(default:False) On timeout if ``False`` return ``None``, else raise ``asyncio.TimeoutError``
        :return: returns event arguments in tuple
        :raises: ``asyncio.TimeoutError``

        Handling timeout

        .. code:: python

            args = ee.wait_event('my event', timeout=5)
            if args is None:
                print("Timeout!")
        """
        future = asyncio.Future()
        self.once(event, future)

        try:
            return await asyncio.wait_for(future, timeout)
        except asyncio.TimeoutError:
            self.remove_listener(event, future.set_result)

            if raises:
                raise
            else:
                return None

    def remove_listener(self, event, callback):
        """
        Removes callback for the specified event

        :param event: event identifier
        :param callback: callback reference
        :type callback: function, method or :class:`asyncio.Future`
        """
        if hasattr(self, '_EventEmitter__callbacks'):
            if event in self.__callbacks:
                del self.__callbacks[event][callback]

                if not self.__callbacks[event]:
                    del self.__callbacks[event]

    def remove_all_listeners(self, event=None):
        """
        Removes all registered callbacks, or all
        registered callbacks for a specific event

        :param event: event identifier
        """
        if hasattr(self, '_EventEmitter__callbacks'):
            if event is None:
                self.__callbacks.clear()
            else:
                if event in self.__callbacks:
                    del self.__callbacks[event]

    def count_listeners(self, event):
        """
        Returns a count of how many listeners are
        registered for a specific event

        :param event: event identifier
        :returns: number of listeners
        :rtype: int
        """
        if hasattr(self, '_EventEmitter__callbacks'):
            if event in self.__callbacks:
                return len(self.__callbacks[event])

        return 0
