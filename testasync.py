import asyncio

async def fetch_data(url):
    print("Fetching data from", url)
    # Simulating an asynchronous operation with a delay
    await asyncio.sleep(1)
    print("Data fetched from", url)

async def main():
    # Creating tasks for fetching data concurrently
    task1 = asyncio.create_task(fetch_data("https://example.com/data1"))
    task2 = asyncio.create_task(fetch_data("https://example.com/data2"))

    # Wait for all tasks to complete
    await asyncio.gather(task1, task2)

asyncio.run(main())
