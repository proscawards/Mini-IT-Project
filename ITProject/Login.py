from tkinter import *
from tkinter import messagebox
import json
import os


class loginRegister():
    def closebuttonwindow (self):
        pass

    def openJsonFile(self):
        with open ('member.json') as json_file:
            self.members = json.load(json_file)
        with open ('Master.json') as json_file2:
            self.data = json.load(json_file2)
        return (self.members,self.data)
    
    def __init__(self):
        self.openJsonFile()
        global login
        login = Tk()
        login.title("Long Distance Bus Tickets Booking System")
        login.resizable (0,0)
        login.attributes("-toolwindow",1)
        login.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        w = 500 
        h = 400 
        ws = login.winfo_screenwidth()
        hs = login.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        login.geometry('%dx%d+%d+%d' % (w, h, x, y))
        login.bind('<Return>', self.enterclick)
        logintitleimg = PhotoImage(file = 'logintitle1.png')
        instruction1 = Label(login, image = logintitleimg)
        instruction1.image = logintitleimg
        instruction1.place(x=145,y=80)

        usernameLabel = Label(login, text="Username:")
        usernameLabel.place(x=150,y=150)    
        self.userEnter = Entry(login, width = 23)
        self.userEnter.place(x=220,y=150)

        passwordLabel = Label(login, text="Password:")
        passwordLabel.place(x=150,y=200)
        self.passEnter = Entry(login, show="*", width = 23)
        self.passEnter.place(x=220,y=200)
        
        self.passwordvimg = PhotoImage(file = 'passview.png')
        self.passwordvbtn = Button(login, image = self.passwordvimg, relief = FLAT,bd = 0, bg = 'white', command = self.loginpasswordhideimg)
        self.passwordvbtn.image = self.passwordvimg
        self.passwordvbtn.place(x=344,y=202)

        
        registerimg = PhotoImage(file = 'register.png')
        registerbtn = Button(login, image = registerimg, command = lambda: self.openRegisterWindow(login))
        registerbtn.image = registerimg
        registerbtn.place(x=20, y=350)
        self.loginimg = PhotoImage(file = 'login.png')
        loginbtn = Button(login,image = self.loginimg ,command= lambda: self.checkLogin(login))
        loginbtn.place(x=400,y=350)
        exitimg = PhotoImage(file = 'exit.png')
        exitbtn= Button(login, image = exitimg, command = lambda : exit())
        exitbtn.image = exitimg
        exitbtn.place(x= 400, y= 10)
        login.mainloop()
    
    def enterclick(self, event=None):
        self.checkLogin(login)
		
    def loginpasswordhideimg(self): #show the password entered
        self.passEnter.config(show="")
        self.passwordhimg = PhotoImage(file = 'passhide.png')
        self.passwordvbtn.image = self.passwordhimg
        self.passwordvbtn.config(image = self.passwordhimg, command = self.loginpasswordviewimg)
        
    def loginpasswordviewimg(self): #hide the password entered
        self.passEnter.config(show="*")
        self.passwordvimg = PhotoImage(file = 'passview.png')
        self.passwordvbtn.image = self.passwordvimg
        self.passwordvbtn.config(image = self.passwordvimg, command = self.loginpasswordhideimg)
        
        
    def registerWindow(self, login):
        global register
        register = Toplevel()
        register.title("Long Distance Bus Tickets Booking System")
        register.resizable (0,0)
        register.attributes("-toolwindow",1)
        register.protocol('WM_DELETE_WINDOW',self.closebuttonwindow)
        w = 500 
        h = 400 
        ws = register.winfo_screenwidth()
        hs = register.winfo_screenheight() 
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        register.geometry('%dx%d+%d+%d' % (w, h, x, y))
        register.bind('<Return>', self.enterregclick)
        logintitleimg2 = PhotoImage(file = 'logintitle2.png')
        instruction2 = Label(register, image = logintitleimg2)
        instruction2.image = logintitleimg2
        instruction2.place(x=145,y=80)

        usernameLabel = Label(register, text="Username:")
        usernameLabel.place(x=150,y=150)
        self.userEntry = Entry(register, width = 23)
        self.userEntry.place(x=220,y=150)

        passwordLabel = Label(register, text="Password:")
        passwordLabel.place(x=150,y=200)
        self.passEntry = Entry(register, show="*", width = 23)
        self.passEntry.place(x=220,y=200)

        self.passwordvregimg = PhotoImage(file = 'passview.png')
        self.passwordvregbtn = Button(register, image = self.passwordvimg, relief = FLAT,bd = 0, bg = 'white', command = self.registerpasswordhideimg)
        self.passwordvregbtn.place(x=344,y=202)
        
        passwordConfirm = Label(register, text="Re-enter password:")
        passwordConfirm.place(x=100,y=250)
        self.passConfirm = Entry(register, show="*", width = 23)
        self.passConfirm.place(x=220, y=250)

        self.submitimg = PhotoImage(file = 'submit.png')
        submitbtn = Button(register, image = self.submitimg, command= lambda: self.registration(login, register))
        submitbtn.place(x=400,y=350)
        self.backimg = PhotoImage(file = 'backtxt.png')
        backbtn = Button(register, image = self.backimg, command= lambda: self.openLoginPage(register,login))
        backbtn.place(x=20,y=350)

    def enterregclick(self, event):
        self.registration(login, register)
		
    def registerpasswordhideimg(self): #show the password entered in register screen
        self.passEntry.config(show="")
        self.passwordhregimg = PhotoImage(file = 'passhide.png')
        self.passwordvregbtn.config(image = self.passwordhregimg, command = self.registerpasswordviewimg)
        
    def registerpasswordviewimg(self): #hide the password entered in register screen
        self.passEntry.config(show="*")
        self.passwordvregimg = PhotoImage(file = 'passview.png')
        self.passwordvregbtn.config(image = self.passwordvregimg, command = self.registerpasswordhideimg) 
        
    def openRegisterWindow(self, login):
        login.withdraw()
        self.registerWindow(login)
    

    def openLoginPage(self, registration,login):
        registration.destroy()
        os.chdir(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject'))
        login.deiconify()
    
    def checkLogin(self,login): #check if the username and password entered match the data in json file
        count = 0
        for x in range(0, len(self.members)):
            if (self.userEnter.get()).lower() == self.members[x]["username"] and self.passEnter.get() == self.members[x]["password"]:

                self.data[0]['currentuser']=(self.userEnter.get()).lower()
                messagebox.showinfo("Login","Login successful!")
                os.chdir(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject'))
                self.saveMastertoJson()
                login.destroy()
                break
            else:
                count +=1

            if count == len(self.members):  #show error message when the it checked till the end of the list
                messagebox.showinfo("Login","Please check your username and password.")
                

    def registration(self, login, register):  #check if the info entered in registration window are eligible for new register
        count=0
        notmatch=0
        if len(self.userEntry.get()) >= 9:
            messagebox.showinfo("Opps","Username length cannot be more than 8 characters.")
            return
        if len(self.userEntry.get()) <1:
            messagebox.showinfo("Opps","Username cannot be blank.")
            return
        if len(self.passEntry.get()) <1:
            messagebox.showinfo("Opps","Password cannot be blank.")
            return
        if self.passConfirm.get() != self.passEntry.get():
            messagebox.showinfo("Opps","Both password did not match!")
            return
            
        if len(self.members) == 0:
            member = {}
            member["username"] = (self.userEntry.get()).lower()
            member["password"] = self.passEntry.get()
            self.members.append(member)
            messagebox.showinfo("Successful!","You have been registered successfully!")
            self.saveMembertoJson(register,login)
            return
            
        for i in range(0, len(self.members)):
            if self.userEntry.get() == self.members[i]["username"]:  #if there's found identical username, it will show error immediately
                count += 1
            if self.userEntry.get() != self.members[i]["username"]: #register successfully if the condition checked until the end of the dictionary
                notmatch += 1
            if self.userEntry.get() != self.members[i]["username"] and notmatch == len(self.members):
                member = {}
                member["username"] = (self.userEntry.get()).lower()
                member["password"] = self.passEntry.get()
                self.members.append(member)
                messagebox.showinfo("Successful!","You have been registered successfully!")
                self.saveMembertoJson(register,login)
                return
            if count >= 1 :
                messagebox.showinfo("Opps","Username has been taken, please enter a new one.")
                
                return
            
    def createfolder(self,register,login):
        os.chdir(os.path.join(os.environ["HOMEPATH"],'Desktop\\ITProject\\Users'))
        os.makedirs((self.userEntry.get()).lower())
        self.openLoginPage(register,login)
    def saveMembertoJson(self, register,login):
        with open ('member.json','w') as json_file:
            json.dump(self.members, json_file, indent=4)
        self.createfolder(register,login)
    def saveMastertoJson(self):
        with open ('Master.json','w') as json_file2:
            json.dump(self.data, json_file2, indent=4)
        
if __name__ == '__main__':
    abc=loginRegister()

    
