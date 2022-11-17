#Library import
import requests

#Mentioning API key and URL
API_KEY = "a8b90466d86d22241e7cd540eb5d44a5"
weather_url = "https://api.openweathermap.org/data/2.5/weather"
#Defining get_weather_function
def get_weather_info(city):

    """
    Input: city
    Returns:
        success [bool]
        response [dict]
    """

    querystring = {"appid":  API_KEY, "q" :city, "units": "metric"}

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    response = requests.request("GET", weather_url, headers=headers, params=querystring)
#responce handling for user inputs
    if response.status_code == 200:
        return True, response.json()
    elif response.status_code == 401:
        return False, {"message": "Invalid API Key"}
    
    else:
        return False, response.json()
