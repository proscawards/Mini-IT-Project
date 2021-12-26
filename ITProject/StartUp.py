from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import copy
import json
import history
import collections
import calendar
import os
     
class startUp():
    def escbutton(self,event):
        self.closebuttonwindow()
		
    def closebuttonwindow (self):
        if self.z == 1:
            pass
        answer=messagebox.askokcancel("Warning","Do you want to cancel your booking?",icon="warning")
        if answer == True :
            exit()
        else:
            pass  
    
    def donothing(self):
        pass
    
    def __init__(self):
        self.z=0
        self.openJsonFile()
        self.openWindow1()
            

    def openJsonFile(self):
        with open('Master.json') as json_file:
            self.data=json.load(json_file)
        return self.data

    def openWindow1(self):
        self.CurrentUser=self.data[0]['currentuser']
        global master
        master= Tk()
        w = 500 
        h = 400 
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        master.title("Long Distance Bus Tickets Booking System (Login As: {})".format(self.CurrentUser))
        master.resizable (0,0)
        master.attributes("-toolwindow",1)
        master.protocol('WM_DELETE_WINDOW',self.donothing)
        master.bind('<Return>',self.entertowindow2) 
        welcomeImg=PhotoImage(file='welcome.png')
        welcome = Label(master, image=welcomeImg)
        welcome.place(x=200,y=70)
        text1 = Label(master, text="Please enter the number of ticket you would like to purchase.")
        text1.config(font=("Calibri", 13))
        text1.place(x=30,y=130)
        self.numoftickets = Entry(master)
        self.numoftickets.place(x=180,y=170)
        self.nextbuttonImg=PhotoImage(file='nexttxt.png')
        textticket=Label(master, text="Ticket Purchased:",font='none 9 bold')
        textticket.place(x=10,y=330)
        ViewImg=PhotoImage(file='view.png')
        self.history=Button(master, image=ViewImg , command= lambda: history.LostTicket())
        self.history.place(x=20,y=350)
        self.nextbtn = Button(master, image=self.nextbuttonImg, command= lambda: self.number(master))
        self.nextbtn.place(x=400,y=350)
        logoutimg = PhotoImage(file = 'logout.png')
        logoutButton= Button(master, image = logoutimg, command = lambda : exit()) 
        logoutButton.image = logoutimg
        logoutButton.place(x= 400, y= 10)
        master.mainloop()
        
    def entertowindow2(self,event):  
        self.number(master)
        
    def number(self,master):  #check if the numberoftickets is valid
        while True:
            try:
                self.numberoftickets = int(self.numoftickets.get())
                if self.numberoftickets >= 11:
                    messagebox.showinfo("Opps","The value entered exceed 10, please try again.")
                    return
                if 0 < self.numberoftickets <= 10:
                    self.nextbtn.destroy()
                    master.unbind('<Escape>')
                    master.unbind('<Return>')
                    master.withdraw()
                    
                    self.openWindow2()
                    return self.numberoftickets
                else: 
                    messagebox.showinfo("Opps","The value entered is invalid, please try again.")
                    return
            except ValueError:
                messagebox.showinfo("Opps","The value entered must be a number, please try again.")
                return
    
    def openWindow2(self):
        self.z += 1
        global window2
        window2 = Toplevel()
        w = 500 
        h = 400 
        ws = window2.winfo_screenwidth()
        hs = window2.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window2.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window2.title("Long Distance Bus Tickets Booking System (Login As: {})".format(self.CurrentUser))
        window2.resizable (0,0)
        window2.attributes("-toolwindow",1)
        window2.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        window2.bind('<Return>',self.entertowindow3)
        window2.bind('<Escape>',self.escbutton)    
        text2 = Label(window2, text="Please enter the IC of the passengers.")
        text2.config(font=("Times",12,"bold"))
        text2.place(x=110,y=25)
        self.NricEntry(window2)     
        self.nextbtn = Button(window2, image=self.nextbuttonImg, command= lambda: self.plusNricEntry(window2))
        self.nextbtn.place(x=400,y=350)
        window2.mainloop()
        
    def entertowindow3(self,event):  
        self.plusNricEntry(window2)
        
    def NricEntry(self, window2): #Generate entry box for nric input
        self.ic = []
        self.photo=PhotoImage(file="minus2.png")
        self.photo1=PhotoImage(file="plus.png")
        self.minusButton = Button(window2, image=self.photo, command= lambda: self.minusEntry(window2))
        self.plusButton = Button(window2, image=self.photo1, command= lambda: self.plusEntry(window2))
        self.plusButton.place(x=430,y=165)
        self.minusButton.place(x=430, y=195)
        plusText = Label(window2, text="Add entry:")
        minusText = Label(window2, text="Minus entry:")
        plusText.config(font=("Calibri", 12))
        minusText.config(font=("Calibri", 12))
        plusText.place(x=350,y=165)
        minusText.place(x=340,y=195)
        self.entry1 = Entry(window2)
        self.entry2 = Entry(window2)
        self.entry3 = Entry(window2)
        self.entry4 = Entry(window2)
        self.entry5 = Entry(window2)
        self.entry6 = Entry(window2)
        self.entry7 = Entry(window2)
        self.entry8 = Entry(window2)
        self.entry9 = Entry(window2)
        self.entry10 = Entry(window2)
        
        if self.numberoftickets == 1:
            self.entry1.place(x=180,y=50)
            
        if self.numberoftickets == 2:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)

        if self.numberoftickets == 3:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
        
        if self.numberoftickets == 4:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
            self.entry4.place(x=180,y=140)
        
        if self.numberoftickets == 5:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
            self.entry4.place(x=180,y=140)
            self.entry5.place(x=180,y=170)
        
        if self.numberoftickets == 6:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
            self.entry4.place(x=180,y=140)
            self.entry5.place(x=180,y=170)
            self.entry6.place(x=180,y=200)
        
        if self.numberoftickets == 7:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
            self.entry4.place(x=180,y=140)
            self.entry5.place(x=180,y=170)
            self.entry6.place(x=180,y=200)
            self.entry7.place(x=180,y=230)
        
        if self.numberoftickets == 8:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
            self.entry4.place(x=180,y=140)
            self.entry5.place(x=180,y=170)
            self.entry6.place(x=180,y=200)
            self.entry7.place(x=180,y=230)
            self.entry8.place(x=180,y=260)
        
        if self.numberoftickets == 9:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
            self.entry4.place(x=180,y=140)
            self.entry5.place(x=180,y=170)
            self.entry6.place(x=180,y=200)
            self.entry7.place(x=180,y=230)
            self.entry8.place(x=180,y=260)
            self.entry9.place(x=180,y=290)
        
        if self.numberoftickets == 10:
            self.entry1.place(x=180,y=50)
            self.entry2.place(x=180,y=80)
            self.entry3.place(x=180,y=110)
            self.entry4.place(x=180,y=140)
            self.entry5.place(x=180,y=170)
            self.entry6.place(x=180,y=200)
            self.entry7.place(x=180,y=230)
            self.entry8.place(x=180,y=260)
            self.entry9.place(x=180,y=290)
            self.entry10.place(x=180,y=320)
        
    def minusEntry (self, window2): #minus entrybox
        if self.numberoftickets > 10:
            self.numberoftickets == 10
        if 1 < self.numberoftickets < 11:
            self.numberoftickets = self.numberoftickets - 1
        if self.numberoftickets == 1:
            self.entry2.destroy()
        if self.numberoftickets == 2:
            self.entry3.destroy()
        if self.numberoftickets == 3:
            self.entry4.destroy()
        if self.numberoftickets == 4:
            self.entry5.destroy()
        if self.numberoftickets == 5:
            self.entry6.destroy()
        if self.numberoftickets == 6:
            self.entry7.destroy()
        if self.numberoftickets == 7:
            self.entry8.destroy()
        if self.numberoftickets == 8:
            self.entry9.destroy()
        if self.numberoftickets == 9:
            self.entry10.destroy()
        if self.numberoftickets == 10:
            self.entry10.destroy()
        
    def plusEntry(self, window2): #add entrybox
        if self.numberoftickets > 10:
            self.numberoftickets == 10
        if self.numberoftickets == 1:
            self.entry2 = Entry(window2)
            self.entry2.place(x=180,y=80)
        if self.numberoftickets == 2:
            self.entry3 = Entry(window2)
            self.entry3.place(x=180,y=110)
        if self.numberoftickets == 3:
            self.entry4 = Entry(window2)
            self.entry4.place(x=180,y=140)
        if self.numberoftickets == 4:
            self.entry5 = Entry(window2)
            self.entry5.place(x=180,y=170)
        if self.numberoftickets == 5:
            self.entry6 = Entry(window2)
            self.entry6.place(x=180,y=200)
        if self.numberoftickets == 6:
            self.entry7 = Entry(window2)
            self.entry7.place(x=180,y=230)
        if self.numberoftickets == 7:
            self.entry8 = Entry(window2)
            self.entry8.place(x=180,y=260)
        if self.numberoftickets == 8:
            self.entry9 = Entry(window2)
            self.entry9.place(x=180,y=290)
        if self.numberoftickets == 9:
            self.entry10 = Entry(window2)
            self.entry10.place(x=180,y=320)
        if 0 < self.numberoftickets < 10:
            self.numberoftickets = self.numberoftickets + 1
        
        

    def plusNricEntry(self,window2): #append all the values from entrybox to list
        if self.numberoftickets == 1:
            self.ic.append(self.entry1.get())
        if self.numberoftickets == 2:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
        if self.numberoftickets == 3:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
        if self.numberoftickets == 4:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
            self.ic.append(self.entry4.get())
        if self.numberoftickets == 5:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
            self.ic.append(self.entry4.get())
            self.ic.append(self.entry5.get())
        if self.numberoftickets == 6:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
            self.ic.append(self.entry4.get())
            self.ic.append(self.entry5.get())
            self.ic.append(self.entry6.get())
        if self.numberoftickets == 7:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
            self.ic.append(self.entry4.get())
            self.ic.append(self.entry5.get())
            self.ic.append(self.entry6.get())
            self.ic.append(self.entry7.get())
        if self.numberoftickets == 8:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
            self.ic.append(self.entry4.get())
            self.ic.append(self.entry5.get())
            self.ic.append(self.entry6.get())
            self.ic.append(self.entry7.get())
            self.ic.append(self.entry8.get())
        if self.numberoftickets == 9:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
            self.ic.append(self.entry4.get())
            self.ic.append(self.entry5.get())
            self.ic.append(self.entry6.get())
            self.ic.append(self.entry7.get())
            self.ic.append(self.entry8.get())
            self.ic.append(self.entry9.get())
        if self.numberoftickets == 10:
            self.ic.append(self.entry1.get())
            self.ic.append(self.entry2.get())
            self.ic.append(self.entry3.get())
            self.ic.append(self.entry4.get())
            self.ic.append(self.entry5.get())
            self.ic.append(self.entry6.get())
            self.ic.append(self.entry7.get())
            self.ic.append(self.entry8.get())
            self.ic.append(self.entry9.get())
            self.ic.append(self.entry10.get())
        self.checkNRIC(window2)
        
  


    def checkNRIC(self, window2): #check the ic
        blanknum = 0
        times=1
        window2.iconify()
        self.newic = copy.copy(self.ic)
        self.monthlist = []
        self.daylist = []
        self.yearlist = []
        self.iclist = []
        
    
        while "" in self.newic: #remove blank input
            self.newic.remove("")
            
        for s in range(0, len(self.newic)): #check for duplicate input
            if len(set(self.newic)) != len(self.newic):
                messagebox.showinfo("Opps!","There are duplicate IC entered!")
                self.ic = []
                self.newic = []
                window2.deiconify()
                return
            
        for i in range (0, len(self.ic)): #add 1 to blanknum if there's blank entrybox
            if self.ic[i]== "" :
                blanknum+=1
                
        for x in range (0, len(self.ic)): #check if the ic is able to change to integer
            if self.ic[x] != "":
                try:
                    check1 = int(self.ic[x])
                except ValueError:
                    messagebox.showinfo("Opps","The IC entered must be digits!")
                    window2.deiconify()
                    self.ic = []
                    self.newic = []
                    return
                
        for c in range(0,len(self.ic)): #check ic length
            if self.ic[c] == "":
                continue
            if len(self.ic[c]) != 12:
                messagebox.showinfo("Opps","The IC entered is invalid!")
                self.newic = []
                self.ic = []
                window2.deiconify()
                return
            
        if blanknum > 0 : #ask for confirmation for the blank inputs
            if blanknum > 1 :
                verb = "are"
            if blanknum == 1 :   
                verb = "is"
            confirmation = messagebox.askokcancel("Oops!"," {} entry {} blank, do you wish to continue? (Ticket without inserting IC will not getting priority seat!)".format(blanknum,verb))

            if confirmation == True:
                for i in range (0, len(self.ic)):
                    if self.ic[i]== "" :
                        self.ic[i] = "null_{}".format(times)
                        times+=1
            if confirmation == False:
                window2.deiconify()
                self.ic=[]
                self.newic = []
                return


        for f in range(0,len(self.ic)): #append month value from ic
            self.monthlist.append(self.ic[f][2] + self.ic[f][3])
            
        for h in range(0, len(self.ic)): #append day value from ic
            if self.ic[h][0:4]=="null":
                self.daylist.append(1)
            else:   
                self.daylist.append(self.ic[h][4] + self.ic[h][5])
                
        for g in range (0, len(self.monthlist)): #check if the days entered match the month entered
            if str(self.monthlist[g]) == "ll":
                continue
            elif int(self.monthlist[g]) >= 13 or int(self.monthlist[g]) <= 0:
                messagebox.showinfo("Opps","The IC entered is invalid!")
                self.monthlist = []
                self.newic = []
                self.ic = []
                window2.deiconify()
                return
            for j in range(0, len(self.daylist)):
                if int(self.monthlist[g]) == 1 or int(self.monthlist[g]) == 3 or int(self.monthlist[g]) == 5 or int(self.monthlist[g]) == 7 or int(self.monthlist[g]) == 8 or int(self.monthlist[g]) == 10 or int(self.monthlist[g]) == 12:
                    if int(self.daylist[j]) >= 32 or int(self.daylist[j]) <= 0:
                        messagebox.showinfo("Opps","The IC entered is invalid!")
                        self.daylist = []
                        self.monthlist = []
                        self.newic = []
                        self.ic = []
                        window2.deiconify()
                        return
                else:
                    if int(self.daylist[j]) >= 31 or int(self.daylist[j]) <= 0:
                        messagebox.showinfo("Opps","The IC entered is invalid!")
                        self.daylist = []
                        self.monthlist = []
                        self.newic = []
                        self.ic = []
                        window2.deiconify()
                        return
            
        for b in range(0,len(self.ic)): #get year digits from ic
            self.iclist.append(self.ic[b][0] + self.ic[b][1])
            
        for p in range(0, len(self.iclist)): #calculate the yearborn from ic
            if str(self.iclist[p]) == "nu":
                self.yearlist.append("nu")
            elif int(self.iclist[p]) >= 18:
                self.yearlist.append(1900 + int(self.iclist[p]))
            else:
                self.yearlist.append(2000 + int(self.iclist[p]))
                
        for r in range(0, len(self.yearlist)):      #check for leap year  
            if str(self.yearlist[r]) == "nu":
                continue
            if calendar.isleap(self.yearlist[r]) == True:
                if int(self.monthlist[r]) == 2:
                    if 1 <= int(self.daylist[r]) < 30:
                        continue
                    if int(self.daylist[r]) >= 30:
                        messagebox.showinfo("Opps","The IC entered is invalid!")
                        self.daylist = []
                        self.monthlist = []
                        self.yearlist = []
                        self.iclist = []
                        self.newic = []
                        self.ic = []
                        window2.deiconify()
                        return
                else:
                    continue
            else:
                if int(self.monthlist[r]) == 2:
                    if 1 <= int(self.daylist[r]) <= 28:
                        continue
                    if int(self.daylist[r]) > 28:
                        messagebox.showinfo("Opps","The IC entered is invalid!")
                        self.daylist = []
                        self.monthlist = []
                        self.yearlist = []
                        self.iclist = []
                        self.newic = []
                        self.ic = []
                        window2.deiconify()
                        return
        self.checkPriority(window2)
        
        
    def checkPriority(self, window2): #check if the passenger is eligible for priority seats
        self.age=[]
        self.priority=[]
        for e in range(0, len(self.yearlist)):
            if str(self.yearlist[e]) == "nu":
                self.age.append(0)
            else:
                self.age.append(2018 - int(self.yearlist[e]))
        
        for z in range(0, len(self.age)):
            if (self.age[z]) >=55:
                self.priority.append(1)
            else:
                self.priority.append(0)
        self.nextbtn.destroy()
        self.openWindow3(window2)


    def openWindow3(self, window2):
        window2.destroy()
        global window3
        window3 = Toplevel()
        window3.title("Long Distance Bus Tickets Booking System (Login As: {})".format(self.CurrentUser))
        window3.resizable (0,0)
        window3.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        window3.attributes("-toolwindow",1)
        w = 500 
        h = 400 
        ws = window3.winfo_screenwidth()
        hs = window3.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window3.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window3.bind('<Return>',self.enterclicked) ########NEW
        window3.bind('<Escape>',self.escbutton)    #########NEW
        text3 = Label(window3, text="Please select departure and arrival city for all the passengers.")
        text3.config(font=("Times", 13, "bold"))
        text3.place(x=20,y=50)
        self.nextbuttonImg2=PhotoImage(file='nexttxt.png')
        self.nextbtn =Button(window3, image=self.nextbuttonImg2, command= lambda: self.confirmLocation())
        self.nextbtn.place(x=400,y=350)

        text4 = Label(window3, text="Please select your departure city.")
        text4.config(font=("Calibri",13))
        text4.place(x=140,y=90)
        text5 = Label(window3, text="Departure:")
        text5.config(font=("Calibri",12))
        text5.place(x=140,y=130)
        self.selection1 = Combobox(window3, state="readonly")
        self.selection1['values'] = ('Butterworth','Melaka','Seremban')
        self.selection1.place(x=220,y=130)
        
        text6 = Label(window3, text="Please select your arrival city.")
        text6.config(font=("Calibri",13))
        text6.place(x=140,y=210)
        text7 = Label(window3, text="Arrival:")
        text7.config(font=("Calibri",12))
        text7.place(x=150,y=260)
        self.selection2 = Combobox(window3, state="readonly")
        self.selection2['values'] = ('Butterworth','Melaka','Seremban')
        self.selection2.place(x=210,y=260)
        window3.mainloop()
        
    def enterclicked(self,event):  
        self.confirmLocation()  

    def confirmLocation(self): #check the location chosen
        self.depart =[]
        self.arrival =[]
        if (self.selection1.get()) == "" or (self.selection2.get()) == "":
            messagebox.showinfo("Location","The departure city or arrival city cannot be blank!")
            return
        if (self.selection1.get()) != (self.selection2.get()):
            messagebox.showinfo("Location","The departure city and arrival city has been confirmed!")
        else:
            messagebox.showinfo("Location","The departure city and arrival city cannot be the same!")
            return
        self.depart = self.selection1.get()
        self.arrival = self.selection2.get()
        self.savePassengerToFile()
        
             
                
    def savePassengerToFile(self):
        for k in range (0,len(self.ic)):    #save the data in lower part of master.json file
            passengerdata = {}
            passengerdata['username'] = self.CurrentUser
            passengerdata['datepurchased']=""
            passengerdata['nric' ] = self.ic[k]
            passengerdata['age'] = self.age[k]
            passengerdata['depart'] = self.depart
            passengerdata['arrival'] = self.arrival
            passengerdata['priority'] = self.priority[k]
            passengerdata['year'] =""
            passengerdata['month'] = ""
            passengerdata['day'] = ""
            passengerdata['timedepart'] = ""   
            passengerdata['seatno'] = ""
            passengerdata["price"]= 0
            passengerdata["fileno"]=0
            self.data.append(passengerdata)
            
        self.data[0]['iclist']=self.ic  #save the data in upper part of master.json file
        self.data[0]['num']=0
        self.data[0]['depart']= self.depart
        self.data[0]['arrival']=self.arrival
        self.data[0]['prioritylist']=self.priority
        self.updateJsonFile()
        window3.destroy()
        master.destroy()

    def updateJsonFile(self): #save the data to file
        with open ('Master.json', 'w') as json_file:
            json.dump (self.data, json_file, indent=4)             

if __name__=='__main__':
    abc=startUp()

