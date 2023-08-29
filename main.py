from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

win = Tk()
win.title("Top Secret")
win.minsize(width=500,height=500)



def encrypt():
    with open( "notes.txt" , "a") as file:
        a =my_entry.get()
        b=my_text.get("1.0",END)
        c=my_entry2.get()

        d= encode(c,b)
        if len(a)==0 or len(b)==0 or len(c) ==0 :
            messagebox.showerror(title="Error" , message=" Girdileri boş bırakma")
        else:
            try:
                file.write("\n"+a+ "\n" +d)
            except:
                messagebox.showerror(title="hata",message="dosya bulunamadı")
            finally:
                my_entry.delete(0,END)
                my_entry2.delete(0,END)
                my_text.delete("1.0",END)


def decrypt():
        a =my_entry.get()
        b=my_text.get("1.0",END)
        c=my_entry2.get()
        d=decode(c,b)
        my_text.delete("1.0",END)
        my_text.insert("1.0",d)
foto=ImageTk.PhotoImage(file="image.jpeg")

labelfoto = Label(win,image=foto)

label1=Label(text="Enter your title")
labelfoto.pack()
label1.pack()

my_entry =Entry()
my_entry.pack()

label2=Label(text="Enter your secret")
label2.pack()

my_text=Text(width=25 ,height=10)
my_text.pack()

label3=Label(text="Enter your key")
label3.pack()

my_entry2 =Entry()
my_entry2.pack()

first_button = Button(text="save & encrypt" , command=encrypt)
second_button = Button(text="decrypt",command=decrypt)

first_button.pack()
second_button.pack()





win.mainloop()
