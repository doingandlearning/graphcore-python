from time import strftime, localtime
import asyncio


def doDisplay(msg):
    now = strftime("%H:%M:%S", localtime())
    print("%s %s" % (now, msg))


async def displayAfter(msg, delay):
    doDisplay("START: " + msg)
    await asyncio.sleep(delay)
    doDisplay("END: " + msg)


async def main():
    try:
        doDisplay("*****Start of main*****")
        task1 = asyncio.create_task(displayAfter("Bonjour", 10))
        task2 = asyncio.create_task(displayAfter("Bore da", 15))
        task3 = asyncio.create_task(displayAfter("Hei hei", 20))

        for i in range(0, 5):
            doDisplay("Doing something useful...")
            await asyncio.sleep(1)

        doDisplay("Waiting for task1 to finish")
        await task1

        doDisplay("Waiting for task2 to finish")
        await task2

        doDisplay("Waiting for task3 to finish")
        await task3

        doDisplay("*****End of main*****")
    except ValueError:
        pass


if __name__ == "__main__":
    asyncio.run(main())
