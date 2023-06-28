from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(pady=50, padx=50)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


button = Button(text="New Button")
button.grid(column=2, row=0)


# Entry
input = Entry(width=10)
input.insert(END, string="Some text to begin with.")
input.grid(column=3, row=2)
print(input.get())



window.mainloop()