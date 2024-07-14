import tkinter as tk

root = tk.Tk()

root.geometry("500x500") #Set the window size
root.title("My first GUI") #Set the window title

label=tk.Label(root,text="Hello World",font=("Arial",24)) #Create a label
label.pack(padx=20,pady=20) #Display the label using "pack"(a layout method)

textbox=tk.Text(root,height=3,width=70,font=("Arial",18)) #Create a text box
textbox.pack(padx=10) #Display the text box using "pack"

# entry=tk.Entry(root,font=("Arial",24)) #Create an entry box   AN ENTRY IS A ONE LINE TEXT BOX
# entry.pack(padx=10,pady=20) #Display the entry box using "pack"

buttonframe=tk.Frame(root) #Create a frame
buttonframe.columnconfigure(0,weight=1) #Set the column weight to 1
buttonframe.columnconfigure(1,weight=1) #Set the column weight to 1
buttonframe.columnconfigure(2,weight=1) #Set the column weight to 1


button1=tk.Button(buttonframe,text="1",height=1,font=("Arial",16)) #Create a button   
button1.grid(row=0,column=0,sticky=tk.W+tk.E) #Display the button using "grid" in the first row and first column

button2=tk.Button(buttonframe,text="2",height=1,font=("Arial",16)) #Create a button
button2.grid(row=0,column=1,sticky=tk.W+tk.E) #Display the button using "grid" in the first row and second column

button3=tk.Button(buttonframe,text="3",height=1,font=("Arial",16)) #Create a button
button3.grid(row=0,column=2,sticky=tk.W+tk.E) #Display the button using "grid" in the first row and third column

button4=tk.Button(buttonframe,text="4",height=1,font=("Arial",16)) #Create a button
button4.grid(row=1,column=0,sticky=tk.W+tk.E) #Display the button using "grid" in the second row and first column

button5=tk.Button(buttonframe,text="5",height=1,font=("Arial",16)) #Create a button
button5.grid(row=1,column=1,sticky=tk.W+tk.E) #Display the button using "grid" in the second row and second column

button6=tk.Button(buttonframe,text="6",height=1,font=("Arial",16)) #Create a button
button6.grid(row=1,column=2,sticky=tk.W+tk.E) #Display the button using "grid" in the second row and third column

buttonframe.pack(fill="x")

root.mainloop() #Run the main loop


