from time import strftime, localtime
import asyncio


def doDisplay(msg):
    now = strftime("%H:%M:%S", localtime())
    print("%s %s" % (now, msg))


async def displayAfter(msg, delay):
    doDisplay("START: " + msg)
    await asyncio.sleep(delay)
    doDisplay("END: " + msg)
    return "I'm all done"


async def main():
    print("*****Start of main*****")
    task = asyncio.create_task(displayAfter("Hello", 2))
    print(task.done())
    for i in range(0, 5):
        print("Doing something useful...")
        await asyncio.sleep(1)

    print("Finished doing useful work, now I'll wait for task to finish")

    await task
    print(task.done())
    print(task.result())
    print("*****End of main*****")


if __name__ == "__main__":
    asyncio.run(main())
