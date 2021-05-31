import requests
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "Your_api_key"
account_sid = "Your_acc_sid"
auth_token = "your_auth_token"
phone_number = 'Target_phone_number'
lat = 44.78
long = 20.44

parameters = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "exclude": "daily,current,minutely"

}

will_rain = False


response = requests.get(OMW_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain today! ☔",
        from_='+19193360896',
        to=phone_number,
    )
    print(message.status)
