from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests
import pytz

root = Tk()
root.title("Weather Forecasting App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = text_field.get()
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    if location is None:
        messagebox.showerror("Error", "City not found.")
        return

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text='CURRENT TIME')
    
    # Weather
    api_key = "aa3f392d83a505a670427de66a1707d8"  
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        t.config(text=f"{temp}°C")
        c.config(text=f"{description.capitalize()}")
        w.config(text=f"{wind_speed} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=f"{description.capitalize()}")
        p.config(text=f"{pressure} hPa")
    else:
        messagebox.showerror("Error", "Failed to get weather data.")

# Search box 
search_image = PhotoImage(file="C:/Users/DELL PC/Desktop/Project for python/Weather App -- ParvatCompTech/Copy of search.png")
my_image = Label(image=search_image)
my_image.place(y=20, x=20)

text_field = tk.Entry(root, justify="center", width=17, font=("sansserif", 25, "bold"), bg="#404040", border=0, fg="white")
text_field.place(x=50, y=40)
text_field.focus()

search_icon = PhotoImage(file="C:/Users/DELL PC/Desktop/Project for python/Weather App -- ParvatCompTech/Copy of search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
myimage_logo = PhotoImage(file="C:/Users/DELL PC/Desktop/Project for python/Weather App -- ParvatCompTech/Copy of logo.png")
logo = Label(image=myimage_logo)
logo.place(x=150, y=100)

# Time
name = Label(root, font=("arial", 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=('Helvetica', 10))
clock.place(x=30, y=130)

# Bottom box 
frame_img = PhotoImage(file="C:/Users/DELL PC/Desktop/Project for python/Weather App -- ParvatCompTech/Copy of box.png")
frame = Label(image=frame_img)
frame.pack(padx=5, pady=5, side=BOTTOM)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, 'bold'), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="....", font=("arial", 20, 'bold'), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="....", font=("arial", 20, 'bold'), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="....", font=("arial", 20, 'bold'), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="....", font=("arial", 20, 'bold'), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
