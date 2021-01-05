import requests
from tkinter import *

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key} 

root = Tk()
root.geometry("400x200")
root.title('Weather app')
root.configure(background = 'bisque')

global api
api = "48f41b03d3b1f0a9867b61f6e3742b68"

global city_text
city_text = Entry(root)
city_text.place(x=100, y=0)

global city

def search():
    global ico_data
    city = city_text.get()
    city = city.upper()

    api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api

    api_link = requests.get(api_url)
    api_data = api_link.json()

    temp = api_data["main"]["temp"]
    c_temp = temp - 273.15

    ico = api_data["weather"][0]["icon"]
    ico_data = "icons/{}.png".format(ico)

    clarity_data = api_data["weather"][0]["description"]

    temp_label['text'] = city
    icon['file'] = ico_data
    temp_status['text'] = '{:.2f}'.format(c_temp)+'°C |'
    clarity['text'] = clarity_data

search_btn = Button(root, text='Search', command=search)
search_btn.place(x=200, y=0)

temp_label = Label(root, text='', bg='bisque', font=('Arial Bold', 30))
temp_label.place(x=105, y=30)
temp_status = Label(root, text='', font=('Arial Bold', 16), bg='bisque')
temp_status.place(x=80, y=80)
clarity = Label(root, text = '', bg='bisque', font=('Arial Bold', 16))
clarity.place(x=175, y=80)

icon = PhotoImage(file='')
icon_ = Label(root, image=icon, bg='bisque')
icon_.place(x=105, y=110)

root.mainloop()