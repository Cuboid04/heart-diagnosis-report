from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Cardiovascular Report")
root.geometry("600x600")

Q1_radiobutton=StringVar(value="0")
Q1=Label(root, text="Do You Experience Shortness Of Breath During Routine Activities?")
Q1.pack()
Q1_r1=Radiobutton(root, text="Yes", value="Yes", variable=Q1_radiobutton)
Q1_r1.pack()
Q1_r2=Radiobutton(root, text="No", value="No", variable=Q1_radiobutton)
Q1_r2.pack()

Q2_radiobutton=StringVar(value="0")
Q2=Label(root, text="Do You Have Swelling In The Feet / Ankle / Legs (Shoes Feel Tighter) Or Abdomen?")
Q2.pack()
Q2_r1=Radiobutton(root, text="Yes", value="Yes", variable=Q2_radiobutton)
Q2_r1.pack()
Q2_r2=Radiobutton(root, text="No", value="No", variable=Q2_radiobutton)
Q2_r2.pack()

Q3_radiobutton=StringVar(value="0")
Q3=Label(root, text="Do You Feel Any Of These Symptoms - Confusion, Disorientation Or Loss Of Memory?")
Q3.pack()
Q3_r1=Radiobutton(root, text="Yes", value="Yes", variable=Q3_radiobutton)
Q3_r1.pack()
Q3_r2=Radiobutton(root, text="No", value="No", variable=Q3_radiobutton)
Q3_r2.pack()

Q4_radiobutton=StringVar(value="0")
Q4=Label(root, text="Do You Experience Shortness Of Breath While At Rest / Lying Down?")
Q4.pack()
Q4_r1=Radiobutton(root, text="Yes", value="Yes", variable=Q4_radiobutton)
Q4_r1.pack()
Q4_r2=Radiobutton(root, text="No", value="No", variable=Q4_radiobutton)
Q4_r2.pack()

Q5_radiobutton=StringVar(value="0")
Q5=Label(root, text="Do You Experience Persistent Wheezing / Coughing That Produces White Or Pink Blood Tinged Mucus?")
Q5.pack()
Q5_r1=Radiobutton(root, text="Yes", value="Yes", variable=Q5_radiobutton)
Q5_r1.pack()
Q5_r2=Radiobutton(root, text="No", value="No", variable=Q5_radiobutton)
Q5_r2.pack()

def fever():
    score=0
    if(Q1_radiobutton.get()=="Yes"):
        score=score+10
        print(score)
    if(Q2_radiobutton.get()=="Yes"):
        score=score+10
        print(score)
    if(Q3_radiobutton.get()=="Yes"):
        score=score+10
        print(score)
    if(Q4_radiobutton.get()=="Yes"):
        score=score+10
        print(score)
    if(Q5_radiobutton.get()=="Yes"):
        score=score+10
        print(score)
        
    if(score<=10):
            messagebox.showinfo("Report", "You Don't Need To Visit A Doctor.")
    elif(score>10 and score<=30):
            messagebox.showinfo("Report", "You Might Have To Visit A Doctor.")
    else:
        messagebox.showinfo("Report", "I Strongly Advise You To Visit A Doctor.")

btn=Button(root, text="Get Report", command=fever)
btn.pack()

root.mainloop()