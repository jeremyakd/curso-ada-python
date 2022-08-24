import python_weather
import asyncio

async def getweather(city):
    client = python_weather.Client(format=python_weather.METRIC )
    weather = await client.get(city)
    print("Ciudad: {} Actual temperatura {} {}.".format(
        city,
        weather.current.temperature,
        weather.format
        )
    )
    await client.close()

if __name__ == "__main__":
    cuidad = input("Ingrese una cuidad por favor.")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather(cuidad))