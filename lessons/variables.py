def get_weather_report() -> str:
    weather: str = input("What is the weather today?\n")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep it cool out there!")
    else:
        print("I don't recognize this weather")
    return weather


print(get_weather_report())
