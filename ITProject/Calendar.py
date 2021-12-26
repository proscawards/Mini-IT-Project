from tkinter import *
from tkinter import ttk
import sys
import time
import string
import calendar
import datetime
import json
import SelectSeat
from tkinter import messagebox
from datetime import date
if sys.version[0] == '2':
    import Tkinter as tk
else:
    import tkinter as tk


    

class Calendar:

    def __init__(self):
        global root
        root = Tk()
        self.data = {}
        self.openJsonFile()
        self.CurrentUser=self.filedata[0]['currentuser']      
        root.title("Long Distance Bus Tickets Booking System (Login As: {})".format(self.CurrentUser))
        root.resizable(0,0)
        root.attributes("-toolwindow",1)
        root.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        root.bind('<Escape>',self.escbutton)
        # Canvas Size
        w = 500
        h = 400
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        # calculate position x and y coordinates
        x = (sw/2) - (w/2)
        y = (sh/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.dateImg=PhotoImage(file='datetxt.png')
        label=Label(root, image=self.dateImg)
        label.grid(row=1)
        now = datetime.datetime.now()
        self.cfm = 0
        self.values = self.data
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.daybutton = []
        self.day_selected = now.day
        self.month_selected = self.month
        self.year_selected = self.year
        self.openJsonFile()        
        self.outlineframe_calendar()
        self.calendarselection(self.year, self.month)
        self.departtimecombobox()
        self.clocktitle()
        self.tdydate()
        self.clocktimer()
        root.mainloop()
    def escbutton(self,event):
        self.closebuttonwindow()
		
    def closebuttonwindow (self):
        answer=messagebox.askokcancel("Warning","Do you want to cancel your booking?Calendar",icon="warning")
        if answer == True :
            self.openJsonFile()
            for i in range (0, len(self.filedata[0]['iclist'])):
                del self.filedata[-1]
            self.updateJsonFile()
            exit()
        else:
            pass     

    def openJsonFile(self):
        with open('Master.json', 'r') as json_file:
            self.filedata = json.load (json_file)
        return self.filedata
        
    def callbackCalendar(self):
        root.deiconify()
        root.bind('<Escape>',self.escbutton)


    # Digital Clock Display :O (Upper Left)
    def clocktitle(self):
        frame2 = Frame(root , padx = 10, pady = 10, bd=1, relief = RAISED)
        frame2.place(x = 10, y = 35)
        timetitle = Label(frame2, text = 'Current Time')
        timetitle.grid(row = 0, column = 1)
        self.clock = Label(frame2, font = ("times 20 bold"))
        self.clock.grid(row = 1, column = 1)
        time1 = ''
        self.selectedtime = StringVar()
        self.selectedtime.set("Time Selected: ")        

    def outlineframe_calendar(self):
        outlinef = Frame(root, bd = 1, height = 280, width= 337, relief = RAISED)
        outlinef.place(x = 149, y = 34)
    
    #Time Depart Combobox
    def clickedconfirm(self, *timedepart):
        self.cfm += 1
        if self.timedepart.get() == '08:00AM (N.A.)':
                messagebox.showinfo("Sorry, my dear customer...","This ride(08:00AM) is not available. Please choose other available ride(s).",icon='warning')
                self.cfm = 0
                self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
                self.selectedtime.set("Time Selected:" + "                                           ")
        if self.timedepart.get() == '12:00PM (N.A.)':
                messagebox.showinfo("Sorry, my dear customer...","This ride(12:00AM) is not available. Please choose other available ride(s).",icon='warning')
                self.cfm = 0
                self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
                self.selectedtime.set("Time Selected:" + "                                           ")
        if self.timedepart.get() == '08:00AM' or self.timedepart.get() == '12:00PM' or self.timedepart.get() == '04:00PM':
                self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
                self.selectedtime.set("Time Selected:" + "  " + self.timedepart.get())

    # Today's Date Display
    def tdydate(self):
        todaydate = date.today()
        frame1 = Frame(root , padx = 10, pady = 10, bd=1, relief = RAISED)
        frame1.place(x = 10, y = 130)
        datetitle = Label(frame1, text = "Today's Date", width = 14)
        datetitle.grid(row = 0, column = 1)
        currentdate = Label(frame1, text = todaydate, font = ("times 16 bold"))
        currentdate.grid(row = 1, column = 1)

    def clocktimer(self, *time1):
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            self.clock.config(text=time2)
        self.clock.after(1000, self.clocktimer)    
        self.refreshcombobox()
        
    def clear_calendar(self):
        for w in self.daybutton[:]:
            w.grid_forget()
            w.destroy()
            self.daybutton.remove(w)
     
    def go_prevbtn(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        self.clear_calendar()
        self.calendarselection(self.year, self.month)
 
    def go_nextbtn(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.month = 1
            self.year += 1
        self.clear_calendar()
        self.calendarselection(self.year, self.month)
         
    def selection(self, day, name):
        self.day_selected = day
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = name
         
        #data
        self.values['day_selected'] = day
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = self.day_name
        self.values['month_name'] = calendar.month_name[self.month_selected]
        self.clear_calendar()
        self.calendarselection(self.year, self.month)
       
    def calendarselection(self, y, m):
        global frame  
        global selectedtime
        now = datetime.datetime.now()
        frame = Frame(root , padx = 10, pady = 27, relief = FLAT)
        frame.place(x = 150, y = 35)
        
        leftimg = PhotoImage(file = 'left.png')
        leftbtn = tk.Button(frame, image = leftimg, command=self.go_prevbtn)
        leftbtn.image = leftimg
        leftbtn.grid(row = 0, column = 0)
         
        header = tk.Label(frame, height = 2, font = 20, text='{}   {}'.format(calendar.month_name[m], str(y)))
        header.grid(row = 0, column = 2, columnspan = 3)
        
        rightimg = PhotoImage(file = 'right.png')
        rightbtn = tk.Button(frame, image = rightimg, command=self.go_nextbtn)
        rightbtn.image = rightimg
        rightbtn.grid(row = 0, column = 6)

         
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for z, name in enumerate(days):
            dayname = tk.Label(frame, text = name[:3], font = 15)
            dayname.grid(row = 1, column = z)
            
       
        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    buttonspawn = tk.Button(frame, width = 5, text=day, command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
                    self.daybutton.append(buttonspawn)
                    buttonspawn.grid(row = w, column = d)
        
        self.disablebuttons()       
        selecteddate = tk.Label(root, text='Date  Selected:  {} {} {}'.format(self.day_selected, calendar.month_abbr[self.month_selected], self.year_selected))
        selecteddate.place(x = 150, y = 338)
        self.selectedtime = StringVar()
        self.selectedtime.set("Time Selected: ")
        self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
        self.selectedtime.set("Time Selected:" + "                                           ")
        self.departtimecombobox()
        nextimg = PhotoImage(file = 'nexttxt.png')
        nextbtn = tk.Button(root, image = nextimg, command = self.changevaluetostring)
        nextbtn.image = nextimg
        nextbtn.place(x = 400, y = 355)

    def refreshcombobox(self):
        if (time.strftime('%H:%M:%S') == '08:00:00') or (time.strftime('%H:%M:%S') == '12:00:00') or (time.strftime('%H:%M:%S') == '16:00:00'):
            self.departtimecombobox()
            self.selectedtime = StringVar()
            self.selectedtime.set("Time Selected: ")
            self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
            self.selectedtime.set("Time Selected:" + "                                           ")
            
    def departtimecombobox(self):
        frame3 = Frame(root , padx = 10, pady = 10, bd=1, relief = RAISED)
        frame3.place(x = 10, y = 219)
        self.selectedtime = StringVar()
        self.selectedtime.set("Time Selected: ")
        now = datetime.datetime.now()
        if self.day_selected == now.day:
            if now.hour < 8:
                frame3 = Frame(root , padx = 10, pady = 10, bd=1, relief = RAISED)
                frame3.place(x = 10, y = 219)
                tk.Label(frame3, text = "Departure Time: ").grid(row = 0, column = 1)
                self.timedepart = ttk.Combobox(frame3, width = 14, state = "readonly")
                self.timedepart['value'] = ('08:00AM', '12:00PM', '04:00PM')
                self.timedepart.grid(row = 1, column = 1)
                confirmimg = PhotoImage(file = 'confirm.png')
                confirmbtn = tk.Button(frame3, image = confirmimg,text = "Confirm", command = self.clickedconfirm)
                confirmbtn.image = confirmimg
                confirmbtn.grid(row = 10, column = 1, columnspan = 2)
                self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
            if now.hour >= 8 and now.hour < 12:
                frame3 = Frame(root , padx = 10, pady = 10, bd=1, relief = RAISED)
                frame3.place(x = 10, y = 219)
                tk.Label(frame3, text = "Departure Time: ").grid(row = 0, column = 1)
                self.timedepart = ttk.Combobox(frame3, width = 14, state = "readonly")
                self.timedepart['value'] = ('08:00AM (N.A.)', '12:00PM', '04:00PM')
                self.timedepart.grid(row = 1, column = 1)
                confirmimg = PhotoImage(file = 'confirm.png')
                confirmbtn = tk.Button(frame3, image = confirmimg,text = "Confirm", command = self.clickedconfirm)
                confirmbtn.image = confirmimg
                confirmbtn.grid(row = 10, column = 1, columnspan = 2)
                self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
            if now.hour >= 12 and now.hour < 16 and int(time.strftime('%S')) >= 00:
                now = datetime.datetime.now()
                frame3 = Frame(root , padx = 10, pady = 10, bd=1, relief = RAISED)
                frame3.place(x = 10, y = 219)
                tk.Label(frame3, text = "Departure Time: ").grid(row = 0, column = 1)
                self.timedepart = ttk.Combobox(frame3, width = 14, state = "readonly")
                self.timedepart['value'] = ('08:00AM (N.A.)', '12:00PM (N.A.)', '04:00PM')
                self.timedepart.grid(row = 1, column = 1)
                confirmimg = PhotoImage(file = 'confirm.png')
                confirmbtn = tk.Button(frame3, image = confirmimg,text = "Confirm", command = self.clickedconfirm)
                confirmbtn.image = confirmimg
                confirmbtn.grid(row = 10, column = 1, columnspan = 2)
                self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
            if self.month_selected == now.month and now.hour >= 16:
                frame3 = Frame(root , padx = 8, pady = 15, bd=1, relief = RAISED)
                self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)
                self.selectedtime.set("                                                              ")
                selecteddate = tk.Label(root, text='Please choose the other day.                     ')
                selecteddate.place(x = 150, y = 338)                
                frame3.place(x = 11, y = 219)
                tk.Label(frame3, text = "").grid(row = 0, column = 1)
                tk.Label(frame3, text = "No ride(s) available.").grid(row = 1, column = 1)
                tk.Label(frame3, text = "").grid(row = 2, column = 1)
        else:       
            frame3 = Frame(root , padx = 10, pady = 10, bd=1, relief = RAISED)
            frame3.place(x = 10, y = 219)   
            self.selectedtime = StringVar()
            self.selectedtime.set("Time Selected: ")            
            tk.Label(frame3, text = "Departure Time: ").grid(row = 0, column = 1)
            self.timedepart = ttk.Combobox(frame3, width = 14, state = "readonly")
            self.timedepart['value'] = ('08:00AM', '12:00PM', '04:00PM')
            self.timedepart.grid(row = 1, column = 1)
            confirmimg = PhotoImage(file = 'confirm.png')
            confirmbtn = tk.Button(frame3, image = confirmimg,text = "Confirm", command = self.clickedconfirm)
            confirmbtn.image = confirmimg
            confirmbtn.grid(row = 10, column = 1, columnspan = 2)
            self.slttime = tk.Label(root, textvariable = self.selectedtime).place(x = 150, y = 320)

    def disablebuttons(self):
        selecteddate = tk.Label(root, text='                                                  ')
        selecteddate.place(x = 150, y = 338)
        now = datetime.datetime.now()
        if now.year > self.year:
            self.daybutton[0].configure(state=DISABLED)
            self.daybutton[1].configure(state=DISABLED) 
            self.daybutton[2].configure(state=DISABLED)
            self.daybutton[3].configure(state=DISABLED)
            self.daybutton[4].configure(state=DISABLED)
            self.daybutton[5].configure(state=DISABLED)
            self.daybutton[6].configure(state=DISABLED)
            self.daybutton[7].configure(state=DISABLED)
            self.daybutton[8].configure(state=DISABLED)
            self.daybutton[9].configure(state=DISABLED)
            self.daybutton[10].configure(state=DISABLED)
            self.daybutton[11].configure(state=DISABLED)
            self.daybutton[12].configure(state=DISABLED)
            self.daybutton[13].configure(state=DISABLED)
            self.daybutton[14].configure(state=DISABLED)
            self.daybutton[15].configure(state=DISABLED)
            self.daybutton[16].configure(state=DISABLED)
            self.daybutton[17].configure(state=DISABLED)
            self.daybutton[18].configure(state=DISABLED)
            self.daybutton[19].configure(state=DISABLED)
            self.daybutton[20].configure(state=DISABLED)
            self.daybutton[21].configure(state=DISABLED)
            self.daybutton[22].configure(state=DISABLED)
            self.daybutton[23].configure(state=DISABLED)
            self.daybutton[24].configure(state=DISABLED)
            self.daybutton[25].configure(state=DISABLED)
            self.daybutton[26].configure(state=DISABLED)
            self.daybutton[27].configure(state=DISABLED)
            if self.month ==2:
                if calendar.isleap(self.year) == True:
                    self.daybutton[28].configure(state=DISABLED)
            if self.month == 4 or self.month ==6 or self.month==9 or self.month == 11:
                self.daybutton[28].configure(state=DISABLED)
                self.daybutton[29].configure(state=DISABLED)
            if self.month == 1 or self.month== 3 or self.month==5 or self.month==7 or self.month==8 or self.month==10 or self.month==12 :
                self.daybutton[28].configure(state=DISABLED)
                self.daybutton[29].configure(state=DISABLED)
                self.daybutton[30].configure(state=DISABLED)
        if now.year == self.year:
            if (now.month > self.month):
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
                self.daybutton[24].configure(state=DISABLED)
                self.daybutton[25].configure(state=DISABLED)
                self.daybutton[26].configure(state=DISABLED)
                self.daybutton[27].configure(state=DISABLED)

                if self.month ==2:
                    if calendar.isleap(self.year) == True:
                        self.daybutton[28].configure(state=DISABLED)
                if self.month == 4 or self.month ==6 or self.month==9 or self.month == 11:
                    self.daybutton[28].configure(state=DISABLED)
                    self.daybutton[29].configure(state=DISABLED)
                if self.month == 1 or self.month== 3 or self.month==5 or self.month==7 or self.month==8 or self.month==10 or self.month==12 :
                    self.daybutton[28].configure(state=DISABLED)
                    self.daybutton[29].configure(state=DISABLED) 
                    self.daybutton[30].configure(state=DISABLED)
        if now.month == self.month :        
            if now.day == 2:
                self.daybutton[0].configure(state=DISABLED)
            if now.day == 3:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
            if now.day == 4:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
            if now.day == 5:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
            if now.day == 6:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
            if now.day == 7:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
            if now.day == 8:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
            if now.day == 9:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
            if now.day == 10:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
            if now.day == 11:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
            if now.day == 12:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
            if now.day == 13:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
            if now.day == 14:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
            if now.day == 15:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
            if now.day == 16:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
            if now.day == 17:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
            if now.day == 18:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
            if now.day == 19:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
            if now.day == 20:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
            if now.day == 21: 
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
            if now.day == 22:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
            if now.day == 23:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
            if now.day == 24:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
            if now.day == 25:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
            if now.day == 26:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
                self.daybutton[24].configure(state=DISABLED)
            if now.day == 27: 
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
                self.daybutton[24].configure(state=DISABLED)
                self.daybutton[25].configure(state=DISABLED)
            if now.day == 28:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
                self.daybutton[24].configure(state=DISABLED)
                self.daybutton[25].configure(state=DISABLED)
                self.daybutton[26].configure(state=DISABLED)
            if now.day == 29:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
                self.daybutton[24].configure(state=DISABLED)
                self.daybutton[25].configure(state=DISABLED)
                self.daybutton[26].configure(state=DISABLED)
                self.daybutton[27].configure(state=DISABLED)
            if now.day == 30: 
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
                self.daybutton[24].configure(state=DISABLED)
                self.daybutton[25].configure(state=DISABLED)
                self.daybutton[26].configure(state=DISABLED)
                self.daybutton[27].configure(state=DISABLED)
                self.daybutton[28].configure(state=DISABLED)
            if now.day == 31:
                self.daybutton[0].configure(state=DISABLED)
                self.daybutton[1].configure(state=DISABLED) 
                self.daybutton[2].configure(state=DISABLED)
                self.daybutton[3].configure(state=DISABLED)
                self.daybutton[4].configure(state=DISABLED)
                self.daybutton[5].configure(state=DISABLED)
                self.daybutton[6].configure(state=DISABLED)
                self.daybutton[7].configure(state=DISABLED)
                self.daybutton[8].configure(state=DISABLED)
                self.daybutton[9].configure(state=DISABLED)
                self.daybutton[10].configure(state=DISABLED)
                self.daybutton[11].configure(state=DISABLED)
                self.daybutton[12].configure(state=DISABLED)
                self.daybutton[13].configure(state=DISABLED)
                self.daybutton[14].configure(state=DISABLED)
                self.daybutton[15].configure(state=DISABLED)
                self.daybutton[16].configure(state=DISABLED)
                self.daybutton[17].configure(state=DISABLED)
                self.daybutton[18].configure(state=DISABLED)
                self.daybutton[19].configure(state=DISABLED)
                self.daybutton[20].configure(state=DISABLED)
                self.daybutton[21].configure(state=DISABLED)
                self.daybutton[22].configure(state=DISABLED)
                self.daybutton[23].configure(state=DISABLED)
                self.daybutton[24].configure(state=DISABLED)
                self.daybutton[25].configure(state=DISABLED)
                self.daybutton[26].configure(state=DISABLED)
                self.daybutton[27].configure(state=DISABLED)
                self.daybutton[28].configure(state=DISABLED)
                self.daybutton[29].configure(state=DISABLED) 
                	

    def changevaluetostring(self):
        global timedepart
        now = datetime.datetime.now()
        if (self.day_selected == now.day) and (now.hour > 16):
           messagebox.showinfo("Sorry, my dear customer...","This date({} {} {}) is not available. Please choose other available date(s).".format(calendar.month_abbr[self.month_selected],self.day_selected, self.year_selected),icon='warning')
        else:   
            self.num = int(self.filedata[0]['num'])
            #day
            if self.day_selected == 1:
                self.day = "1"
            if self.day_selected == 2:
                self.day = "2"
            if self.day_selected == 3:
                self.day = "3"
            if self.day_selected == 4:
                self.day = "4"
            if self.day_selected == 5:
                self.day = "5"
            if self.day_selected == 6:
                self.day = "6"
            if self.day_selected == 7:
                self.day = "7"
            if self.day_selected == 8:
                self.day = "8"
            if self.day_selected == 9:
                self.day = "9"
            if self.day_selected == 10:
                self.day = "10"
            if self.day_selected == 11:
                self.day = "11"
            if self.day_selected == 12:
                self.day = "12"
            if self.day_selected == 13:
                self.day = "13"
            if self.day_selected == 14:
                self.day = "14"
            if self.day_selected == 15:
                self.day = "15"
            if self.day_selected == 16:
                self.day = "16"
            if self.day_selected == 17:
                self.day = "17"
            if self.day_selected == 18:
                self.day = "18"
            if self.day_selected == 19:
                self.day = "19"
            if self.day_selected == 20:
                self.day = "20"
            if self.day_selected == 21:
                self.day = "21"
            if self.day_selected == 22:
                self.day = "22"
            if self.day_selected == 23:
                self.day = "23"
            if self.day_selected == 24:
                self.day = "24"
            if self.day_selected == 25:
                self.day = "25"
            if self.day_selected == 26:
                self.day = "26"
            if self.day_selected == 27:
                self.day = "27"
            if self.day_selected == 28:
                self.day = "28"
            if self.day_selected == 29:
                self.day = "29"
            if self.day_selected == 30:
                self.day = "30"
            if self.day_selected == 31:
                self.day = "31"
            #month
            if self.month_selected == 1:
                self.mth = "1"
            if self.month_selected == 2:
                self.mth = "2"
            if self.month_selected == 3:
                self.mth = "3"
            if self.month_selected == 4:
                self.mth = "4"
            if self.month_selected == 5:
                self.mth = "5"
            if self.month_selected == 6:
                self.mth = "6"
            if self.month_selected == 7:
                self.mth = "7"
            if self.month_selected == 8:
                self.mth = "8"
            if self.month_selected == 9:
                self.mth = "9"
            if self.month_selected == 10:
                self.mth = "10"
            if self.month_selected == 11:
                self.mth = "11"
            if self.month_selected == 12:
                self.mth = "12"
            self.td = self.timedepart.get()
            if self.td == "08:00AM" and self.cfm >= 0:
                self.filedata[0]['timedepart'] = self.timedepart.get()
            if self.td == "12:00PM" and self.cfm >= 0:
                self.filedata[0]['timedepart'] = self.timedepart.get()   
            if self.td == "04:00PM" and self.cfm >= 0:
                self.filedata[0]['timedepart'] = self.timedepart.get()
            if (self.td == '08:00AM (N.A.)' or self.td == '12:00PM (N.A.)'):
                messagebox.showinfo("Sorry, my dear customer...","Departure time is not available. Please try again.",icon='warning')
                self.cfm = 0
                return
            if self.td == "" or self.cfm == 0:
                messagebox.showinfo("Sorry, my dear customer...","Departure time is not selected. Please try again.",icon='warning')
                return
            day = self.year_selected
            if self.cfm == 0:
                return
            self.save_to_file()
    def save_to_file(self):
        for i in range ( 1 , len(self.filedata)):
            now = datetime.datetime.now() 
            self.filedata[0]['month'] = self.mth
            self.filedata[0]['day'] = self.day
            self.filedata[0]['year'] = str(self.year_selected)
            self.filedata[0]['timedepart'] = self.td
            if (len(self.filedata[0]['iclist'])) > self.num :
               if ((self.filedata[i]['nric']) == (self.filedata[0]['iclist'][self.num]) and 
                    (self.filedata[i]['fileno']) == 0):
                    self.num +=1
                    self.filedata[i]['month'] = self.mth
                    self.filedata[i]['day'] = self.day
                    self.filedata[i]['year'] = str(self.year_selected)
                    self.filedata[i]['timedepart'] = self.td
                    if now.day < 10:                    
                        self.filedata[i]['datepurchased'] = ("0")+(str(now.day))+'_'+("0")+(str(now.month))+'_'+(str(now.year))
                    if now.month < 10:
                        self.filedata[i]['datepurchased'] = (str(now.day))+'_'+("0")+(str(now.month))+'_'+(str(now.year))                       
                    if now.day < 10 and now.month < 10:                 
                        self.filedata[i]['datepurchased'] = ("0")+(str(now.day))+'_'+("0")+(str(now.month))+'_'+(str(now.year))
                    if now.day > 9 and now.month > 9:           
                        self.filedata[i]['datepurchased'] = (str(now.day))+'_'+(str(now.month))+'_'+(str(now.year))                         
        self.updateJsonFile()
        root.withdraw()
        root.unbind('<Escape>')
        SelectSeat.seatlayout()

    def updateJsonFile(self) :
        with open ('Master.json' ,'w') as json_file:
            json.dump(self.filedata,json_file, indent=4)
        
            
if __name__ == '__main__':
    cal = Calendar()



    

