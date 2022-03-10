from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
window.config(bg="white")

label1 = Label(text="is equal to", font=("Arial", 12, "normal"))
label1.grid(row=1, column=0)
label1.config(padx=5, pady=5, bg="white")

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

label2 = Label(text="Miles", font=("Arial", 12, "normal"))
label2.config(padx=5,pady=5, bg="white")
label2.grid(row=0, column=2)

label3 = Label(text="Km", font=("Arial", 12, "normal"))
label3.config(padx=10,pady=10, bg="white")
label3.grid(row=1, column=2)

def miles_to_km():
    result = round(float(entry.get()) * 1.60934)
    result_label.config(text=f"{result}")

result_label = Label(text="0", bg="white")
result_label.grid(row=1, column=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)


# #Label
# my_label = Label(text="My Label", font=("Arial", 20, "italic"))
# my_label.grid(row=0, column=0)

# button = Button(text="Click me")
# button.grid(row=1, column=1)

# button2 = Button(text="Click me")
# button2.grid(row=0, column=2)

# entry = Entry(width=10)
# entry.insert(END, string="Some text to begin with")
# entry.grid(row=2,  column=3)


window.mainloop()