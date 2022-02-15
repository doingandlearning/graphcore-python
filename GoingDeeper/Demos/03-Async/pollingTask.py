from time import strftime, localtime
import asyncio

def doDisplay(msg):
    now = strftime("%H:%M:%S", localtime())
    print("%s %s" % (now, msg))

async def createStringAfter(msg, delay) :
    await asyncio.sleep(delay)
    now = strftime("%H:%M:%S", localtime())
    return "{0} {1}".format(now, msg)
    
async def main():
    doDisplay("*****Start of main*****")
    task = asyncio.create_task(createStringAfter("Bonjour", 10))
    
    while True: 
        if task.done():
            result = task.result()
            doDisplay(result)
            break
        else:
            doDisplay("Doing something useful...")
            await asyncio.sleep(1)

    doDisplay("*****End of main*****")
    
if __name__ == "__main__" :
    asyncio.run(main())
