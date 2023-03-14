import requests


print("Welcome To Wecharm")
while True:
    command_user = input(">")
    com = command_user.lower()
    if com == "rec -we":
        geographique_Data = []
        city_command_user = input("Type The City  >")
        state_command_user = input("Type The State (if you don't know keep it empty) >")
        country_code_command_user = input("Type The Code of Countries (if you don't know keep it empty) >")
        api_key = "c4d5837a918b0792e88606a35ecac830"
        print("Please wait...")
        api = f"http://api.openweathermap.org/geo/1.0/direct?q={city_command_user},{state_command_user},{country_code_command_user}&appid={api_key}"
        response = requests.get(api)
        if response.status_code == 200:
            print("Getting Country Completed")
            data = response.json()
            geographique_Data.append(data)
            extract = geographique_Data[0]
            extract_1 = extract[0]
            print("Working...")
            api_we_key = "1bb6685c8ff45debb173b1c55413f7e0"
            api_2 = f"https://api.openweathermap.org/data/2.5/weather?lat={extract_1['lat']}&lon={extract_1['lon']}&appid={api_we_key}"
            response_2 = requests.get(api_2)
            if response_2.status_code == 200:
                data_we = response_2.json()
                weather_general, weather_medium = data_we['weather'], data_we['main']
                weather_info = ""
                weather_info += f"General:{weather_general[0]['main']}\nTemp:{weather_medium['temp']-273.15}c°\nTemp Min:{weather_medium['temp_min']-273.15}c°\nTemp Max:{weather_medium['temp_max']-275.15}c°\nHumidity:{weather_medium['humidity']}% "
                print(weather_info)
                print("Operation completed")
            else:
                print("Error fatal")
        else:
            print("Error", response)