import asyncio
import time


async def a_sleep(id):
    await asyncio.sleep(1)
    print(f"a_sleep {id} has ended")


async def main():
    await asyncio.gather(
        a_sleep(1),
        a_sleep(2),
        a_sleep(3))


if __name__ == '__main__':
    start = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    exec_time = time.time() - start
    print({
        'exec_time': exec_time
    })
