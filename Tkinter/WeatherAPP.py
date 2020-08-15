from tkinter import *
import requests
import json



root = Tk()
root.title("Weather App")
root.geometry("400x50")
root.configure(background="green")
api_request = requests.get("url")

api = json.loads(api_request.content)
#Creating A function to search for spefic api
def zipfunction():
    zip_entry.get()
    label = Label(root,text=zip_entry.get(),anchor=N)
    label.grid(row=1,column=0,columnspan=2,sticky=E + W)

    try:
        api_request = requests.get("url")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "#0CO"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#FF9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        label = Label(root, text=city + " Air Quality" + str(quality) + " " + category, font=("Helvetical", 20),
                      background=weather_color)
        label.grid(row=2, column=0)

    except EXCEPTION as e:
           api = "Error ....."

#creating zip Enrty
zip_entry = Entry(root)
zip_entry.grid(row=0,column=0,padx=20)

#creating a btn to load the Api
zip_btn = Button(root,text="Search the api",command=zipfunction)
zip_btn.grid(row=0,column=1)




root.mainloop()
