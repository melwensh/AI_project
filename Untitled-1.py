import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Fraud Detecion")
root.geometry("400x300")
root.minsize(550,550)

# background_image = tk.PhotoImage(file="dollars.png")
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=200, y=500, relwidth=1, relheight=1 , width=50,height=50)
image = Image.open("dollars.png")

# Resize the image
image = image.resize((400, 400), Image.ANTIALIAS) 

# Convert the image to a Tkinter-compatible format
background_image = ImageTk.PhotoImage(image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=300, y=300, width=300, height=300)

label = tk.Label(root,text="Welcome To Fraud Detection Project" , font=("bold" , 25))
label.pack(side="top")

label1=tk.Label(root,text="Enter Time : ", font=(("inter" , 20 )), width=7 , height=10 , bg="lightgrey" )
label1.place(x=7, y=50, width=250, height=40)

entry1 = tk.Entry(root,width=30,font=("inter" , 13) , bg="lightgrey" , borderwidth=3)
entry1.place(x=270,y=55,width=250,height=40)

label2=tk.Label(root,text="Enter Card Number : ", font=(("inter" , 20 )), width=7 , height=10 , bg="lightgrey" )
label2.place(x=0, y=100, width=250, height=50)

entry2 = tk.Entry(root,width=30,font=("inter" , 13) , bg="lightgrey" , borderwidth=3)
entry2.place(x=270, y=105, width=250, height=40)

label3=tk.Label(root,text="Enter merchant : ", font=(("inter" , 20 )), width=7 , height=10 , bg="lightgrey" )
label3.place(x=0, y=160, width=250, height=50)

entry3 = tk.Entry(root,width=30,font=("inter" , 13) , bg="lightgrey" , borderwidth=3)
entry3.place(x=270, y=165, width=250, height=40)

label4=tk.Label(root,text="Enter category : ", font=(("inter" , 20 )), width=7 , height=10 , bg="lightgrey" )
label4.place(x=0, y=220, width=250, height=50)

entry4 = tk.Entry(root,width=30,font=("inter" , 13) , bg="lightgrey" , borderwidth=3)
entry4.place(x=270,y=225,width=250,height=40)

label5=tk.Label(root,text="Enter Amount : ", font=(("inter" , 20 )), width=7 , height=10 , bg="lightgrey" )
label5.place(x=0, y=280, width=250, height=50)

entry5 = tk.Entry(root,width=30,font=("inter" , 13) , bg="lightgrey" , borderwidth=3)
entry5.place(x=270, y=285, width=250, height=40)

label6=tk.Label(root,text="Enter firstName : ", font=(("inter" , 20 )), width=7 , height=10 , bg="lightgrey" )
label6.place(x=0, y=350, width=250, height=50)

entry6 = tk.Entry(root,width=30,font=("inter" , 13) , bg="lightgrey" , borderwidth=3)
entry6.place(x=270, y=355, width=250, height=40)

label7=tk.Label(root,text="Enter LastName : ", font=(("inter" , 20 )), width=7 , height=10 , bg="lightgrey" )
label7.place(x=0, y=420, width=250, height=50)

entry7 = tk.Entry(root,width=30,font=("inter" , 13) , bg="lightgrey" , borderwidth=3)
entry7.place(x=270, y=425, width=250, height=40)

button = tk.Button(root, text="Submit" , font=("inter" , 10) , bg="#D6C0BA")
button.place(x=30, y=480, width=90, height=40)

root.mainloop()