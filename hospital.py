from tkinter import *
from tkinter import ttk
# import random
# import time
# import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1270x1000+0+0")


        self.Name_of_tablets=StringVar()
        self.Dose=StringVar()
        self.Number_Of_Tablets=StringVar()
        self.Patient_Name=StringVar()
        self.Patient_Address=StringVar()
        

        lbl_title = Label(self.root,bd=17,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="green",bg="yellow",font=("times new roman",40,"bold"))
        lbl_title.pack(side=TOP,fill=X)

        # ------------------------------------------DATAFRAME---------------------------------------------
        Data_Frame = Frame(self.root,bd=10,relief=RIDGE,)
        Data_Frame.place(x=0,y=100,width=1270,height=290)

        Data_Frame_Left = LabelFrame(Data_Frame,bd=8,padx=10,relief=RIDGE,fg="blue",font=("arial",12,"bold"),text="Patient Information")
        Data_Frame_Left.place(x=0,y=5,width=700,height=260)

        Data_Frame_Right = LabelFrame(Data_Frame,bd=8,padx=10,relief=RIDGE,fg="red",font=("arial",12,"bold"),text="Prescription")
        Data_Frame_Right.place(x=750,y=4,width=450,height=260)


       
    #    ----------------------------------------------BUTTON FRAME---------------------------------------------
        Button_Frame = Frame(self.root,bd=10,relief=RIDGE,)
        Button_Frame.place(x=0,y=395,width=1270,height=40)

    # # -------------------------------------------------Details frame-------------------------------------------
        Details_Frame = Frame(self.root,bd=10,relief=RIDGE)
        Details_Frame.place(x=0,y=445,width=1270,height=200)

    # # --------------------------------------------------Data frame left------------------------------------------
        lbl_Name_Tablet = Label(Data_Frame_Left,text="Names of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Name_Tablet.grid(row=0,column=0)

        Com_Name_Tablet = ttk.Combobox(Data_Frame_Left,textvariable=self.Name_of_tablets,font=("times new roman",12,"bold"),width=50)

        Com_Name_Tablet["values"]=("Paracitamol","Corona Vacacine","Sinovac","Moderna")
        Com_Name_Tablet.current(0)
        Com_Name_Tablet.grid(row=0,column=1)

    

        lbl_Dose=Label(Data_Frame_Left,font=("times new roman",12,"bold"),text="Dose: ",padx=2,pady=4)
        lbl_Dose.grid(row=2,column=0,sticky=W)
        txt_Dose = Entry(Data_Frame_Left,textvariable=self.Dose,font=("times new roman",12,"bold"),width=50)
        txt_Dose.grid(row=2,column=1)

        lbl_No_Of_Tablets=Label(Data_Frame_Left,font=("times new roman",12,"bold"),text="No Of Tablets: ",padx=2,pady=6)
        lbl_No_Of_Tablets.grid(row=3,column=0,sticky=W)
        txt_No_Of_Tablets = Entry(Data_Frame_Left,textvariable=self.Number_Of_Tablets,font=("times new roman",12,"bold"),width=50)
        txt_No_Of_Tablets.grid(row=3,column=1)

     


        lbl_Patient_Name=Label(Data_Frame_Left,font=("times new roman",12,"bold"),text="Patient Name: ",padx=2,pady=6)
        lbl_Patient_Name.grid(row=7,column=0,sticky=W)
        txt_Patient_Name = Entry(Data_Frame_Left,textvariable=self.Patient_Name,font=("times new roman",12,"bold"),width=50)
        txt_Patient_Name.grid(row=7,column=1)


        lbl_Patient_Address=Label(Data_Frame_Left,font=("times new roman",12,"bold"),text="Patient Address: ",padx=2,pady=6)
        lbl_Patient_Address.grid(row=8,column=0,sticky=W)
        txt_Patient_Address = Entry(Data_Frame_Left,textvariable=self.Patient_Address,font=("times new roman",12,"bold"),width=50)
        txt_Patient_Address.grid(row=8,column=1)

        # ---------------------------------------DATAFRAME RIGHT----------------------------------------------

        self.txt_Presciption = Text(Data_Frame_Right,font=("arial",12,"bold"),width=43,height=11,padx=2,pady=6)
        self.txt_Presciption.grid(row=0,column=0)

        # -------------------------------------------BUTTONS-------------------------------------------
        btn_Presciption = Button(Button_Frame,command=self.iPresciption,text="Presciption",bg="yellow",fg="black",font=("arial",8,"bold"),width=44,padx=1,pady=1)
        btn_Presciption.grid(row=0,column=0)

        btn_Presciption_Data = Button(Button_Frame,command=self.iPrescriptionData,text="Presciption Data",bg="blue",fg="white",font=("arial",8,"bold"),width=43,padx=1,pady=1)
        btn_Presciption_Data.grid(row=0,column=1)

        btn_Delete = Button(Button_Frame,command=self.idelete,text="Delete",bg="black",fg="white",font=("arial",8,"bold"),width=43,padx=1,pady=1)
        btn_Delete.grid(row=0,column=3)

        btn_Clear = Button(Button_Frame,command=self.Clear,text="Clear",bg="red",fg="white",font=("arial",8,"bold"),width=43,padx=1,pady=1)
        btn_Clear.grid(row=0,column=4)
    # =========================================Scrollbar ========================================================
        scroll_x = ttk.Scrollbar(Details_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Details_Frame,orient=VERTICAL)

        self.Hospital_Table=ttk.Treeview(Details_Frame,columns=("NameOfTable","Dose","NoOfTablets",
                   "PatientName","PatientAddress"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.Hospital_Table.xview)
        scroll_y=ttk.Scrollbar(command=self.Hospital_Table.yview)

        self.Hospital_Table.heading("NameOfTable",text="Name_Of_Tablets")
        self.Hospital_Table.heading("Dose",text="Dose")
        self.Hospital_Table.heading("NoOfTablets",text="No_Of_Tablets")
        self.Hospital_Table.heading("PatientName",text="Patient Name")
        self.Hospital_Table.heading("PatientAddress",text="Patient Address")

        self.Hospital_Table["show"]="headings"

        self.Hospital_Table.column("NameOfTable",width=90)
        self.Hospital_Table.column("Dose",width=80)
        self.Hospital_Table.column("NoOfTablets",width=80)
        self.Hospital_Table.column("PatientName",width=80)
        self.Hospital_Table.column("PatientAddress",width=80)
    

        self.Hospital_Table.pack(fill=BOTH,expand=1)
        self.Hospital_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()


        # =================================================================Functinality Declration===================================================================
    def iPrescriptionData(self):
        if self.Name_of_tablets.get()=="" or self.Dose.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Abhishek@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s)",(
                self.Name_of_tablets.get(),
                self.Dose.get(),
                self.Number_Of_Tablets.get(),
                self.Patient_Name.get(),
                self.Patient_Address.get()
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")


    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Abhishek@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Name_of_Tablet=%s,No_Of_Tablets=%s,Patient_Name=%s,Patient_Address=%s  where Dose=%s",(
            self.Name_of_tablets.get(),
            self.Number_Of_Tablets.get(),
            self.Patient_Name.get(),
            self.Patient_Address.get(),
            self.Dose.get()
        ))


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Abhishek@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Hospital_Table.delete(*self.Hospital_Table.get_children())
            for i in rows:
                self.Hospital_Table.insert("",END,values=i)
            conn.commit()
        conn.close()



    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Abhishek@123",database="mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Dose=%s"
        value = (self.Dose.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")



    def Clear(self):
        self.Name_of_tablets.set("")
        self.Dose.set("")
        self.Number_Of_Tablets.set("")
        self.Patient_Name.set("")
        self.Patient_Address.set("")
        self.txt_Presciption.delete("1.0",END)



    
    def get_cursor(self,event=""):
        cursor_rows=self.Hospital_Table.focus()
        content=self.Hospital_Table.item(cursor_rows)
        row=content["values"]
        self.Name_of_tablets.set(row[0])
        self.Dose.set(row[1])
        self.Number_Of_Tablets.set(row[2])
        self.Patient_Name.set(row[3])
        self.Patient_Address.set(row[4])
    

    def iPresciption(self):
        self.txt_Presciption.insert(END,"Name_Of_Tablets:\t\t\t"+self.Name_of_tablets.get()+"\n")
        self.txt_Presciption.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txt_Presciption.insert(END,"Number_Of_Tablets:\t\t\t"+self.Number_Of_Tablets.get()+"\n")
        self.txt_Presciption.insert(END,"Patient_Name:\t\t\t"+self.Patient_Name.get()+"\n")
        self.txt_Presciption.insert(END,"Patient_Address:\t\t\t"+self.Patient_Address.get()+"\n")   



root = Tk()
ob = Hospital(root)
root.mainloop()


