import webbrowser
from tkinter import *
import pyshorteners


def redirect_port():
    get_url = shorten_url.get()
    if shorten_url.get() != "":
        webbrowser.open(get_url, new=0)


def convert():

    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url_entry.get())
        shorten_url.insert(0, short_url)

        redirect_button = Button(window, text="Redirect", font=("Georgia", 12), bg="#333333", fg="yellow", command=redirect_port)
        redirect_button.place(x=110, y=230)

    except:
        pass


window = Tk()
window.title("URL Shortener")
window.geometry("300x300")
window.configure(bg="#333333")
window.resizable(False, False)

url_entry = Entry(window, font=("Georgia", 12))
url_entry.place(x=40, y=30)

url_entry_label = Label(window, text="Enter url here", bg="#333333", fg="white")
url_entry_label.configure(font=("Georgia", 12))
url_entry_label.place(x=87, y=60)

shorten_url = Entry(window, font=("Georgia", 12))
shorten_url.place(x=40, y=110)

shorten_url_label = Label(window, text="Shortened url", font=("Georgia", 12), bg="#333333", fg="white")
shorten_url_label.place(x=87, y=140)

convert_button = Button(window, text="Convert", font=("Georgia", 12), bg="#333333", fg="yellow", command=convert)
convert_button.place(x=110, y=190)

window.mainloop()