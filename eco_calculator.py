from tkinter import *

root= Tk()
root.title("Engineering Economics Calculator")

global l1,e1,l2,e2,l3,e3,l4,e4,l5,e5 
l1 = Label(root, text = "Present Value : ").grid(row = 0, column = 0)  
e1 = Entry(root) 
e1.insert(0,"0")

l2 = Label(root, text = "Future Value at nth year : ").grid(row = 1, column = 0)  
e2 = Entry(root) 
e2.insert(0,"0")

l3 = Label(root, text = "Annuity Value for n years : ").grid(row = 2, column = 0)  
e3 = Entry(root)
e3.insert(0,"0")  

l4 = Label(root, text = "Number of years (N) : ").grid(row = 3, column = 0)  
e4 = Entry(root) 
e4.insert(0,"0")

l5 = Label(root, text = "Interest Rate (i) : ").grid(row = 4, column = 0)  
e5 = Entry(root)
e5.insert(0,"0")

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
e3.grid(row = 2, column = 1)
e4.grid(row = 3, column = 1)
e5.grid(row = 4, column = 1)


def pw():
    pre_val= int(e1.get())
    f_val= int(e2.get())
    annuity= int(e3.get())
    N= int(e4.get())
    i= int(e5.get())*0.01

    result= pre_val + f_val*(1/((1+i)**N)) + annuity*(((i+1)**N - 1)/(i*(i+1)**N))

    label_res.config(text="Present Worth = %d" % result)  
    return  

def fw():
    pre_val= int(e1.get())
    f_val= int(e2.get())
    annuity= int(e3.get())
    N= int(e4.get())
    i= int(e5.get())*0.01
    
    result= pre_val*((1+i)**N) + f_val + annuity*(((i+1)**N - 1)/i)
    label_res.config(text="Future Worth = %d" % result)  
    return

def ann():
    pre_val= int(e1.get())
    f_val= int(e2.get())
    annuity= int(e3.get())
    N= int(e4.get())
    i= int(e5.get())*0.01

    result= pre_val*(i*(i+1)**N / ((i+1)**N - 1)) + f_val*(i / ((i+1)**N - 1)) + annuity
    label_res.config(text="Equivalent Annual Worth = %d" % result)  
    return

def irr():
    pre_val= int(e1.get())
    f_val= int(e2.get())
    annuity= int(e3.get())
    N= int(e4.get())
    i1,i2= 14*0.01,15*0.01

    pw1= pre_val + f_val*(1/((1+i1)**N)) + annuity*(((i1+1)**N - 1)/(i1*(i1+1)**N))
    pw2= pre_val + f_val*(1/((1+i2)**N)) + annuity*(((i2+1)**N - 1)/(i2*(i2+1)**N))
    result= (i1 + (((i2-i1)*pw1)/(pw1-pw2)))*100
    label_res.config(text="IRR = %d" %result)  
    return

label_res = Label(root)  
label_res.grid(row=8, column=0) 

button1= Button(root, text="Present Worth", padx=40, pady=20, command=pw)
button2= Button(root, text="Future Worth", padx=40, pady=20, command=fw)
button3= Button(root, text="Equivalent Annual Worth", padx=11, pady=20, command=ann)
button4= Button(root, text="IRR", padx=66, pady=20, command=irr)

button1.grid(row=6, column=0)
button2.grid(row=6, column=1)
button3.grid(row=7, column=0)
button4.grid(row=7, column=1)


root.mainloop()
