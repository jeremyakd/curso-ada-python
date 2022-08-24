# import the module
import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC )

    # fetch a weather forecast from a city
    weather = await client.get("Ushuaia") #Washington DC
    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(forecast.date, forecast.snow_width) #forecast.astronomy)
        #print(str(forecast.date), forecast.hourly )
        #for _ in forecast.sun_shines:
        #    print(_)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())