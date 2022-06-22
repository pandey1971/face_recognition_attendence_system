from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train 
from face_recognition import Face_recognition

class face_recognition_system:
   def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("face recognition system")
       
       img=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\download.jpg")
       img=img.resize((500,130),Image.ANTIALIAS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=500,height=130)

       #second image
       img1=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\download.jpg")
       img1=img1.resize((500,130),Image.ANTIALIAS)
       self.photoimg1=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=500,y=0,width=500,height=130)

       img2=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\download.jpg")
       img2=img2.resize((500,130),Image.ANTIALIAS)
       self.photoimg2=ImageTk.PhotoImage(img2)

       f_lbl=Label(self.root,image=self.photoimg2)
       f_lbl.place(x=1000,y=0,width=500,height=130)

  #==bg
       img3=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\facedet.jpg")
       img3=img3.resize((1530,710),Image.ANTIALIAS)
       self.photoimg3=ImageTk.PhotoImage(img3)

       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)


       title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
       title_lbl.place(x=0,y=0,width=1530,height=45)
   
   #student button

       img4=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\child.jpg")
       img4=img4.resize((220,220),Image.ANTIALIAS)
       self.photoimg4=ImageTk.PhotoImage(img4)

       b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
       b1.place(x=200,y=100,width=220,height=220)

       b1_lb=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2")
       b1_lb.place(x=200,y=300,width=220,height=40)
       

       img5=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\face.jpg")
       img5=img5.resize((220,220),Image.ANTIALIAS)
       self.photoimg5=ImageTk.PhotoImage(img5)

       b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
       b1.place(x=500,y=100,width=220,height=220)

       b1_lb=Button(bg_img,text="detect face",cursor="hand2",command=self.face_data)
       b1_lb.place(x=500,y=300,width=220,height=40)




       
       img6=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\att.jpg")
       img6=img6.resize((220,220),Image.ANTIALIAS)
       self.photoimg6=ImageTk.PhotoImage(img6)

       b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
       b1.place(x=800,y=100,width=220,height=220)

       b1_lb=Button(bg_img,text="ATTENDANCE",cursor="hand2")
       b1_lb.place(x=800,y=300,width=220,height=40)



       
       
       img7=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\att.jpg")
       img7=img7.resize((220,220),Image.ANTIALIAS)
       self.photoimg7=ImageTk.PhotoImage(img7)

       b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
       b1.place(x=200,y=400,width=220,height=220)

       b1_lb=Button(bg_img,text="TRAIN FACE",cursor="hand2",command=self.train_data)
       b1_lb.place(x=200,y=600,width=220,height=40)


       
       
       img8=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\att.jpg")
       img8=img8.resize((220,220),Image.ANTIALIAS)
       self.photoimg8=ImageTk.PhotoImage(img8)

       b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
       b1.place(x=500,y=380,width=220,height=220)

       b1_lb=Button(bg_img,text="photos",cursor="hand2",command=self.open_img)
       b1_lb.place(x=500,y=500,width=220,height=40)


       
       
#==============functions buttons========================
   def student_details(self):
     self.__new_window=Toplevel(self.root)
     self.app=Student(self.__new_window)
   
   def open_img(self):
       os.startfile("data")

    
   def train_data(self):
         self.__new_window=Toplevel(self.root)
         self.app=Train(self.__new_window)
       
   def face_data(self):
         self.__new_window=Toplevel(self.root)
         self.app=Face_recognition(self.__new_window)
         





if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()