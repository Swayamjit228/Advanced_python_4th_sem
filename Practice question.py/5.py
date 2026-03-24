#SECTION E: GUI + Database Based  
#18. Create a Tkinter form: - Name input - Submit button - Show entered name 
"""from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sunny bhai ka Form")
root.iconbitmap(r'C:\Users\LOQ\OneDrive\Desktop\New folder\cute-cartoon-happy-sun-with-face-isolated-on-white-background-summer-shadowed-clip-art-sunshine-icon-in-kid-s-style-sunny-weather-symbol-vector.jpg')

root.geometry('500x500+0+0')
root.configure(background="#E5570B")

# image
img = Image.open(r'C:\Users\LOQ\OneDrive\Desktop\New folder\cute-cartoon-happy-sun-with-face-isolated-on-white-background-summer-shadowed-clip-art-sunshine-icon-in-kid-s-style-sunny-weather-symbol-vector.jpg')
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image = img)
img_label.pack(pady=10,padx=20)

# text label
text_label = Label(root,text="Sunny ka form",font=('Arial', 18,'bold'),bg="#C94508",fg='white')
text_label.pack(pady=10,padx=20)

email_label = Label(root,text="Email",font=('Arial', 18,'bold'),bg="#FB1111",fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial', 18,'bold'),bg="#F41317",fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='grey')
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('Arial', 18,'bold'),bg="#EF0D0D",fg='white')
login_btn.pack(pady=(5,10))

root.mainloop()"""

#19. Python + SQL: - Connect database - Create table Student 
#- Insert 3 records - Fetch and display all 
import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="04Jan2006@sjm",
    host="localhost",
    port=3306,
    database="giet"

)

cur = con.cursor()

query = "select * from student2"
querry="select * from student2 where name='swayam'"
querry="select * from student2 where age=20"
cur.execute(query)

myresult = cur.fetchall()
for x in myresult:
    print(x)
    
# cur.close()
con.close()
#20. Build mini project: 
#STUDENT MANAGEMENT SYSTEM 
#Features: - Add student - View student - Delete student - Store data in file or database 