import asyncio

async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    print('ok')
    await asyncio.sleep(delay)
    
    # Set *value* as a result of *fut* Future.
    fut.set_result(value)

async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.create_task(
        set_after(fut, 0.5, '... world'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(fut)
    await fut
    print(fut)
    print(await fut)

asyncio.run(main())


async def task_thing(time):
    print('ok. Started')
    await asyncio.sleep(time+1)
    print('finished')



async def main2():
    tasks = []
    for x in range(5):

        task = asyncio.create_task(task_thing(x))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

asyncio.run(main2())

    