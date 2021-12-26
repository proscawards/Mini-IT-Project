from tkinter import *
import os
from os import walk
import json
class LostTicket:
    def closebuttonwindow (self):
        pass

    def __init__ (self):
        global master
        master=Toplevel()
        self.openJsonFile()
        self.CurrentUser=self.data[0]['currentuser']
        master.title("Long Distance Bus Tickets Booking System (Login As: {})".format(self.CurrentUser))        
        master.resizable (0,0)
        master.attributes("-toolwindow",1)
        master.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        w = 500 
        h = 400 
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        backImg=PhotoImage(file='backtxt.png')
        self.backbtn=Button(master, image=backImg , command= lambda: master.destroy())
        self.backbtn.place(x=200,y=360)
        self.readText()
        self.DisplayHistory()
        master.mainloop()
        
    def openJsonFile(self):
        with open ('Master.json' , 'r') as json_file:
            self.data = json.load (json_file)
        return self.data

    def DisplayHistory(self):
        global frame
        self.frames=[]
        self.PBimg=PhotoImage(file='pastbooking.png')
        label=Label(master, image=self.PBimg)
        label.grid(row=1)
        self.nextImg=PhotoImage(file='next.png')
        if len(self.listfiles) > 4 :
            self.nextpagebtn = Button(master , image=self.nextImg, relief =FLAT , command= lambda: self.displaynextpage())
            self.nextpagebtn.place(x=420, y=370)
            number=4
        else:
            number=len(self.listfiles)
        for f in range (0,number):
            Fbutton=Frame(master)
            Fbutton.place(x=100,y=50+f*75)
            self.frames.append(Fbutton)
            
        self.combo=PhotoImage(file='combo.png')
        self.buttons=[]


        for i in range(0,number):
            historybtn = Button(self.frames[i], text =('{:<29s}'.format("Destination: " + self.destination[i])+ "{:>20s}".format(str(self.seats[i]) +' Seats') +'\n'
                                        +'{:<47s}'.format('Date Purchased: '+self.datepurchase[i])+'\n'
                                        +'{:<48s}'.format("Departure Time: "+self.timedepart[i])),image=(self.combo) ,compound='left',bg='white',font = ("none 11 bold"), height = 63, width = 300, relief=FLAT
                                        ,command=lambda j=i :self.displaytextbox(j))
            historybtn.grid()
            self.buttons.append(historybtn)
        
    def readText(self):
        self.listfiles=[]
        self.namefiles=[]
        self.datepurchase=[]
        self.filenum=[]
        self.timedepart=[]
        self.destination=[]
        self.seats=[]
        
        for dirpath,dirnames, filenames in walk(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject\\Users',self.CurrentUser)):
            for i in range (0,len(filenames)):
                self.listfiles.append(filenames[i])

        if 	self.listfiles ==[]:
            norecord = Label(master, text= "Sorry! No record found!" , font = ('none 12 bold'))
            norecord.place(x=150, y= 100)
            return
            
        for x in range (0,len(self.listfiles)):
            filenamenew=self.listfiles[x].replace(".txt" , "")
            count=filenamenew[-1]
            self.filenum.append(count)
            filenamenew2=filenamenew.replace("_{}_{}".format(self.CurrentUser,count), "")
            date=filenamenew2.replace("_","/")
            self.datepurchase.append(date)
            self.namefiles.append(filenamenew2)
        
        for num in range (0,len(self.listfiles)):
            numseat=0
            for z in range(1,len(self.data)):
                if ((self.data[z]['username']==self.CurrentUser) and (self.data[z]['datepurchased']==self.namefiles[num]) and 
                (self.data[z]['fileno'] == int(self.filenum[num]))) :
                    numseat +=1
                    timedeparture=(self.data[z]['timedepart'])
                    arrival=(self.data[z]['arrival'])
            self.seats.append(numseat)
            self.timedepart.append(timedeparture)
            self.destination.append(arrival)
        for c in range (0, len(self.destination)):
            if self.destination[c] == "Melaka":
                self.destination[c]="MEL"
            if self.destination[c] == "Seremban":
                self.destination[c]="SRM"
            if self.destination[c] == "Butterworth":
                self.destination[c]="BUT."
      

    def backpagebutton(self):
        self.backpagebtn.destroy()
        self.DisplayHistory()
		
    def displaynextpage(self):
        self.buttons[0].destroy()
        self.buttons[1].destroy()
        self.buttons[2].destroy()
        self.buttons[3].destroy()
        self.nextpagebtn.destroy()
        self.backpageIMG=PhotoImage(file='back.png')
        self.backpagebtn=Button(master,image=self.backpageIMG, relief =FLAT  , command=self.backpagebutton)
        self.backpagebtn.place(x=0, y=370)
            
        for i in range(4,len(self.listfiles)): 
            historybtn = Button(self.frames[i-4], text =('{:<29s}'.format("Destination: " + self.destination[i])+ "{:>20s}".format(str(self.seats[i]) +' Seats') +'\n'
                                        +'{:<47s}'.format('Date Purchased: '+self.datepurchase[i])+'\n'
                                        +'{:<48s}'.format("Departure Time: "+self.timedepart[i])),image=(self.combo) ,compound='left',bg='white',font = ("none 11 bold"), height = 63, width = 300, relief=FLAT
                                        ,command=lambda j=i :self.displaytextbox(j))            
            historybtn.grid()
            self.buttons.append(historybtn)     
        
        
        
        
        
    def displaytextbox(self,j):
        global detail
        master.destroy()
        detail=Toplevel()
        detail.resizable (0,0)
        detail.attributes("-toolwindow",1)
        detail.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        w = 500 
        h = 400 
        ws = detail.winfo_screenwidth()
        hs = detail.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        detail.geometry('%dx%d+%d+%d' % (w, h, x, y))
        detail.title("Long Distance Bus Tickets Booking System (Login As: {})".format(self.CurrentUser))        
        text=Text(detail)
        text = Text(detail, relief = SUNKEN, bg="#EEEEEE", highlightcolor='black', font = ("none 15 bold"))
        scroll = Scrollbar(detail, command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.tag_configure('text1', foreground='black',font=("none 15 bold"))
        scroll.pack(side=RIGHT, fill=Y )
        file=open(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject\\Users',self.CurrentUser,"{}".format(self.listfiles[j])), 'r') 
        f_contents = file.read()
        text.insert(END,f_contents,'text1')
        text.place(x=20,y=20,height=320,width=450)
        text.configure(state = DISABLED)
        self.backImg= PhotoImage(file='backtxt.png')
        self.backclosetextbtn=Button(detail,image=self.backImg,command=self.closetextwindow)
        self.backclosetextbtn.place(x=200, y=350)
        detail.mainloop()

    def closetextwindow(self):
        detail.destroy()
        self.__init__()
                
if __name__ == '__main__':
    History=LostTicket()
