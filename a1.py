from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


import tkinter as tk
from tkcalendar import DateEntry


class BIODATA:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Bio Data Management System')

        # variables
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_marriedstatus = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar()
        self.var_idproof = StringVar()
        self.var_phone = StringVar()
        self.var_country = StringVar()
        self.var_state = StringVar()
        self.var_nationality = StringVar()
        self.var_fathername = StringVar()
        self.var_languagesknown = StringVar()
        self.var_qualification = StringVar()


# ============ title name ==============
        lbl_title = Label(self.root, text='BIO DATA MANAGEMENT SYSTEM', font=('time new roman', 37, 'bold'), fg='gray', bg='white')
        lbl_title.place(x=0, y=0, width=1530, height=50)

# ========     logo for title =========

        img_logo = Image.open('image/a2.png')
        img_logo = img_logo.resize((90, 50), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=270, y=0, width=50, height=50)

# === image frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=50, width=1530, height=160)

# === 1st

        img1 = Image.open('image/a3.jpeg')
        img1 = img1.resize((540, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)

# ======= 2nd

        img2 = Image.open('image/a4.png')
        img2 = img2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540, y=0, width=540, height=160)

# ====== 3rd

        img3 = Image.open('image/a5.jpeg')
        img3 = img3.resize((540, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1100, y=0, width=540, height=160)

        #main frame

        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=220, width=1500, height=560)

        # upper frame

        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Personal information', font=('time new roman', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)

 # labels and entry fields

        # Name
        lbl_name = Label(upper_frame, font=('arial', 12, 'bold'), text="Name:", bg='white')
        lbl_name.grid(row=0, column=0, padx=2, sticky=W)

        txt_name = ttk.Entry(upper_frame,textvariable=self.var_name, width=22, font=("arial", 11, "bold"))
        txt_name.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # GENDER
        lbl_gender = Label(upper_frame, text='Gender', font=('arial', 11, 'bold'), bg='white')
        lbl_gender.grid(row=0, column=2, padx=2, sticky=W)

        combo_gender = ttk.Combobox(upper_frame,textvariable=self.var_gender, font=('arial', 12, 'bold'), width=17, state='readonly')
        combo_gender['value']=('select Gender', 'Male', 'Female')
        combo_gender.current(0)
        combo_gender.grid(row=0, column=3, padx=2, pady=7)

        # email
        lbl_email = Label(upper_frame, font=('arial', 12, 'bold'), text="Email:", bg='white')
        lbl_email.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_email = ttk.Entry(upper_frame,textvariable=self.var_email, width=22, font=("arial", 11, "bold"))
        txt_email.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # married status
        lbl_marriedstatus = Label(upper_frame, font=('arial', 12, 'bold'), text="Married Status", bg='white')
        lbl_marriedstatus.grid(row=1, column=2, sticky=W, padx=2, pady=6)

        combo_marriedstatus = ttk.Combobox(upper_frame,textvariable=self.var_marriedstatus, state="readonly", font=('arial', 12, 'bold'), width=18)
        combo_marriedstatus['value'] = ("status", "Married", "unmarried")
        combo_marriedstatus.current(0)
        combo_marriedstatus.grid(row=1, column=3, padx=2, pady=7)

        # address
        lbl_address = Label(upper_frame, font=('arial', 12, 'bold'), text="Address:", bg='white')
        lbl_address.grid(row=2, column=0, padx=2, sticky=W, pady=7)

        txt_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=2, column=1, padx=2, pady=7)

        # dob
        lbl_dob = Label(upper_frame, font=('arial', 12, 'bold'), text="D.O.B:", bg='white')
        lbl_dob.grid(row=2, column=2, padx=2, sticky=W, pady=7)

        txt_dob = tk.Tk()


        txt_dob = DateEntry(upper_frame,textvariable=self.var_dob, selectmode='day')
        txt_dob.grid(row=2, column=3, padx=2, sticky=W, pady=7)

        # id proof
        com_txt_idproof = ttk.Combobox(upper_frame, state="readonly", font=("arial", 12, "bold"), width=18)
        com_txt_idproof['value'] = ("Select ID Proof:", "PAN CARD:", "ADHAAR CARD:", "DRIVING LICENCE:")
        com_txt_idproof.current(0)
        com_txt_idproof.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_idproof = ttk.Entry(upper_frame, textvariable=self.var_idproof, width=22, font=("arial", 11, "bold"))
        txt_idproof.grid(row=3, column=1, padx=2, pady=7)

        # phone
        lbl_phone = Label(upper_frame, font=("arial", 12, "bold"), text="Phone No:", bg="white")
        lbl_phone.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_phone = ttk.Entry(upper_frame, textvariable=self.var_phone, width=22, font=("arial", 11, "bold"))
        txt_phone.grid(row=3, column=3, padx=2, pady=7)

        # country
        lbl_country=Label(upper_frame, font=("arial", 12, "bold"), text="Country:", bg="white")
        lbl_country.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_country = ttk.Entry(upper_frame, textvariable=self.var_country, width=22, font=("arial", 11, "bold"))
        txt_country.grid(row=4, column=1, padx=2, pady=7)

        # state

        lbl_state = Label(upper_frame, font=("arial", 12, "bold"), text="state:", bg="white")
        lbl_state.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_state = ttk.Entry(upper_frame, textvariable=self.var_state, width=22, font=("arial", 11, "bold"))
        txt_state.grid(row=4, column=3, padx=2, pady=7)

        # nationality
        lbl_nationality = Label(upper_frame, font=("arial", 12, "bold"), text="Nationality:", bg="white")
        lbl_nationality.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_state = ttk.Entry(upper_frame, textvariable=self.var_nationality, width=22, font=("arial", 11, "bold"))
        txt_state.grid(row=0, column=5, padx=2, pady=7)

        # father name
        lbl_fathername = Label(upper_frame, font=("arial", 12, "bold"), text="Father's name:", bg="white")
        lbl_fathername.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_fathername = ttk.Entry(upper_frame, textvariable=self.var_fathername, width=22, font=("arial", 11, "bold"))
        txt_fathername.grid(row=1, column=5, padx=2, pady=7)

        #languages known

        lbl_languagesknown = Label(upper_frame, font=("arial", 12, "bold"), text="languages know:", bg="white")
        lbl_languagesknown.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        txt_languagesknown = ttk.Entry(upper_frame, textvariable=self.var_languagesknown, width=22, font=("arial", 11, "bold"))
        txt_languagesknown.grid(row=2, column=5, padx=2, pady=7)

        # qualification

        lbl_qualification = Label(upper_frame, font=("arial", 12, "bold"), text="Qualification:", bg="white")
        lbl_qualification.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        txt_qualification = ttk.Entry(upper_frame, textvariable=self.var_qualification, width=22, font=("arial", 11, "bold"))
        txt_qualification.grid(row=3, column=5, padx=2, pady=7)

        # Mask image

        img_mask = Image.open('image/a3.jpeg')
        img_mask = img1.resize((220, 220), Image.ANTIALIAS)
        self.photomask = ImageTk.PhotoImage(img_mask)

        self.img_mask = Label(upper_frame, image=self.photomask)
        self.img_mask.place(x=1030, y=0, width=220, height=220)

        # button frame

        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1290, y=20, width=170, height=210)

        btn_add=Button(button_frame, text="Save",command=self.add_data, font=("arial", 15, "bold"), width=13, bg='green', fg='white')
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update=Button(button_frame, text="Update",command=self.update_data, font=("arial", 15, "bold"), width=13, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(button_frame, text="Delete",command=self.delete_data, font=("arial", 15, "bold"), width=13, bg='red', fg='white')
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_clear = Button(button_frame, text="Clear",command=self.reset_data, font=("arial", 15, "bold"), width=13, bg='gray', fg='white')
        btn_clear.grid(row=3, column=0, padx=1, pady=5)


        # down frame

        down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Information Table', font=('time new roman',11,'bold'),fg='red')
        down_frame.place(x=10, y=280, width=1480, height=270)

        # search frame

        search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search Bio Data', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=3, y=0, width=1470, height=60)

        search_by=Label(search_frame, font=("arial", 15, "bold"),text="Search By:", fg='white', bg="red")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        #search

        self.var_com_search=StringVar()
        com_txt_search = ttk.Combobox(search_frame,textvariable=self.var_com_search, state="readonly", font=("arial", 12, "bold"), width=18)
        com_txt_search['value']=("select Option", "Phone", "id_proof")
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search=StringVar()
        txt_search = ttk.Entry(search_frame,textvariable=self.var_search, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_frame, text="Search",command=self.search_data, font=("arial", 11, "bold"), width=14, bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=5)

        btn_showall = Button(search_frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), width=14, bg="blue", fg="white")
        btn_showall.grid(row=0, column=4, padx=5)

        stayhome = Label(search_frame, text="Wear a Mask", font=("times new roman", 30, "bold"), fg="red", bg="white")
        stayhome.place(x=780, y=0, width=600, height=30)

        img_logo_mask=Image.open(r"image\a4.png")
        img_logo_mask = img_logo_mask.resize((50, 50), Image.ANTIALIAS)
        self.photoing_logo_mask = ImageTk.PhotoImage(img_logo_mask)

        self.logo=Label(search_frame, image=self.photoing_logo_mask)
        self.logo.place(x=900, y=0, width=50, height=30)

       # =======================  biodata table =================

        # table frame
        table_frame = Frame(down_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.biodata_table = ttk.Treeview(table_frame, columns=("name", "gender", "email", "marriedstatus", "address", "dob", "idproof", "phone", "country", "state", "nationality", "fathername", "languagesknown", "qualification"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.biodata_table.xview)
        scroll_y.config(command=self.biodata_table.yview)

        self.biodata_table.heading("name", text='Name')
        self.biodata_table.heading("gender", text="Gender")
        self.biodata_table.heading("email", text="Email")
        self.biodata_table.heading("marriedstatus", text="Married Status")
        self.biodata_table.heading("address", text="Address")
        self.biodata_table.heading("dob", text="DOB")
        self.biodata_table.heading("idproof", text="ID proof")
        self.biodata_table.heading("phone", text="Phone")
        self.biodata_table.heading("country", text="Country")
        self.biodata_table.heading("state", text="State")
        self.biodata_table.heading("nationality", text="Nationality")
        self.biodata_table.heading("fathername", text="Father's Name")
        self.biodata_table.heading("languagesknown", text="Languages Known")
        self.biodata_table.heading("qualification", text="Qualification")

        self.biodata_table['show'] = 'headings'

        self.biodata_table.column("name", width=100)
        self.biodata_table.column("gender", width=100)
        self.biodata_table.column("email", width=100)
        self.biodata_table.column("marriedstatus",width=100)
        self.biodata_table.column("address", width=100)
        self.biodata_table.column("dob", width=100)
        self.biodata_table.column("idproof", width=100)
        self.biodata_table.column("phone", width=100)
        self.biodata_table.column("country", width=100)
        self.biodata_table.column("state", width=100)
        self.biodata_table.column("nationality", width=100)
        self.biodata_table.column("fathername", width=100)
        self.biodata_table.column("languagesknown", width=100)
        self.biodata_table.column("qualification", width=100)


        self.biodata_table.pack(fill=BOTH, expand=1)
        self.biodata_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


    # ===================== function declarations =============


    def add_data(self):
        if self.var_name.get()=="" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='127.0.0.1', username='root', password='Manish5300@', database='mydatabase')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into biodata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                                self.var_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_marriedstatus.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_idproof.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_country.get(),
                                                                                                                self.var_state.get(),
                                                                                                                self.var_nationality.get(),
                                                                                                                self.var_fathername.get(),
                                                                                                                self.var_languagesknown.get(),
                                                                                                                self.var_qualification.get(),


                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Biodata has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)



        # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Manish5300@', database='mydatabase')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from biodata')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.biodata_table.delete(*self.biodata_table.get_children())
            for i in data:
                self.biodata_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor

    def get_cursor(self,event=""):
        cursor_row=self.biodata_table.focus()
        content=self.biodata_table.item(cursor_row)
        data=content['values']

        self.var_name.set(data[0])
        self.var_gender.set(data[1])
        self.var_email.set(data[2])
        self.var_marriedstatus.set(data[3])
        self.var_address.set(data[4])
        self.var_dob.set(data[5])
        self.var_idproof.set(data[6])
        self.var_phone.set(data[7])
        self.var_country.set(data[8])
        self.var_state.set(data[9])
        self.var_nationality.set(data[10])
        self.var_fathername.set(data[11])
        self.var_languagesknown.set(data[12])
        self.var_qualification.set(data[13])

    def update_data(self):
        if self.var_name.get()=="" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are sure update this biodata')
                if update>0:
                    conn=mysql.connector.connect(host='localhost', username='root', password='Manish5300@', database='mydatabase')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update biodata set name=%s,gender=%s,email=%s,marriedstatus=%s,address=%s,dob=%s,phone=%s,country=%s,state=%s,nationality=%s,fathername=%s,languagesknown=%s,qualification=%s where idproof=%s',(

                                                                                                                                                                                                                                       self.var_name.get(),
                                                                                                                                                                                                                                       self.var_gender.get(),
                                                                                                                                                                                                                                       self.var_email.get(),
                                                                                                                                                                                                                                       self.var_marriedstatus.get(),
                                                                                                                                                                                                                                       self.var_address.get(),
                                                                                                                                                                                                                                       self.var_dob.get(),

                                                                                                                                                                                                                                       self.var_phone.get(),
                                                                                                                                                                                                                                       self.var_country.get(),
                                                                                                                                                                                                                                       self.var_state.get(),
                                                                                                                                                                                                                                       self.var_nationality.get(),
                                                                                                                                                                                                                                       self.var_fathername.get(),
                                                                                                                                                                                                                                       self.var_languagesknown.get(),
                                                                                                                                                                                                                                       self.var_qualification.get(),
                                                                                                                                                                                                                                       self.var_idproof.get()

                                                                                                                                                                                                                                       ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Biodata successfully updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due to:{str(es)}', parent=self.root)

    # delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error', "All Fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this biodata', parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Manish5300@',database='mydatabase')
                    my_cursor = conn.cursor()
                    sql='delete from biodata where idproof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Biodata successfully Deleted', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due to:{str(es)}', parent=self.root)

    #reset
    def reset_data(self):
        self.var_name.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_marriedstatus.set("")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_idproof.set("Enter ID.no")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_state.set("")
        self.var_nationality.set("")
        self.var_fathername.set("")
        self.var_languagesknown.set("")
        self.var_qualification.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('error','Please select option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Manish5300@',database='mydatabase')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from biodata where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.biodata_table.delete(*self.biodata_table.get_children())
                    for i in rows:
                        self.biodata_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due To:{str(es)}',parent=self.root)













if __name__=="__main__":
    root = Tk()
    obj = BIODATA(root)
    root.mainloop()

