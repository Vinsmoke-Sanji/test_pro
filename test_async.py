import time
import asyncio

now = lambda : time.time()
async def show_something(x):
    print('wait', x)

start = now()

coroutine = show_something(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('TIME:', now() - start)