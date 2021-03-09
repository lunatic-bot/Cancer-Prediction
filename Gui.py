from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from tkinter.filedialog import askopenfilename
import pickle 
 


root = Tk()

def CancerPrediction(num):
    if num==0:
        return 'Actinic keratoses'
    if num==1:
        return 'Basal cell carcinoma'
    if num==2:
        return 'Benign keratosis-like lesions'
    if num==3:
        return 'Dermatofibroma'
    if num==4:
        return 'Melanoma'
    if num==5:
        return "Melanocytic nevi"
    if num==6:
        return 'Vascular lesions'

def fun():
    try:
        path=askopenfilename(filetypes=[("Image File",'.jpg')])
        im = Image.open(path)
        im = im.resize((200, 200))
        #pixels=np.matrix(im.getdata())
        photo = ImageTk.PhotoImage(im)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x=300, y=200)
        pickle_in = open("C:\\Users\\Arpit\\Cancer_finalized_model.pickle","rb")
        cancer_prediction = pickle.load(pickle_in)

        img = im.resize((28,28)) 
        pixels = np.matrix(img.getdata())
        ini_array1 = np.array(pixels)
        result = ini_array1.flatten() 
        temp=result.reshape(1,-1)
        if cancer_prediction.predict(temp)[0]<=6 or cancer_prediction.predict(temp)[0]>=0:
            Label(root,text="Report : Cancerous ",font='Papyrus 12 bold',fg='Black',pady=1).place(x=800,y=250)
            result = "Cancer Type:    "+CancerPrediction(cancer_prediction.predict(temp)[0])
        else:
           #result=" Not Cancerous"
           Label(root,text="Report :  Not Cancerous ",font='Papyrus 12 bold',fg='Black',pady=1).place(x=800,y=250)
           
        Label(root,text=result,font='Papyrus 12 bold',fg='Black',pady=1).place(x=800,y=300)

    except:
        pass


root.title("Cancer Prediction")
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()
#root.attributes('-fullscreen',True)
root.geometry("1000x800")
#root.geometry(root.winfo_screenwidth(),root.winfo_screenheight())
Label(root,width=120,height=5,text= "Cancer Type Detection",font='Papyrus 16 bold',fg='Black',bg='Sky Blue',pady=1).pack()

root.minsize(200,100)
#photo = tkinter.PhotoImage(file = "logo.png")
#label = tkinter.Label(image = photo).pack()
btn1=Button(root,fg="white",bg="Gray",text="Select image",command=fun,width=50)
Label(root,text="Your Results",font='Black',fg='Black',pady=1,width=40).place(x=800,y=500)
btn1.place(x=235,y=500)

root.mainloop()
