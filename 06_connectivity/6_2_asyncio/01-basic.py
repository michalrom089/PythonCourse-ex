import asyncio
import time

c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[92m"  # Green
)


async def a_sleep(id):
    await asyncio.sleep(1)
    print(c[id + 1] + f"a_sleep {id} has ended" + c[0])


def sleep(id):
    time.sleep(id)
    print(c[id + 1] + f"sleep {id} has ended" + c[0])


async def main():
    await asyncio.gather(
        a_sleep(1),
        a_sleep(2),
        a_sleep(3))

    # # synchronous version
    # for i in range(1, 4):
    #     sleep(i)


if __name__ == '__main__':
    start = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

    exec_time = time.time() - start
    print({
        'exec_time': exec_time
    })
