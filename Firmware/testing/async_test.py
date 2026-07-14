import asyncio

async def every_sec():
    while True: 
        await asyncio.sleep(1)
        print("meow")

async def every_five_secs():
    while True:
        await asyncio.sleep(5)
        print("ZHWOM")

async def main():
    await asyncio.gather(every_sec(), every_five_secs())

if __name__ == "__main__":
    asyncio.run(main())
