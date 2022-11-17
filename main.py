#From weather module we are importing get_weather_info function.
from weather import get_weather_info
#Define main function
def main():
#User input with correct and wrong entry handling.
    try:
        city = input("Enter city!\n")
        if not city:
            raise
        #Once user gives input (Country name) it calls the weather details from API
        success, response = get_weather_info(city=city)
        if success:
            print(f"Place: {response['name']} -  {response['sys']['country']}")
            print(f"Temperature : {response['main']['temp']} celsius.\n")
            print(f"Min : {response['main']['temp_min']} celsius.\n")
            print(f"Max : {response['main']['temp_max']} celsius.\n")
            print("\n\n")
        else:
            print(response["message"].title())
    except:
        print("Invalid input! Please enter correct city name. ")


if __name__ == "__main__":
    main()
