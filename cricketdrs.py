import tkinter
from tkinter.constants import ANCHOR
import PIL.Image , PIL.ImageTk #Python img lib to display img in tkinter
import cv2
from functools import partial # Gives func. argument b/c tkinter button command func. can't have parametrized func.
import threading #It allows you to have different parts of your process run concurrently
import imutils #Resizing Image
import time

#-----------------------------------------------------------------------------------------------------------------------#
stream = cv2.VideoCapture(r"C:\Users\KIIT\Desktop\Apps\Project\DRS System\iplclip.mp4")
flag= True
def play(speed):
   frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
   stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
   global flag 
   grabbed,frame = stream.read()
   if not grabbed:
       exit()
   frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
   frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) 
   canvas.image= frame
   canvas.create_image(0,0,image=frame,anchor= tkinter.NW)
   if flag:
        canvas.create_text(120,30,fill='red',text="DECISION PENDING")
   flag= not flag
    
def pending(decision):
    # 1. Display Decision Pending Image
    frame = cv2.cvtColor(cv2.imread(r"C:\Users\KIIT\Desktop\Apps\Project\DRS System\IPL_v1.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width= SET_WIDTH,height= SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) #Making Compatible with Tkinter UI -> Anchor ->set position ->North West
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor= tkinter.NW)

    # 2. wait 1 sec.
    time.sleep(1)
    # 3. display sponsor image
    frame = cv2.cvtColor(cv2.imread(r"C:\Users\KIIT\Desktop\Apps\Project\DRS System\sponsoripl.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width= SET_WIDTH,height= SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) #Making Compatible with Tkinter UI -> Anchor ->set position ->North West
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor= tkinter.NW)
    # 4. wait 1.5 sec
    time.sleep(1.5)
    # 5. Display Out/Not out Image
    if decision== 'out':
        decisionImg = "C:\\Users\\KIIT\Desktop\\Apps\\Project\\DRS System\\outip.png"
    else:
        decisionImg = "C:\\Users\\KIIT\Desktop\\Apps\\Project\\DRS System\\iplnotout.jpg"

    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width= SET_WIDTH,height= SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame)) #Making Compatible with Tkinter UI -> Anchor ->set position ->North West
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor= tkinter.NW)
    
def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon =1
    thread.start() #Starts Thread
    print("Player is OUT")
def not_out():
    thread = threading.Thread(target=pending,args=("not_out",))
    thread.daemon =1
    thread.start()
    print("Player is NOT OUT")

#-----------------------------------------------------------------------------------------------------------------------#

SET_WIDTH = 650 # Height & width of main screen
SET_HEIGHT = 368

window = tkinter.Tk() #Making Main Window
window.title("EMPIRE DECISION")
cv_img = cv2.cvtColor(cv2.imread(r"C:\Users\KIIT\Desktop\Apps\Project\DRS System\wlcm.png"),cv2.COLOR_BGR2RGB) #Convert Color
canvas = tkinter.Canvas(window, width = SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img)) #read img to array
image_on_canvas= canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack() #alline all image in respective place

#-----------------------------------------------------------------------------------------------------------------------#

#Buttons for Playback

btn= tkinter.Button(window,text="<< 𝗣𝗥𝗘𝗩𝗜𝗢𝗨𝗦 (Fast)",width=50,command=partial(play,-25))
btn.pack()
btn= tkinter.Button(window,text="<< 𝗣𝗥𝗘𝗩𝗜𝗢𝗨𝗦 (Slow)",width=50,command=partial(play,-2))
btn.pack()
btn= tkinter.Button(window,text=" 𝙉𝙀𝙓𝙏 (Fast) >>",width=50,command=partial(play,25))
btn.pack()
btn= tkinter.Button(window,text=" 𝙉𝙀𝙓𝙏 (Slow) >>",width=50,command=partial(play,2))
btn.pack()
btn= tkinter.Button(window,text=" 【Ｇｉｖｅ　ＯＵＴ】 ",width=50, bg='red',activebackground='white',command=out)
btn.pack()
btn= tkinter.Button(window,text=" 【Ｇｉｖｅ　ＮＯＴ　ＯＵＴ】 ",width=50,bg='green',activebackground='white',command=not_out)
btn.pack()

#-----------------------------------------------------------------------------------------------------------------------#

window.mainloop() #Loop until app closed