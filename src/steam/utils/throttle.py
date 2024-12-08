import asyncio
import time
from typing import Awaitable, Callable


class ConstantRateLimit:
    def __init__(
        self,
        times,
        seconds,
        exit_wait=False,
        sleep_func: Callable[[None], Awaitable[None]] = asyncio.sleep,
    ):
        """Context manager for enforcing constant rate on code inside the block .

        `rate = seconds / times`

        :param times: times to execute per...
        :type  times: :class:`int`
        :param seconds: ...seconds
        :type  seconds: :class:`int`
        :param exit_wait: whether to automatically call :meth:`wait` before exiting the block
        :type  exit_wait: :class:`bool`
        :param sleep_func: Sleep function in seconds. Default: :func:`time.sleep`
        :type  sleep_func: :class:`bool`

        Example:

        .. code:: python

            with RateLimiter(1, 5) as r:
                # code taking 1s
                r.wait()  # blocks for 4s
                # code taking 7s
                r.wait()  # doesn't block
                # code taking 1s
                r.wait()  # blocks for 4s
        """
        self.__dict__.update(locals())
        self.rate = float(seconds) / times
        self.sleep_func = sleep_func
        self.exit_wait = exit_wait

    async def __aenter__(self):
        self._update_ref()
        return self

    async def __aexit__(self, etype, evalue, traceback):
        if self.exit_wait:
            await self.wait()

    def _update_ref(self):
        self._ref = time.monotonic() + self.rate

    async def wait(self):
        """Blocks until the rate is met"""
        now = time.monotonic()
        if now < self._ref:
            delay = max(0, self._ref - now)
            self.sleep_func(delay)
        self._update_ref()
