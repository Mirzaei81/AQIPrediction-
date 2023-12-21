import requests 
from pandas import DataFrame as df

IR_CODE =  364
API_KEY = "fed7950cdbc8b5c8b4bf7035cd058dce"
CITY_NAME = "qazvin"
Limit = 5

res = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={CITY_NAME},,{IR_CODE}&limit={Limit}&appid={API_KEY}")
print(res.text)
