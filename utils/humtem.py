import requests

def get_temp_hum(district, state=None, month=None):
    # First, try fetching data using district
    district_url = f"https://api.openweathermap.org/data/2.5/weather?q={district}&appid=af1253e5ac93e4757ad434376e322761"
    district_response = requests.get(district_url)

    # If the request using district fails, try using state
    if district_response.status_code != 200:
        if state is not None:
            state_url = f"https://api.openweathermap.org/data/2.5/weather?q={state}&appid=af1253e5ac93e4757ad434376e322761"
            state_response = requests.get(state_url)

            if state_response.status_code != 200:
                print(f"Failed to fetch data for both {district} and {state}")
                raise Exception(f"Unable to get the temperature for {district} or {state}")

            data = state_response.json()
        else:
            print(f"Failed to fetch data for {district}")
            raise Exception(f"Unable to get the temperature for {district}")
    else:
        data = district_response.json()

    humidity = data['main']['humidity']
    temp = (data['main']['temp_min'] + data['main']['temp_max']) / 2 - 273.15
    return temp, humidity
