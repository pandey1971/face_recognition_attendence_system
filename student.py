from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
       def __init__(self,root):
           self.root=root
           self.root.geometry("1530x790+0+0")
           self.root.title("face recognition system")

           #==============variables==============
           self.var_dep=StringVar()
           self.var_course=StringVar()
           self.var_year=StringVar()
           self.var_sem=StringVar()
           self.var_id=StringVar()
           self.var_name=StringVar()
           self.var_rollno=StringVar()
           
           
           img=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\face1.jpg")
           img=img.resize((500,130),Image.ANTIALIAS)
           self.photoimg=ImageTk.PhotoImage(img)

           f_lbl=Label(self.root,image=self.photoimg)
           f_lbl.place(x=0,y=0,width=500,height=130)

           
           img1=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\face1.jpg")
           img1=img1.resize((500,130),Image.ANTIALIAS)
           self.photoimg1=ImageTk.PhotoImage(img1)

           f_lbl=Label(self.root,image=self.photoimg1)
           f_lbl.place(x=500,y=0,width=500,height=130)

           img2=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\face1.jpg")
           img2=img2.resize((500,130),Image.ANTIALIAS)
           self.photoimg2=ImageTk.PhotoImage(img2)

           f_lbl=Label(self.root,image=self.photoimg2)
           f_lbl.place(x=1000,y=0,width=500,height=130)


           img4=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\facedet.jpg")
           img4=img4.resize((1530,710),Image.ANTIALIAS)
           self.photoimg4=ImageTk.PhotoImage(img4)

           bg_img=Label(self.root,image=self.photoimg4)
           bg_img.place(x=0,y=130,width=1530,height=710)


           title_lbl=Label(bg_img,text="STUDENT MANAGEMENT AREA",font=("times new roman",35,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1530,height=45)


           main_frame=Frame(bg_img,bd=2,bg="white")
           main_frame.place(x=20,y=50,width=1498,height=600)

           #leftframe

          
           left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",15,"bold"))
           left_frame.place(x=10,y=10,width=730,height=580)

           img5=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\face1.jpg")
           img5=img5.resize((720,130),Image.ANTIALIAS)
           self.photoimg5=ImageTk.PhotoImage(img5)

           f_lbl=Label(left_frame,image=self.photoimg5)
           f_lbl.place(x=5,y=0,width=720,height=130)

           #CURRENT COURSE
           current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course info")
           current_frame.place(x=15,y=135,width=720,height=150)
           #deprtment 
           dep_label=Label(current_frame,text="department",font=("times new roman",12,"bold"))
           dep_label.grid(row=0,column=0,padx=10)

           dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
           dep_combo["values"]=("Select Department","CSE","IT","MECH","ELECTRO","AGRICULTURE")
           dep_combo.current(0)
           dep_combo.grid(row=0,column=1,padx=2,pady=10)

           

           course_label=Label(current_frame,text="Course",font=("times new roman",12,"bold"))
           course_label.grid(row=0,column=2,padx=10)

           course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
           course_combo["values"]=("course","FE","TE","BE","UG","SG")
           course_combo.current(0)
           course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)




           
           year_label=Label(current_frame,text="year",font=("times new roman",12,"bold"))
           year_label.grid(row=1,column=0,padx=10,sticky=W)

           year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
           year_combo["values"]=("year","2021","2022","2023","2024")
           year_combo.current(0)
           year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)



           sem_label=Label(current_frame,text="semester",font=("times new roman",12,"bold"))
           sem_label.grid(row=1,column=2,padx=10,sticky=W)

           sem_combo=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="read only")
           sem_combo["values"]=("semester","1","2","3","4")
           sem_combo.current(0)
           sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


           #CURRENT COURSE
           class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student info")
           class_student_frame.place(x=5,y=250,width=720,height=300)


           StudentId_label=Label(class_student_frame,text="Student_ID:",font=("times new roman",13,"bold"))
           StudentId_label.grid(row=0,column=0,padx=10,sticky=W)

           student_ID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
           student_ID_entry.grid(row=0,column=1,padx=10,sticky=W)


           Studentname_label=Label(class_student_frame,text="Student_name:",font=("times new roman",13,"bold"))
           Studentname_label.grid(row=0,column=2,padx=10,sticky=W)

           studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
           studentname_entry.grid(row=0,column=3,padx=10,sticky=W)


           roll_label=Label(class_student_frame,text="Rollno",font=("times new roman",13,"bold"))
           roll_label.grid(row=1,column=0,padx=10,sticky=W)

           roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollno,width=20,font=("times new roman",13,"bold"))
           roll_entry.grid(row=1,column=1,padx=10,sticky=W)

           #radio
           self.var_radio1=StringVar()
           radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="yes")
           radiobtn1.grid(row=5,column=0)

           radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="NO photo sample",value="NO")
           radiobtn2.grid(row=5,column=1)

           #btn frame
           btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
           btn_frame.place(x=0,y=200,width=715,height=70)


           save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
           save_btn.grid(row=0,column=0)

           update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
           update_btn.grid(row=0,column=1)



           DELETE_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
           DELETE_btn.grid(row=0,column=2)




           reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
           reset_btn.grid(row=0,column=3)


           takephoto_btn=Button(btn_frame,command=self.generate_datase,text="TakePhotoSample",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
           takephoto_btn.grid(row=1,column=0)


           updatephot_btn=Button(btn_frame,text="UPDATE pHoto",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
           updatephot_btn.grid(row=1,column=1)



           

#right label frame
           right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",15,"bold"))
           right_frame.place(x=680,y=10,width=750,height=580)

           #======search system===========
           search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",15,"bold"))
           search_frame.place(x=5,y=135,width=710,height=70) 
           
           search_lbl=Label(search_frame,bd=1,bg="red",text="search by",font=("times new roman",12,"bold"),fg="white")
           search_lbl.grid(row=0,column=0,padx=10,sticky=W)

           search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="read only")
           search_combo["values"]=("select","Rollno","Student_ID")
           search_combo.current(0)
           search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


           
           s_entry=ttk.Entry(search_frame ,width=20,font=("times new roman",13,"bold"))
           s_entry.grid(row=0,column=2,padx=10,sticky=W)
           
           
           search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
           search_btn.grid(row=0,column=3,padx=4)

           
           showall_btn=Button(search_frame,text="Showall",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
           showall_btn.grid(row=0,column=4,padx=4)


           #============table frame================
   


           table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
           table_frame.place(x=5,y=210,width=710,height=330)

           scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
           scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL) 

           self.student_table=ttk.Treeview(table_frame,columns=("dep","Course","year","semester","id","name","rollno","Photosamples"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

           scroll_x.pack(side=BOTTOM,fill=X)
           scroll_y.pack(side=RIGHT,fill=Y)
           scroll_x.config(command=self.student_table.xview)
           scroll_y.config(command=self.student_table.yview)

           self.student_table.heading("dep",text="Department")
           self.student_table.heading("Course",text="course")
           self.student_table.heading("year",text="Year")
           self.student_table.heading("semester",text="Semester")
           self.student_table.heading("id",text="ID")
           self.student_table.heading("name",text="NAME")
           self.student_table.heading("rollno",text="Rollno")
           self.student_table.heading("Photosamples",text="photosamples")
           self.student_table["show"]="headings"

           self.student_table.column("dep",width=100)
           self.student_table.column("Course",width=100)
           self.student_table.column("year",width=100)
           self.student_table.column("semester",width=100)
           self.student_table.column("id",width=100)
           self.student_table.column("name",width=100)
           self.student_table.column("rollno",width=100)
           self.student_table.column("Photosamples",width=100)

           self.student_table.pack(fill=BOTH,expand=1)
           self.student_table.bind("<ButtonRelease>",self.get_cursor)
           self.fetch_data()
#====fucntion declaration========================
       
       def add_data(self):
           if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="":
               messagebox.showerror("Error","ALL FIELDS REQUIRED",parent=self.root)
           else:
               try:
                   conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@1234",database="face_recognizer")
                   my_cursor=conn.cursor()
                   my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                    
                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_rollno.get(),
                                                                                            self.var_radio1.get()

                                                       
                                                                                         ))
               
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("SUCESS","DETAILS ADDED SUCCESFULLY",parent=self.root)


               except Exception as es:
                   messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)

               
       #====================fetch data======================
       def fetch_data(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@1234",database="face_recognizer")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from student ")
           data=my_cursor.fetchall()

           if len(data)!=0:
               self.student_table.delete(*self.student_table.get_children())
               for i in data:
                   self.student_table.insert("",END,values=i)
               conn.commit()
           conn.close()    
           

       #===================get cursor===================
       def get_cursor(self,event=""):
           cursor_focus=self.student_table.focus()
           content=self.student_table.item(cursor_focus)
           data=content["values"]
           self.var_dep.set(data[0]),
           self.var_course.set(data[1]),
           self.var_year.set(data[2]),
           self.var_sem.set(data[3]),
           self.var_id.set(data[4]),
           self.var_name.set(data[5]),
           self.var_rollno.set(data[6]),
           self.var_radio1.set(data[7])
                  
       #=================update==============
       def update_data(self):
           if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="":
               messagebox.showerror("Error","ALL FIELDS REQUIRED",parent=self.root) 
           else:
               try: 
                   Update=messagebox.askyesno("UPDATE","WANNA UPDATE DETAILS",parent=self.root)
                   if Update>0:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@1234",database="face_recognizer")
                       my_cursor=conn.cursor()
                       my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,rollno=%s,photosamples=%s where id=%s",(

                                                                                                                       self.var_dep.get(),
                                                                                                                       self.var_course.get(),
                                                                                                                       self.var_year.get(),
                                                                                                                       self.var_sem.get(),
                                                                                                                       self.var_name.get(),
                                                                                                                       self.var_rollno.get(),
                                                                                                                       self.var_radio1.get(),
                                                                                                                       self.var_id.get()
                                                                                                                      

                                                                                                                ))
                   else:
                       if not Update: 
                           return
                   messagebox.showinfo("sucess","details updated",parent=self.root)
                   conn.commit()
                   self.fetch_data()
                   conn.close()
               except Exception as es:
                   messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)

   #=============delte=================

       def delete_data(self):
           if self.var_id.get()=="":
               messagebox.showerror("ERROR","STUDENT ID REQUIRED",parent=self.root)
           else:
               try:
                   delete=messagebox.askyesno("STUDENT DELETE PAGE","DO YOU WANT TO DELETE DETAILS",parent=self.root)
                   if delete>0:
                       conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@1234",database="face_recognizer")
                       my_cursor=conn.cursor()
                       sql="delete from student where id=%s"
                       val=(self.var_id.get(),)
                       my_cursor.execute(sql,val)
                   else:
                       if not delete:
                           return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete","succesfully deted",parent=self.root)
               except Exception as es:
                   messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)

               
#============reset===============
       def reset_data(self):
           self.var_dep.set("Select Department")
           self.var_course.set("course")
           self.var_year.set("year")
           self.var_sem.set("semester")
           self.var_id.set("")
           self.var_name.set("")
           self.var_rollno.set("")
           self.var_radio1.set("")

        #=======================generate data set==========================================

       def generate_datase(self):
           if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="":
                   messagebox.showerror("Error","ALL FIELDS REQUIRED",parent=self.root) 
           else:
               try: 
                   conn=mysql.connector.connect(host="localhost",username="root",password="Shubham@1234",database="face_recognizer")
                   my_cursor=conn.cursor()
                   my_cursor.execute("select * from student")
                   my_result=my_cursor.fetchall()
                   id=0
                   for x in my_result:
                       id+=1
                   my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,rollno=%s,photosamples=%s where id=%s",(

                                                                                                                       self.var_dep.get(),
                                                                                                                       self.var_course.get(),
                                                                                                                       self.var_year.get(),
                                                                                                                       self.var_sem.get(),
                                                                                                                       self.var_name.get(),
                                                                                                                       self.var_rollno.get(),
                                                                                                                       self.var_radio1.get(),
                                                                                                                       self.var_id.get()==id+1
                                                                                                                      

                                                                                                                )) 
                   conn.commit()
                   self.fetch_data()
                   self.reset_data()
                   conn.close()
                   #====================load ===========
                   
                   face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                   def face_cropped(img):
                       gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                       faces=face_classifier.detectMultiScale(gray,1.3,5)
                       for (x,y,w,h) in faces:
                           face_cropped=img[y:y+h,x:x+w]
                           return face_cropped

                   cap=cv2.VideoCapture(0)
                   img_id=0
                   while True:
                       ret,frame_my=cap.read()
                       if face_cropped(frame_my) is not None:
                           img_id+=1
                           face=cv2.resize(face_cropped(frame_my),(450,450))
                           face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                           file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                           cv2.imwrite(file_name_path,face)
                           cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                           cv2.imshow("Crooped Face",face)

                       if cv2.waitKey(1)==13 or int(img_id)==100:
                           break
                   cap.release()
                   cv2.destroyAllWindows()
                   messagebox.showinfo("result","GENERATING DATASET COMPLETED",parent=self.root)     

               except Exception as es:
                   messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)
        
                       



    
            
           






if __name__=="__main__":
       root=Tk()
       obj=Student(root)
       root.mainloop()