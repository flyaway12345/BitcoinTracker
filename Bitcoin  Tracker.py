import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S %p")

    lablePrice.config(text = "$ " + str(price))
    lableTime.config(text = "Updated At: " +time)

    print(response)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Tracker")
f1 = ("comic sans",24, "bold")
f2 = ("comic sans",22, "bold")
f3 = ("comic sans",18, "normal")

label = tk.Label(canvas,text="Bitcoin Price", font = f1)
label.pack(pady = 20)

lablePrice = tk.Label(canvas, font=f2)
lablePrice.pack(pady = 20)

lableTime = tk.Label(canvas, font=f3)
lableTime.pack(pady = 20)


trackBitcoin()
canvas.mainloop()

