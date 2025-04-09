import requests

城市=input(print("請輸入城市名稱:"))
API="bbe1cb0e9a4b6d0525cc89fff273300e"
網址=f"https://api.openweathermap.org/data/2.5/weather?q={城市}&appid={API}"
天氣資料=requests.get(網址)
氣溫=int(天氣資料.json()["main"]["temp"]-273.15)
print(f"{城市}目前為{氣溫}°C")