from tkinter import *
from tkinter import messagebox
import sys
import json
import string
import Calendar
import TicketDetail

class seatlayout:

    def callbackSeat(self):  #From TicketDetail module calls this Function to redraw back SeatLayout Tk WIndow
        master.bind('<Escape>',self.escbutton)
        master.deiconify()

    def escbutton(self,event):
        self.closebuttonwindow()
        
    def closebuttonwindow (self): #When user Clicks 'X' (Close button) on the window top bar
        answer=messagebox.askokcancel("Warning","Do you want to cancel your booking?",icon="warning")
        if answer == True :
            self.openJsonFile()
            for i in range (0, len(self.data[0]['iclist'])):
                for i in range (0 ,len(self.listseat)):
                    if ((self.listseat[i]['year']==(self.data[-1]['year']))and
                    (self.listseat[i]['month']==(self.data[-1]['month']))and
                    (self.listseat[i]['day']==(self.data[-1]['day']))and
                    (self.listseat[i]['timedepart']==(self.data[-1]['timedepart']))and
                    (self.listseat[i]['depart']==(self.data[-1]['depart']))and
                    (self.listseat[i]['arrival']==(self.data[-1]['arrival']))and
                    (self.data[-1]['fileno']==0) ):
                        if (self.data[-1]['seatno'] != ""):
                            self.listseat[i]['listseatno'].remove(self.data[-1]['seatno'])
                        del self.data[-1]
            self.updateJsonFile()
            exit()
        else:
            pass       
  
    def __init__(self): 
        self.openJsonFile()
        global num
        global master
        self.times_1A= 0
        self.times_1B= 0
        self.times_1C= 0
        self.times_1D= 0
        self.times_2A= 0
        self.times_2B= 0
        self.times_2C= 0
        self.times_2D= 0
        self.times_3A= 0
        self.times_3B= 0
        self.times_3C= 0
        self.times_3D= 0
        self.times_4A= 0
        self.times_4B= 0
        self.times_4C= 0
        self.times_4D= 0
        self.times_5A= 0
        self.times_5B= 0
        self.times_5C= 0
        self.times_5D= 0
        self.times_6A= 0 
        self.times_6B= 0
        self.times_6C= 0
        self.times_6D= 0
        self.times_7A= 0
        self.times_7B= 0
        self.times_7C= 0
        self.times_7D= 0
        self.onetime=0
        master=Toplevel()  #Create Tkinter Window
        # To center the Tkinter window on the screen
        w = 500 
        h = 400 
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        # Window Title
        CurrentUser=self.data[0]['currentuser']
        master.title("Long Distance Bus Tickets Booking System (Login As: {})".format(CurrentUser))
        
        master.resizable (0,0) #Prevent window from being resized
        master.attributes("-toolwindow",1) # Remove Minimize and Maximize Buttons on the window's title bar
        master.protocol('WM_DELETE_WINDOW',self.closebuttonwindow) #Give Command to Close button on the window's title bar
        master.bind('<Escape>',self.escbutton)
        self.selectseatImg= PhotoImage(file='selectseat.png')
        self.label= Label(master, image=self.selectseatImg)
        self.label.grid(row=1)
        self.openJsonFile()
        num=int(self.data[0]['num'])
        if num == 0 :
            backImg=PhotoImage(file='backtxt.png')
            self.backbtn=Button(master, image=backImg , command= lambda k=1 : self.backbutton(master,k))
            self.backbtn.place(x=20,y=350)
        master.iconbitmap('busicon32.ico')
        self.nextImg=PhotoImage(file='nexttxt.png')
        self.createseatlayout(master)    
        master.mainloop()
  
    # Backbutton Function
    def backbutton(self,master,k):
        self.openJsonFile()
        
        number=0
        for x in range (1, len(self.data)):
            if ((self.data[x]['username'] == (self.data[0]['currentuser'])) and 
                (self.data[x]['nric']== (self.data[0]['iclist'][number])) and 
                (self.data[x]['fileno'] == 0)):
                number +=1
                self.data[x]['year'] =""
                self.data[x]['month'] =""
                self.data[x]['day'] =""
                self.data[x]['timedepart'] =""
                self.updateJsonFile()
        master.withdraw()
        if k == 0 :
             messagebox.showinfo("Attention",'Sorry, it is full! Please change to another date OR departtime.', icon="warning")
        Calendar.Calendar.callbackCalendar(self)
                
    #Load Json File         
    def openJsonFile(self):
        with open ('Master.json' , 'r') as json_file:
            self.data = json.load (json_file)
        with open ('CheckListSeat.json' ,'r') as json_file2:
            self.listseat = json.load (json_file2)
        return (self.data , self.listseat)

    #Create Seatlayout  
    def createseatlayout(self,master):
        IcNoImg=PhotoImage(file='icno.png')
        IcNo=Label(master, image = IcNoImg)
        IcNo.image = IcNoImg
        IcNo.place(x=200,y=0)
        if self.data[0]['iclist'][num][0:4] == "null" : 
            displayic="None"
        else:
            displayic=self.data[0]['iclist'][num]
        IcLabel=Label(master, text = "{}".format(displayic) , font=('none 15 bold'))
        IcLabel.grid()
        IcLabel.place(x=260,y=0)
        self.layout= Frame(master, padx=20, pady= 20  ,bd=1 ,relief=RAISED)
        self.layout.grid()
        self.layout.place(x=40, y=40)
        self.bottomlayout = Frame(master)
        self.bottomlayout.grid()
        self.bottomlayout.place( x= 120, y= 285)
        self.seatImg  = PhotoImage(file='seat.png')
        self.driverphoto = PhotoImage(file='driver.png')
        self.gold = PhotoImage(file='gold.png')
        self.red = PhotoImage(file='red.png')
        self.green = PhotoImage(file='green.png')
        self.doorphoto = PhotoImage(file='door.png')
        self.driver= Label ( self.layout , image=self.driverphoto)
        self.door = Label( self.layout , image= self.doorphoto)
        self.empty= Label(self.layout)
        self.empty2= Label(self.layout)
        self.empty.grid(row=2)
        self.empty2.grid(row=6)
        self.colorgold=Label(self.bottomlayout , image=self.gold , relief= SUNKEN)
        self.textgold=Label (self.bottomlayout , text = "Priority Seat" , font =('times 13 bold'))
        self.colorred=Label (self.bottomlayout , image=self.red ,relief = SUNKEN)
        self.textred=Label (self.bottomlayout , text = "Taken" , font =('times 13 bold'))
        self.colorgreen=Label (self.bottomlayout , image=self.green ,relief = SUNKEN)
        self.textgreen=Label (self.bottomlayout , text = "Selected" , font =('times 13 bold'))
        self.A=Label(self.layout , text = "A" , font =('times 13 bold'))
        self.B=Label(self.layout , text = "B" , font =('times 13 bold'))
        self.C=Label(self.layout , text = "C" , font =('times 13 bold'))
        self.D=Label(self.layout , text = "D" , font =('times 13 bold'))
        self.num1=Label(self.layout , text = "1" , font =('times 13 bold'))
        self.num2=Label(self.layout , text = "2" , font =('times 13 bold'))
        self.num3=Label(self.layout , text = "3" , font =('times 13 bold'))
        self.num4=Label(self.layout , text = "4" , font =('times 13 bold'))
        self.num5=Label(self.layout , text = "5" , font =('times 13 bold'))
        self.num6=Label(self.layout , text = "6" , font =('times 13 bold'))
        self.num7=Label(self.layout , text = "7" , font =('times 13 bold'))
        self.button1A=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_1A(master))
        self.button1B=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_1B(master))
        self.button1C=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_1C(master))
        self.button1D=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_1D(master))
        self.button2A=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_2A(master))
        self.button2B=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_2B(master))
        self.button2C=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_2C(master))
        self.button2D=Button(self.layout, image=self.seatImg,state=NORMAL, bg="gold",command= lambda :self.button_2D(master))
        self.button3A=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_3A(master))
        self.button3B=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_3B(master))
        self.button3C=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_3C(master))
        self.button3D=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_3D(master))
        self.button4A=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_4A(master))
        self.button4B=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_4B(master))
        self.button4C=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_4C(master))
        self.button4D=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_4D(master))
        self.button5A=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_5A(master))
        self.button5B=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_5B(master))
        self.button5C=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_5C(master))
        self.button5D=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_5D(master))
        self.button6A=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_6A(master))
        self.button6B=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_6B(master))
        self.button6C=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_6C(master))
        self.button6D=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_6D(master))
        self.button7A=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_7A(master))
        self.button7B=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_7B(master))
        self.button7C=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_7C(master))
        self.button7D=Button(self.layout, image=self.seatImg,state=NORMAL, bg="red" ,command= lambda :self.button_7D(master))
         
        self.button1D.grid(row=0, column= 2)
        self.button2D.grid(row=0, column= 3)
        self.button3D.grid(row=0, column= 4)
        self.button4D.grid(row=0, column= 5)
        self.button5D.grid(row=0, column= 6)
        self.button6D.grid(row=0, column= 7)
        self.button7D.grid(row=0, column= 8)
        self.button1C.grid(row=1, column= 2)
        self.button2C.grid(row=1, column= 3)
        self.button3C.grid(row=1, column= 4)
        self.button4C.grid(row=1, column= 5)
        self.button5C.grid(row=1, column= 6)
        self.button6C.grid(row=1, column= 7)
        self.button7C.grid(row=1, column= 8)
        self.button1B.grid(row=3, column= 2)
        self.button2B.grid(row=3, column= 3)
        self.button3B.grid(row=3, column= 4)
        self.button4B.grid(row=3, column= 5)
        self.button5B.grid(row=3, column= 6)
        self.button6B.grid(row=3, column= 7)
        self.button7B.grid(row=3, column= 8)
        self.button1A.grid(row=4, column= 2)
        self.button2A.grid(row=4, column= 3)
        self.button3A.grid(row=4, column= 4)
        self.button4A.grid(row=4, column= 5)
        self.button5A.grid(row=4, column= 6)
        self.button6A.grid(row=4, column= 7)
        self.button7A.grid(row=4, column= 8)
        self.driver.grid(row=0,column=0)
        self.door.grid(row=4,column=0)
        self.A.grid(row=4,column=1)
        self.B.grid(row=3,column=1)
        self.C.grid(row=1,column=1)
        self.D.grid(row=0,column=1)
        self.num1.grid(row=5,column=2)
        self.num2.grid(row=5,column=3)
        self.num3.grid(row=5,column=4)
        self.num4.grid(row=5,column=5)
        self.num5.grid(row=5,column=6)
        self.num6.grid(row=5,column=7)
        self.num7.grid(row=5,column=8)
        self.colorgold.grid(row=7,column=2)
        self.textgold.grid(row=7,column=3)
        self.colorred.grid(row=7,column=5)
        self.textred.grid(row=7,column=6)
        self.colorgreen.grid(row=7,column=7)
        self.textgreen.grid(row=7,column=8)
        self.checkseatavailable(master)

    def checkseatavailable(self,master) :
        self.button3A.configure( bg='#EEEEEE')
        self.button4A.configure( bg='#EEEEEE')
        self.button5A.configure( bg='#EEEEEE')
        self.button6A.configure( bg='#EEEEEE')
        self.button7A.configure( bg='#EEEEEE')
        self.button3B.configure( bg='#EEEEEE')
        self.button4B.configure( bg='#EEEEEE')
        self.button5B.configure( bg='#EEEEEE')
        self.button6B.configure( bg='#EEEEEE')
        self.button7B.configure( bg='#EEEEEE')
        self.button3C.configure( bg='#EEEEEE')
        self.button4C.configure( bg='#EEEEEE')
        self.button5C.configure( bg='#EEEEEE')
        self.button6C.configure( bg='#EEEEEE')
        self.button7C.configure( bg='#EEEEEE')
        self.button3D.configure( bg='#EEEEEE')
        self.button4D.configure( bg='#EEEEEE')
        self.button5D.configure( bg='#EEEEEE')
        self.button6D.configure( bg='#EEEEEE')
        self.button7D.configure( bg='#EEEEEE')
        # Create a new list into CheckListSeat.json File 
        confirm=0
        for x in range (0,len(self.listseat)):
            if((self.data[0]['year'] == (self.listseat[x]['year'])) and 
            (self.data[0]['month'] == (self.listseat[x]['month'])) and 
            (self.data[0]['day'] == (self.listseat[x]['day'])) and 
            (self.data[0]['depart'] == (self.listseat[x]['depart'])) and
            (self.data[0]['arrival'] == (self.listseat[x]['arrival'])) and 
            (self.data[0]['timedepart'] == (self.listseat[x]['timedepart']))):
                confirm +=1
        if confirm == 0:
            newlistseat={}
            newlistseat['year'] =self.data[0]['year']
            newlistseat['month'] =self.data[0]['month']     
            newlistseat['day'] =self.data[0]['day']
            newlistseat['timedepart'] =self.data[0]['timedepart']
            newlistseat['depart']= self.data[0]['depart']
            newlistseat['arrival']=self.data[0]['arrival']
            newlistseat['listseatno'] =[]
            self.listseat.append(newlistseat)
            self.updateJsonFile()
        
        #Disable the priorty seat
        priority = 1
        for i in range (1, len(self.data)):
            if ((self.data[i]['username'] == (self.data[0]['currentuser'])) and 
                (self.data[i]['nric']== (self.data[0]['iclist'][num])) and
                (self.data[i]['priority'] == 0) and
                (self.data[i]['fileno'] == 0)):
                    priority -= 1
                    self.button1A.configure(state=DISABLED)
                    self.button1B.configure(state=DISABLED)
                    self.button1C.configure(state=DISABLED)
                    self.button1D.configure(state=DISABLED)
                    self.button2A.configure(state=DISABLED)
                    self.button2B.configure(state=DISABLED)
                    self.button2C.configure(state=DISABLED)
                    self.button2D.configure(state=DISABLED)

        # Disable seat buttons that are not available                   
        for x in range (0 ,len(self.listseat)) :
            if ((self.data[0]['year'] == (self.listseat[x]['year'])) and 
            (self.data[0]['month'] == (self.listseat[x]['month'])) and 
            (self.data[0]['day'] == (self.listseat[x]['day'])) and 
            (self.data[0]['depart'] == (self.listseat[x]['depart'])) and 
            (self.data[0]['arrival'] == (self.listseat[x]['arrival'])) and 
            (self.data[0]['timedepart'] == (self.listseat[x]['timedepart']))):
                list= self.listseat[x]['listseatno']
                
                for y in range (0, len(list)):
                    if  (list[y] == "1A"):
                        self.button1A.configure( bg="red",state=DISABLED)
                    if  (list[y] == "2A"):
                        self.button2A.configure( bg="red",state=DISABLED)
                    if  (list[y] == "3A"):
                        self.button3A.configure( bg="red",state=DISABLED)
                    if  (list[y] == "4A"):
                        self.button4A.configure( bg="red",state=DISABLED)
                    if  (list[y] == "5A"):
                        self.button5A.configure( bg="red",state=DISABLED)
                    if  (list[y] == "6A"):
                        self.button6A.configure( bg="red",state=DISABLED)
                    if  (list[y] == "7A"):
                        self.button7A.configure( bg="red",state=DISABLED)
                    if  (list[y] == "1B"):
                        self.button1B.configure( bg="red", state=DISABLED)
                    if  (list[y] == "2B"):
                        self.button2B.configure( bg="red", state=DISABLED)
                    if  (list[y] == "3B"):
                        self.button3B.configure( bg="red",state=DISABLED)
                    if  (list[y] == "4B"):
                        self.button4B.configure( bg="red",state=DISABLED)
                    if  (list[y] == "5B"):
                        self.button5B.configure( bg="red",state=DISABLED)
                    if  (list[y] == "6B"):
                        self.button6B.configure( bg="red",state=DISABLED)
                    if  (list[y] == "7B"):
                        self.button7B.configure( bg="red",state=DISABLED)
                    if  (list[y] == "1C"):
                        self.button1C.configure( bg="red", state=DISABLED)
                    if  (list[y] == "2C"):
                        self.button2C.configure( bg="red", state=DISABLED)
                    if  (list[y] == "3C"):
                        self.button3C.configure( bg="red",state=DISABLED)
                    if  (list[y] == "4C"):
                        self.button4C.configure( bg="red",state=DISABLED)
                    if  (list[y] == "5C"):
                        self.button5C.configure( bg="red",state=DISABLED)
                    if  (list[y] == "6C"):
                        self.button6C.configure( bg="red",state=DISABLED)
                    if  (list[y] == "7C"):
                        self.button7C.configure( bg="red",state=DISABLED)
                    if  (list[y] == "1D"):
                        self.button1D.configure( bg="red", state=DISABLED)
                    if  (list[y] == "2D"):
                        self.button2D.configure( bg="red", state=DISABLED)
                    if  (list[y] == "3D"):
                        self.button3D.configure( bg="red",state=DISABLED)
                    if  (list[y] == "4D"):
                        self.button4D.configure( bg="red",state=DISABLED)
                    if  (list[y] == "5D"):
                        self.button5D.configure( bg="red",state=DISABLED)
                    if  (list[y] == "6D"):
                        self.button6D.configure( bg="red",state=DISABLED)
                    if  (list[y] == "7D"):
                        self.button7D.configure( bg="red",state=DISABLED)
        self.forcepriority = 0
        normalseatlist=["3A","3B","3C","3D","4A","4B","4C","4D","5A","5B","5C","5D","6A","6B","6C","6D","7A","7B","7C","7D"]
        disabled=0
        for c in range (0,len(list)):
            for b in range (0, len(normalseatlist)):
                if list[c]==normalseatlist[b] :
                    disabled +=1
        priorityseatlist=["1A","1B","1C","1D","2A","2B","2C","2D"]
        prioritydisabled=0
        for c in range (0,len(list)):
            for b in range (0, len( priorityseatlist)):
                if list[c]== priorityseatlist[b] :
                    prioritydisabled +=1
        prioritynum=0
        prioritylist=self.data[0]['prioritylist']
        for j in range (0,len(prioritylist)):
            if prioritylist[j] == 1 :
                    prioritynum +=1        
        if num == 0:                
        # Check whether the bus seat are Full or Not &
		#force to buy priorty seat if number of seats are limited
            if (list == ["1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D","4A","4B","4C","4D","5A","5B","5C","5D","6A","6B","6C","6D","7A","7B","7C","7D"]):     
                k = 0
                self.backbutton(master,k)
                return
            seatavailable= 28-disabled-prioritydisabled
            self.data[0]['seatavailable']=seatavailable
            self.updateJsonFile()
            if prioritynum > 0 :
                if seatavailable < len(self.data[0]['iclist']) :
                    k = 0
                    self.backbutton(master,k) 
                    return
            if prioritynum == 0 :
                if ((disabled == 20) or ((20-disabled) < len(self.data[0]['iclist']))):     
                    k = 0
                    self.backbutton(master,k)
                    return
        for t in range (1,len(self.data)):
            if  ((self.data[0]['iclist'][num] == self.data[t]['nric']) and 
                (self.data[0]['currentuser']==self.data[t]['username']) and
                (self.data[t]['fileno'] == 0) and 
                (prioritydisabled == 8)):
                    self.forcepriority=0
                    break
            if  ((self.data[0]['iclist'][num] == self.data[t]['nric']) and 
                (self.data[0]['currentuser']==self.data[t]['username']) and
                (self.data[t]['priority'] == 1) and
                (self.data[t]['fileno'] == 0) and 
                (self.data[0]['seatavailable'] == len(self.data[0]['iclist']))):
                    self.forcepriority=1
                    break
                
    def button_1A(self,master):
        seatnum="1A"

        
        if (float(self.times_1A % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_1A += 1
            self.onetime -=1
            self.button1A.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_1A += 1
                self.onetime +=1
                self.button1A.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_2A(self,master):
        seatnum="2A"

            
        if (float(self.times_2A % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_2A += 1
            self.onetime -=1
            self.button2A.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_2A += 1
                self.onetime +=1
                self.button2A.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
            
    def button_3A(self,master):
        seatnum="3A"  
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        if (float(self.times_3A % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_3A += 1
            self.onetime -=1
            self.button3A.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_3A += 1
                self.onetime +=1
                self.button3A.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")  
    
    def button_4A(self,master):
        seatnum="4A"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        if (float(self.times_4A % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_4A += 1
            self.onetime -=1
            self.button4A.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_4A += 1
                self.onetime +=1
                self.button4A.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_5A(self,master):
        seatnum="5A"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
                    
        if (float(self.times_5A % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_5A += 1
            self.onetime -=1
            self.button5A.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_5A += 1
                self.onetime +=1
                self.button5A.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
                
    def button_6A(self,master):
        seatnum="6A"    
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
                    
        if (float(self.times_6A % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_6A += 1
            self.onetime -=1
            self.button6A.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_6A += 1
                self.onetime +=1
                self.button6A.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
                
    def button_7A(self,master):
        seatnum="7A"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
             
        if (float(self.times_7A % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_7A += 1
            self.onetime -=1
            self.button7A.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_7A += 1
                self.onetime +=1
                self.button7A.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_1B(self,master):
        seatnum="1B"

            
        if (float(self.times_1B % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_1B += 1
            self.onetime -=1
            self.button1B.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_1B += 1
                self.onetime +=1
                self.button1B.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_2B(self,master):
        seatnum="2B"

            
        if (float(self.times_2B % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_2B += 1
            self.onetime -=1
            self.button2B.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_2B += 1
                self.onetime +=1
                self.button2B.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_3B(self,master):
        seatnum="3B"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        if (float(self.times_3B % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_3B += 1
            self.onetime -=1
            self.button3B.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_3B += 1
                self.onetime +=1
                self.button3B.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_4B(self,master):
        seatnum="4B"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        if (float(self.times_4B % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_4B += 1
            self.onetime -=1
            self.button4B.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_4B += 1
                self.onetime +=1
                self.button4B.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_5B(self,master):
        seatnum="5B"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return

        if (float(self.times_5B % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_5B += 1
            self.onetime -=1
            self.button5B.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_5B += 1
                self.onetime +=1
                self.button5B.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")

    def button_6B(self,master):
        seatnum="6B"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return

        if (float(self.times_6B % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_6B += 1
            self.onetime -=1
            self.button6B.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_6B += 1
                self.onetime +=1
                self.button6B.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_7B(self,master):
        seatnum="7B"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return

        if (float(self.times_7B % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_7B += 1
            self.onetime -=1
            self.button7B.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_7B += 1
                self.onetime +=1
                self.button7B.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
                
    def button_1C(self,master):
        seatnum="1C"
        
        if (float(self.times_1C % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_1C += 1
            self.onetime -=1
            self.button1C.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_1C += 1
                self.onetime +=1
                self.button1C.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_2C(self,master):
        seatnum="2C"

        if (float(self.times_2C % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_2C += 1
            self.onetime -=1
            self.button2C.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_2C += 1
                self.onetime +=1
                self.button2C.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_3C(self,master):
        seatnum="3C"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        if (float(self.times_3C % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_3C += 1
            self.onetime -=1
            self.button3C.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_3C += 1
                self.onetime +=1
                self.button3C.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_4C(self,master):
        seatnum="4C"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
              
        if (float(self.times_4C % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_4C += 1
            self.onetime -=1
            self.button4C.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_4C += 1
                self.onetime +=1
                self.button4C.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_5C(self,master):
        seatnum="5C"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        
        if (float(self.times_5C % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_5C += 1
            self.onetime -=1
            self.button5C.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_5C += 1
                self.onetime +=1
                self.button5C.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_6C(self,master):
        seatnum="6C"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        
        if (float(self.times_6C % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_6C += 1
            self.onetime -=1
            self.button6C.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_6C += 1
                self.onetime +=1
                self.button6C.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_7C(self,master):
        seatnum="7C"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        
        if (float(self.times_7C % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_7C += 1
            self.onetime -=1
            self.button7C.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_7C += 1
                self.onetime +=1
                self.button7C.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")

    def button_1D(self,master):
        seatnum="1D"
        if (float(self.times_1D % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_1D += 1
            self.onetime -=1
            self.button1D.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_1D += 1
                self.onetime +=1
                self.button1D.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_2D(self,master):
        seatnum="2D"
            
        if (float(self.times_2D % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_2D += 1
            self.onetime -=1
            self.button2D.configure ( bg='gold')
            pass
        else:
            if self.onetime == 0:
                self.times_2D += 1
                self.onetime +=1
                self.button2D.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_3D(self,master):
        seatnum="3D"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        if (float(self.times_3D % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_3D += 1
            self.onetime -=1
            self.button3D.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_3D += 1
                self.onetime +=1
                self.button3D.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_4D(self,master):
        seatnum="4D"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            

        if (float(self.times_4D % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_4D += 1
            self.onetime -=1
            self.button4D.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_4D += 1
                self.onetime +=1
                self.button4D.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_5D(self,master):
        seatnum="5D"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return

        if (float(self.times_5D % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_5D += 1
            self.onetime -=1
            self.button5D.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_5D += 1
                self.onetime +=1
                self.button5D.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_6D(self,master):
        seatnum="6D"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            
        
        if (float(self.times_6D % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_6D += 1
            self.onetime -=1
            self.button6D.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_6D += 1
                self.onetime +=1
                self.button6D.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
    
    def button_7D(self,master):
        seatnum="7D"
        if self.forcepriority == 1:
            messagebox.showinfo("Attention",'You must choose priority seat!'+'\n'+ 'Because no more available seat for your friend(s)/family member(s)', icon="warning")
            return
            

        if (float(self.times_7D % 2) != 0 ) and (self.onetime == 1):
            self.nextbtn.destroy()
            self.times_7D += 1
            self.onetime -=1
            self.button7D.configure ( bg='#EEEEEE')
            pass
        else:
            if self.onetime == 0:
                self.times_7D += 1
                self.onetime +=1
                self.button7D.configure( bg="green")
                self.nextbtn=Button(master, image=self.nextImg, command = lambda : self.confirmbutton(master,seatnum))
                self.nextbtn.grid()
                self.nextbtn.place( x = 400 , y= 350) 
            else:
                messagebox.showinfo("Attention",'You can only select 1 seat!!', icon="warning")
                
 # Save the seat number into both Json files  
    def confirmbutton (self,master,seatnum) : 
        self.openJsonFile()
        for i in range (1, len(self.data)):
            if ((self.data[i]['username'] == (self.data[0]['currentuser'])) and 
                (self.data[i]['nric'] == (self.data[0]['iclist'][num])) and 
                (self.data[i]['fileno'] == 0)):               
                self.data[i]['seatno'] = seatnum
        for x in range (0, len(self.listseat)):
            if ((self.data[0]['year'] == (self.listseat[x]['year'])) and 
            (self.data[0]['month'] ==  (self.listseat[x]['month'])) and 
            (self.data[0]['day'] == (self.listseat[x]['day'])) and 
            (self.data[0]['timedepart'] == (self.listseat[x]['timedepart'])) and
            (self.data[0]['depart'] == (self.listseat[x]['depart'])) and 
            (self.data[0]['arrival'] == (self.listseat[x]['arrival']))):
                self.listseat[x]['listseatno'].append(seatnum)
        # sort the seatnumber in 'listseano' list
        for y in range (0, len(self.listseat)):
            self.listseat[y]['listseatno'].sort()
                    
        self.updateJsonFile()
        master.withdraw()
        master.unbind('<Escape>')
        TicketDetail.bus_tickets()
               
    def updateJsonFile(self):        
        with open ('Master.json' ,'w') as json_file:
            json.dump(self.data,json_file, indent=4)
        with open ('CheckListSeat.json' ,'w') as json_file2:
            json.dump(self.listseat,json_file2, indent=4)
        
if __name__ == '__main__':
    Main = seatlayout()


