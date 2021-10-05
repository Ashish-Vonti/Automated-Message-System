from tkinter import *             #import tkinter
from PIL import Image,ImageTk
import tkinter.messagebox as mb       #importing message box
import smtplib         #simple mail transfer protocol
import os
import requests

root = Tk()                           #tkinter initial steps
root.title("Welcome to our Massage Center!!")      #window title
root.geometry("1360x768")             
root.iconbitmap(r"C:\Users\U6064293\OneDrive - Clarivate Analytics\Desktop\Repo\Automated-Message-System-main\auto\logo.ico")   #icon




mail = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('PASSWORD')


def click():
    mb.showinfo("Success","Your appointment as been placed.We have sent you verification mail to your Email ID ")
    cusname = e1.get()
    cusphone = e2.get()
    cusmailid = e3.get()

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(mail,password)

        subject = "Verification Mail"
        body = f"Hello {cusname}.This is just a verification mail\n This is sent to confirm the email address given while booking an massage therapy.\n Your booking as been confirmed.We are open from 9AM to 5PM.\nThis is automated message DONT REPLY"
        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(mail, f'{cusmailid}' ,msg)

    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization":"RxUp2FD7Edma0bXtLZH16NGnouyQqleY389sJrOSwiA5cIVkzhz9KYlZCiaGfUynobkt1dO6L8qJMWeA","sender_id":"FSTSMS","language":"english","route":"qt","numbers":f"{cusphone}","message":"33563","variables":"{AA}|{CC}","variables_values":"12345|asdaswdx"}

    headers = {'cache-control': "no-cache"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

Label(text="Welcome to our Massage Center!! ",bg="red",padx = 10,pady = 10, font = "comicsansms 20 bold").pack(fill = X)   #title
Label(text="We help you to relax your mind and soul", padx =3, pady = 3, font ="comicsanms 15 ").pack(pady=3)  #subtitle 
Label(text="ABOUT US", font= "comicsansms 19 ").pack(anchor="w",pady=0)    #about branch
Label(text="_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________").pack()
frame = Frame(root)
frame.pack()
sbar = Scrollbar(frame ,  orient = VERTICAL)
sbar.pack(side = RIGHT, fill = Y)
mt = Text(frame, height=5, width=210, yscrollcommand = sbar.set)
mt.insert(1.0, "WHAT IS A MASSAGE?\n")
mt.insert(2.0,"Massage is defined as the systematic manipulation of the soft tissues of the body for a curative effect.Soft tissues are made more pliable through massage to promote circulation and blood flow and bring about healing effects.Both physically and psychologically.\n")
mt.insert(3.0,"WHAT ARE THE BENEFITS OF  MASSAGE?\n")
mt.insert(4.0,"1. Insomnia\n")
mt.insert(5.0,"2. Muscular tension\n")
mt.insert(6.0,"3. Headaches and Migraines\n")
mt.insert(7.0,"4. Work related stress\n")
mt.insert(8.0,"5. Repetitive strain injuries\n")
mt.insert(9.0, "WHAT SHOULD I EXPECT FROM A MASSAGE SESSION?\n")
mt.insert(10.0, "Massage normally takes place in a private room or space. Clients are expected to partially undress and are given a towel or robe to place over themselves. The exception to this is with ‘Mobile Massage’ whereby the client may remain clothed and is not always in a private space. Most massage will take place on a massage table lying down, but in some cases the massage takes place whilst you are seated on a massage chair, or on a floor mat. Massage therapy can last for 10 mins to 1 hour depending what is requested.\n")
mt.insert(11.0,"CONTACT US\n")
mt.insert(12.0,"Owner's Name: ASHISH V\n")
mt.insert(13.0,"Email address of the owner: ashishvonti19@gmail.com\n")
mt.insert(14.0,"Contact:+91 9743740082\n")
mt.config(state = DISABLED)
mt.pack(fill = X)
sbar.config(command = mt.yview)

can = Canvas(root,width =1300, heigh = 180 )
can.pack()

img1 = PhotoImage(file = r"C:\Users\U6064293\OneDrive - Clarivate Analytics\Desktop\Repo\Automated-Message-System-main\auto\pic1.png")
my_image1 = can.create_image(300,0, anchor = "n",image =img1)

img2 = PhotoImage(file = r"C:\Users\U6064293\OneDrive - Clarivate Analytics\Desktop\Repo\Automated-Message-System-main\auto\pic2.png")
my_image2 = can.create_image(300,0, anchor = "n",image =img2)

img3 = PhotoImage(file = r"C:\Users\U6064293\OneDrive - Clarivate Analytics\Desktop\Repo\Automated-Message-System-main\auto\pic3.png")
my_image3 = can.create_image(550,0, anchor = "n",image =img3)

img4 = PhotoImage(file = r"C:\Users\U6064293\OneDrive - Clarivate Analytics\Desktop\Repo\Automated-Message-System-main\auto\pic4.png")
my_image4 = can.create_image(800,0, anchor = "n",image =img4)

img5 = PhotoImage(file = r"C:\Users\U6064293\OneDrive - Clarivate Analytics\Desktop\Repo\Automated-Message-System-main\auto\pic5.png")
my_image5 = can.create_image(1100,0, anchor = "n",image =img5)


Label(text="BOOK YOUR APPOINTMENT", font= "comicsansms 19 ",pady=10).pack(anchor="w",)  #appointment branch
Label(text="_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________").pack()
Label(text="Enter your name").pack()                      #credentials
e1 = Entry(root)
e1.pack()
Label(text="Enter your phone number").pack()
e2 = Entry(root)
e2.pack()
Label(text="Enter your email id").pack()
e3 = Entry(root)
e3.pack()
Label(text="Liked our Service? Write a Feedback to us below.").pack()
e4 = Entry(root)
e4.pack()                                                 
Label(text="Rate us").pack()
myslider = Scale(root, from_ = 0, to = 5, orient = HORIZONTAL)
myslider.pack()                                             #slider
myslider.set(4)                                              #default value
b1= Button(root, text="Submit",command= click)              #submit button
b1.pack()
root.mainloop()
