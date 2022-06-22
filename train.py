from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
       def __init__(self,root):
           self.root=root
           self.root.geometry("1530x790+0+0")
           self.root.title("face recognition system")

          
           title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1530,height=45)

           imgt=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\face1.jpg")
           imgt=imgt.resize((1530,325),Image.ANTIALIAS)
           self.photoimgt=ImageTk.PhotoImage(imgt)

           f_lbl=Label(self.root,image=self.photoimgt)
           f_lbl.place(x=0,y=55,width=1530,height=200)


           imgb=Image.open(r"C:\Users\sp355\OneDrive\Desktop\face recognition\icon\face1.jpg")
           imgb=imgb.resize((1530,325),Image.ANTIALIAS)
           self.photoimgb=ImageTk.PhotoImage(imgb)

           f_lbl=Label(self.root,image=self.photoimgb)
           f_lbl.place(x=0,y=440,width=1530,height=350)


           b1_lb=Button(self.root,text="TRAIN FACE",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
           b1_lb.place(x=0,y=380,width=1530,height=60)

       def train_classifier(self):
           data_dir=("data")
           path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

           faces=[]
           ids=[]

           for image in path:
               img=Image.open(image).convert('L')
               imageNp=np.array(img,'uint8')
               id=int(os.path.split(image)[1].split('.')[1])

               faces.append(imageNp)
               ids.append(id)
               cv2.imshow("TRAINING",imageNp)
               cv2.waitKey(1)==13
           ids=np.array(ids)
       
           clf=cv2.face.LBPHFaceRecognizer_create()
           clf.train(faces,ids)
           clf.write("classifier.xml")
           cv2.destroyAllWindows()
           messagebox.showinfo("Result","TRaining completed")


           



if __name__=="__main__":
       root=Tk()
       obj=Train(root)
       root.mainloop()          