from tkinter import*
import tkinter.messagebox
import json
import datetime
import os
import SelectSeat
import endscreen
from os import walk

class bus_tickets():

    def __init__(self):
        global window
        global text
        global CurrentUser
        window = Toplevel()
        self.openJsonFile()
        CurrentUser=self.data[0]['currentuser']
        
        #create tkinter window and fix it in the center of the computer screen
        window.title("Long Distance Bus Tickets Booking System (Login As: {})".format(CurrentUser))
        window.resizable (0,0)
        window.attributes("-toolwindow",1)
        window.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        window.bind('<Escape>',self.escbutton)
        w = 500 
        h = 400 
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.iconbitmap('busicon32.ico')
        
        #set text configure in tkinter and scroll bar
        text = Text(window , relief = SUNKEN, bg="#EEEEEE", highlightcolor='black')
        scroll = Scrollbar(window, command=text.yview)
        text.configure(yscrollcommand=scroll.set)
        text.tag_configure('text1', foreground='black',font=('Times',15,'bold'))
        text.tag_configure('text2', foreground='black',font=('Times',18,'bold','italic'))
        scroll.pack(side=RIGHT, fill=Y)
        self.openJsonFile()
        self.calPriceWithoutInsurance()
        window.mainloop()

    #function to read data from json file   
    def openJsonFile(self):
        with open('Master.json','r') as json_file:
            self.data=json.load(json_file)
        with open('CheckListSeat.json','r') as json_file2:
            self.listseat=json.load(json_file2)
        return (self.data,self.listseat)
            
    #function to calculate the bus ticket price without insurance       
    def calPriceWithoutInsurance(self):
        global CurrentUser
        self.num=self.data[0]['num']
        for i in range (1 ,len(self.data)):
            if ((self.data[i]['username']==(self.data[0]['currentuser']))and
            (self.data[i]['nric']==(self.data[0]['iclist'][self.num]))and
            (self.data[i]['fileno']== 0)):
                if (self.data[0]['depart']=="Melaka"):
                    if (self.data[0]['arrival']=="Seremban"):
                        if (self.data[i]['priority']==1):
                            self.price=8.0*50/100
                        else:
                            self.price=8.0

                if (self.data[0]['depart']=="Melaka"):
                    if (self.data[0]['arrival']=="Butterworth"):
                        if (self.data[i]['priority']==1):
                            self.price=50.0*50/100
                        else:
                            self.price=50.0
                        
                if (self.data[0]['depart']=="Butterworth"):
                    if (self.data[0]['arrival']=="Melaka"):
                        if (self.data[i]['priority']==1):
                            self.price=50.0*50/100
                        else:
                            self.price=50.0

                if (self.data[0]['depart']=="Butterworth"):
                    if (self.data[0]['arrival']=="Seremban"):
                        if (self.data[i]['priority']==1):
                            self.price=46.0*50/100
                        else:
                            self.price=46.0

                if (self.data[0]['depart']=="Seremban"):
                    if (self.data[0]['arrival']=="Melaka"):
                        if (self.data[i]['priority']==1):
                            self.price=8.0*50/100
                        else:
                            self.price=8.0

                if (self.data[0]['depart']=="Seremban"):
                    if (self.data[0]['arrival']=="Butterworth"):
                        if (self.data[i]['priority']==1):
                            self.price=46.0*50/100
                        else:
                            self.price=46.0
        self.askInsurance()
    
    #function to ask the user to include the optional travel insurance
    def askInsurance(self):
        global displayic
        self.passengerdtsImg=PhotoImage(file='passengerdts.png')
        self.title=Label(window,image=self.passengerdtsImg)
        self.title.place(x=0)
        
        #to display the word "None" in tkinter window if the user do not insert IC number beforehand
        displayic=[]
        for x in range (0, len(self.data[0]['iclist'])):        
            if self.data[0]['iclist'][x][0:4] == "null" : 
                displayic.append("None")
            else:
                displayic.append(self.data[0]['iclist'][x])
                
        for i in range (1 ,len(self.data)):
            if ((self.data[i]['username']==(self.data[0]['currentuser']))and
            (self.data[i]['nric']==(self.data[0]['iclist'][self.num]))and
            (self.data[i]['fileno']== 0)):
                answer=tkinter.messagebox.askquestion("Travel Insurance",(displayic[self.num]+", "+"do you want travel insurance? Travel insurance for a ride is RM4."))
                if (answer=='yes'):
                    self.price=self.price+4
                    self.data[i]['price']=self.price
                    text.insert(END,"IC Number: ",'text1')
                    text.insert(END,displayic[self.num] +'\n','text1')
                    text.insert(END,"Departure: ",'text1')
                    text.insert(END,self.data[i]['depart']+'\n','text1')
                    text.insert(END,"Arrival: ",'text1')
                    text.insert(END,self.data[i]['arrival']+'\n','text1')
                    text.insert(END,"Date: ",'text1')
                    text.insert(END,self.data[i]['day']+'/','text1')
                    text.insert(END,self.data[i]['month']+'/','text1')
                    text.insert(END,self.data[i]['year']+'\n','text1')
                    text.insert(END,"Departure Time: ",'text1')
                    text.insert(END,self.data[i]['timedepart']+'\n','text1')
                    text.insert(END,"Seat Number: ",'text1')
                    text.insert(END,self.data[i]['seatno']+'\n','text1')
                    text.insert(END,"Price: RM",'text1')
                    text.insert(END,'{0:1.2f}'.format(self.price),'text1')
                    text.insert(END,'\n','text1')
                    text.insert(END,'\n','text1')
                    text.place(x=1,y=40,height=300,width=500)
                else:
                    self.data[i]['price']=self.price
                    text.insert(END,"IC Number: ",'text1')
                    text.insert(END,displayic[self.num]+'\n','text1')
                    text.insert(END,"Departure: ",'text1')
                    text.insert(END,self.data[i]['depart']+'\n','text1')
                    text.insert(END,"Arrival: ",'text1')
                    text.insert(END,self.data[i]['arrival']+'\n','text1')
                    text.insert(END,"Date: ",'text1')
                    text.insert(END,self.data[i]['day']+"/",'text1')
                    text.insert(END,self.data[i]['month']+"/",'text1')
                    text.insert(END,self.data[i]['year']+'\n','text1')
                    text.insert(END,"Departure Time: ",'text1')
                    text.insert(END,self.data[i]['timedepart']+'\n','text1')
                    text.insert(END,"Seat Number: ",'text1')
                    text.insert(END,self.data[i]['seatno']+'\n','text1')
                    text.insert(END,"Price: RM",'text1')
                    text.insert(END,'{0:1.2f}'.format(self.price),'text1')
                    text.insert(END,'\n','text1')
                    text.insert(END,'\n','text1')
                    text.place(x=1,y=40,height=300,width=500)
                break
        self.updateJsonFile()
        #to create a "Next" and a "Back" button
        self.NextImg=PhotoImage(file='nexttxt.png')
        self.nextbtn=Button(window,image=self.NextImg,command=self.next_button)
        self.nextbtn.place(x=300, y=350, height=30, width=100)
        self.BackImg=PhotoImage(file='backtxt.png')
        self.backbtn=Button(window,image=self.BackImg,command=self.back_button)
        self.backbtn.place(x=100, y=350, height=30, width=100)
    
    #function to update data in json file   
    def updateJsonFile(self):
        with open('Master.json','w') as json_file:
            json.dump(self.data,json_file,indent=4)
        with open('CheckListSeat.json','w') as json_file:
            json.dump(self.listseat,json_file,indent=4)
            
    #function to give command to "Back" button
    def back_button(self):
        global seatno
        #to clear specific key value of 'seatno' key in Master.json file
        for i in range (1 ,len(self.data)):
            if ((self.data[i]['username']==(self.data[0]['currentuser']))and
            (self.data[i]['nric']==(self.data[0]['iclist'][self.num]))and
            (self.data[i]['fileno']== 0)):
                seatno=self.data[i]['seatno']
                self.data[i]['seatno']=""
        #to clear specific key value of 'listseatno' key in CheckListSeat.json file
        for i in range (0 ,len(self.listseat)):
            if ((self.listseat[i]['year']==(self.data[0]['year']))and
            (self.listseat[i]['month']==(self.data[0]['month']))and
            (self.listseat[i]['day']==(self.data[0]['day']))and
            (self.listseat[i]['timedepart']==(self.data[0]['timedepart']))and
            (self.listseat[i]['depart']==(self.data[0]['depart']))and
            (self.listseat[i]['arrival']==(self.data[0]['arrival']))):
                self.listseat[i]['listseatno'].remove(seatno)
        self.updateJsonFile()
        window.destroy()
        SelectSeat.seatlayout.callbackSeat(self)
        
    #function to give command to "Next" button
    def next_button(self):
        self.num+=1
        self.data[0]['num']=self.num
        self.updateJsonFile()
        if (self.num>=len(self.data[0]['iclist'])):
            text.delete('1.0',END)
            self.title.destroy()
            self.nextbtn.destroy()
            self.backbtn.destroy()
            self.ticketdtsImg=PhotoImage(file='ticketdts.png')
            self.title=Label(window,image=self.ticketdtsImg)
            self.title.place(x=0)
            #to create a "Confirm" button
            self.confirmImg=PhotoImage(file='confirm.png')
            self.confirmbtn=Button(window,image=self.confirmImg,command=self.close_window)
            self.confirmbtn.place(x=350, y=350, height=30, width=100)
            self.printAllTicket()
        else:
            window.destroy()
            SelectSeat.seatlayout()
            
    #function to print all tickets information in the screen of tkinter window    
    def printAllTicket(self):
        count=0
        #to calculate total price of the tickets
        totalprice=0
        for i in range (1 ,len(self.data)):
            if ((self.data[i]['username']==(self.data[0]['currentuser']))and
            (self.data[i]['nric']==(self.data[0]['iclist'][count]))and
            (self.data[i]['fileno']== 0)):
                totalprice=totalprice+self.data[i]['price']
                text.insert(END,"IC Number: ",'text1')
                text.insert(END,displayic[count]+'\n','text1')
                text.insert(END,"Departure: ",'text1')
                text.insert(END,self.data[i]['depart']+'\n','text1')
                text.insert(END,"Arrival: ",'text1')
                text.insert(END,self.data[i]['arrival']+'\n','text1')
                text.insert(END,"Date: ",'text1')
                text.insert(END,self.data[i]['day']+"/",'text1')
                text.insert(END,self.data[i]['month']+"/",'text1')
                text.insert(END,self.data[i]['year']+'\n','text1')
                text.insert(END,"Departure Time: ",'text1')
                text.insert(END,self.data[i]['timedepart']+'\n','text1')
                text.insert(END,"Seat Number: ",'text1')
                text.insert(END,self.data[i]['seatno']+'\n','text1')
                text.insert(END,"Price: RM",'text1')
                text.insert(END,'{0:1.2f}'.format(self.data[i]['price']),'text1')
                text.insert(END,'\n','text1')
                text.insert(END,'\n','text1')
                text.place(x=1,y=40,height=300,width=500)
                self.nowdate=self.data[i]['datepurchased']
                count+=1
        labelprice=Label(window, text ="Total Price: RM {0:1.2f}".format(totalprice), font='none 15 bold')
        labelprice.place(x=50, y=350)
    
    #function to give command to "Confirm" button
    def close_window(self):
        self.saveDataToTextFile() 
        os.chdir(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject'))
        window.iconify()
        endscreen.Endscreen()

    #function to write all tickets information in a text file 
    def saveDataToTextFile(self):
        #to go through all the text files in CurrentUser's folder
        listfiles=[]
        os.chdir(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject\\Users',CurrentUser))
        for dirpath,dirnames, filenames in walk(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject\\Users',CurrentUser)):
            for x in range (0,len(filenames)):
                listfiles.append(filenames[x])
        times=1
        
        #to make sure the text file name do not duplicate
        for y in range (0,len(listfiles)):
            if listfiles[y] == '{}_{}_{}.txt'.format(self.nowdate,CurrentUser,times):
                times+=1

        #to create a text file and write the information into it
        with open('{}_{}_{}.txt'.format(self.nowdate,CurrentUser,times),'w') as text_file:
            text_file.write("Ticket Details:")
            text_file.write('\n')
            text_file.write('\n')
            turn=0
            self.num=self.data[0]['num']
            for i in range (1 ,len(self.data)):
                if ((self.data[i]['username']==(self.data[0]['currentuser']))and
                (self.data[i]['nric']==(self.data[0]['iclist'][turn]))and
                (self.data[i]['fileno']== 0)):
                    text_file.write("IC Number: ")
                    text_file.write(displayic[turn]+'\n')
                    text_file.write("Departure: ")
                    text_file.write(self.data[i]['depart']+'\n')
                    text_file.write("Arrival: ")
                    text_file.write(self.data[i]['arrival']+'\n')
                    text_file.write("Date: ")
                    text_file.write(self.data[i]['day']+"/")
                    text_file.write(self.data[i]['month']+"/")
                    text_file.write(self.data[i]['year']+'\n')
                    text_file.write("Departure Time: ")
                    text_file.write(self.data[i]['timedepart']+'\n')
                    text_file.write("Seat Number: ")
                    text_file.write(self.data[i]['seatno']+'\n')
                    text_file.write("Total Price: RM ")
                    text_file.write('{0:1.2f}'.format(self.data[i]['price']))
                    text_file.write('\n')
                    text_file.write('\n')
                    turn+=1
        count=0
        for i in range (1 ,len(self.data)):
            if ((self.data[i]['username']==(self.data[0]['currentuser']))and
            (self.data[i]['nric']==(self.data[0]['iclist'][count]))and
            (self.data[i]['fileno']== 0)):
                self.data[i]['fileno']=times
                count+=1
        os.chdir(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject'))
        self.updateJsonFile()
        
    def escbutton(self,event):
        self.closebuttonwindow()
        
    #To clear the data in Master.json and CheckListSeat.json file if the user press 'X' (Close button) on the window top bar
    def closebuttonwindow (self):
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
            
if __name__ == '__main__':
    ticketinfo=bus_tickets()




    
