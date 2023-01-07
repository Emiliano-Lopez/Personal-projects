from tkinter import *
from weather import Weather
from settings import Root_setiings
from datetime import datetime
from PIL import ImageTk,Image



root_settings = Root_setiings()


now = datetime.now()




w = Weather()
root = Tk()
root.geometry(root_settings.screen_size)
root.configure(background=root_settings.background)

icon_2xx = ImageTk.PhotoImage(Image.open("images/cloud_thunder.jpg"))
icon_3xx = ImageTk.PhotoImage(Image.open("images/cloud_rain.png"))
icon_5xx = ImageTk.PhotoImage(Image.open("images/cloud_rain.png"))
icon_6xx = ImageTk.PhotoImage(Image.open("images/snowflake.png"))
icon_7xx = ImageTk.PhotoImage(Image.open("images/cloud_fog.png"))
icon_800 = ImageTk.PhotoImage(Image.open("images/sun.png"))
icon_8xx = ImageTk.PhotoImage(Image.open("images/cloud_sun.png"))


list_icons= [icon_2xx,icon_3xx,icon_5xx,icon_6xx,icon_7xx,icon_800,icon_8xx]


#root.attributes('-alpha',0.9)


def show_weather():
    def show_menu():
        menu()
        place_label.destroy()
        weather_label.destroy()
        image_label.destroy()
        temp_label.destroy()
        feels_label.destroy()
        hum_label.destroy()
        back_button.destroy()

    if w.weather_code >= 200 and w.weather_code <300:
        image_label = Label(root,image=list_icons[0])

    if w.weather_code >= 300 and w.weather_code <400:
        image_label = Label(root,image=list_icons[1])

    if w.weather_code >= 500 and w.weather_code <600:
        image_label = Label(root,image=list_icons[2])

    if w.weather_code >= 600 and w.weather_code <700:
        image_label = Label(root,image=list_icons[3])

    if w.weather_code >= 700 and w.weather_code <800:
        image_label = Label(root,image=list_icons[4])

    if w.weather_code == 800:
        image_label = Label(root,image=list_icons[5])

    if w.weather_code > 800 and w.weather_code <900:
        image_label = Label(root,image=list_icons[6])


    place_label = Label(root, text=w.city+", "+w.country, font=root_settings.title_font)
    place_label.config(bg=root_settings.background)
    place_label.pack(pady=5)

    weather_label = Label(root,text= w.weather ,font=root_settings.title_font)
    weather_label.config(bg=root_settings.background)
    weather_label.pack() 
    
    image_label.pack(pady=5)

    temp_label =  Label(root, text="temp: "+w.temp+"°", font=root_settings.text_font)
    temp_label.config(bg=root_settings.background)
    temp_label.place(relx=0.3, rely=0.75, anchor=CENTER)


    feels_label = Label(root,text="feels like: "+w.feels_like+"°", font=root_settings.text_font)
    feels_label.config(bg=root_settings.background)
    feels_label.place(relx=0.75, rely=0.75, anchor=CENTER)

    hum_label = Label(root,text="humidity: "+w.hum+"%", font=root_settings.text_font)
    hum_label.config(bg=root_settings.background)
    hum_label.place( relx=0.5,rely=0.825, anchor=CENTER)

    back_button = Button(root,text="menu",command=show_menu)
    back_button.place(relx=0.5,rely=0.925, anchor=CENTER)


def menu():
    def get_city():

        try: 
            w.city= city_entry.get().title()
            w.get_weather()

            city_label.destroy()
            city_entry.destroy()
            city_button.destroy()

            show_weather()

        except:
            city_button.config(text="Insert a valid city",fg="red")

    if root_settings.clock_visible == False:
        dtime_label = Label(root,text=now.strftime("%A %H")+":00", bg=root_settings.background, font=root_settings.text_font)
        dtime_label.pack(side=TOP,anchor=NW)
        root_settings.clock_visible = True


    city_label = Label(root, text="Enter the city",font=root_settings.title_font)
    city_label.pack(pady=50)
    city_label.config(bg=root_settings.background)

    city_entry = Entry(root)
    city_entry.place(relx=0.5, rely=0.5, anchor=CENTER)


    city_button = Button(root,text="CONFIRM",command=get_city)
    city_button.place(relx=0.5, rely=0.6, anchor=CENTER)




menu()
root.mainloop()


