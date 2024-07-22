import tkinter as tk
root = tk.Tk()

root.geometry("500x500")
root.title("My First tk")
#(parentObj, text, font=("Arial,18"))
label = tk.Label(root, text="Hello world!", font=("Arial", 18))
label.pack(padx= 10, pady= 10)#padx and pady for padding

textbox = tk.Text(root,height=3, font=("Arial", 16))#gets only 3 lines in the textbox
textbox.pack(padx=10)



#button = tk.Button(root, text="Button", font=("Arial", 18))
#button.pack(padx=10, pady=10)# we will have grid and place for button like pack
#.............................place is for certain height and width
#.............................gird is to place multiple button like in calculator
#.............................in grid...sticky=tk.W+tk.E is for no gap between them

#myEntry = tk.Entry(root)#text box used for passwords
#myEntry.pack()#only one line input

root.mainloop()