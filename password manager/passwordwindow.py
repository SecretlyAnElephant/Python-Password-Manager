import tkinter as tk
import passwordutilities as pu
import passwordretriever as pr

class PasswordWindow():

    def __init__(self):

        # very messy
        
        # define the root
        self.root = tk.Tk()

        # customise the window
        self.root.title("Password Manager")
        self.root.geometry("450x300")

        # define the password text label
        self.text = tk.StringVar()
        self.text.set("Press Generate")
        self.label = tk.Label(self.root, textvariable=self.text)

        # define the error message label
        self.errormessage = tk.StringVar()
        self.errorlabel = tk.Label(self.root, textvariable=self.errormessage)

        self.namelabel = tk.Label(self.root, text='Password Name')

        # define the buttons
        self.button = tk.Button(self.root,
                                text="Click to generate a password",
                                command=self.changeText)

        self.savebutton = tk.Button(self.root,
                                text="Save Password",
                                command=self.savePassword)

        # define the text inputs
        self.passname=tk.StringVar()
        self.passnameentry = tk.Entry(self.root, textvariable = self.passname, font=('calibre',10,'normal'))

        # define the deleting ui
        self.deletenamelabel = tk.Label(self.root, text='Delete a Password')
        self.deletename = tk.StringVar()
        self.warnstate = tk.StringVar()
        self.warnstate.set('Delete Password')
        self.deletenameentry = tk.Entry(self.root, textvariable = self.deletename, font=('calibre',10,'normal'))
        self.deletebutton = tk.Button(self.root,
                                textvariable = self.warnstate,
                                command=self.deletePassword)

        # define the checklist

        self.UsingLetters = tk.IntVar()
        self.UsingNumbers = tk.IntVar()
        self.UsingSymbols = tk.IntVar()
        self.CopyList = tk.IntVar()
        
        self.C1 = tk.Checkbutton(self.root, text = "Use Letters", variable = self.UsingLetters, onvalue = 1, offvalue = 0)
        self.C2 = tk.Checkbutton(self.root, text = "Use Numbers", variable = self.UsingNumbers, onvalue = 1, offvalue = 0)
        self.C3 = tk.Checkbutton(self.root, text = "Use Symbols", variable = self.UsingSymbols, onvalue = 1, offvalue = 0)
        self.C4 = tk.Checkbutton(self.root, text = "Copy to Clipboard", variable = self.CopyList, onvalue = 1, offvalue = 0)

        self.C1.grid(row=1, column=1)
        self.C2.grid(row=2, column=1)
        self.C3.grid(row=3, column=1)
        self.C4.grid(row=4, column=1)
        
        self.button.grid(row=5, column=1)
        self.label.grid(row=6, column=1)
        
        self.namelabel.grid(row=1, column=2)
        self.passnameentry.grid(row=2, column=2)
        self.savebutton.grid(row=3, column=2)
        self.errorlabel.grid(row=4, column=2)

        self.deletenamelabel.grid(row=1, column=3)
        self.deletenameentry.grid(row=2, column=3)
        self.deletebutton.grid(row=3, column=3)

        # from this point on EXTREMELY MESSY

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.grid(row=4, column=2)

        self.passlist = tk.Listbox(self.root, yscrollcommand = self.scrollbar.set)
        self.passlist.grid(row=4, column=2)
        
        for line in range(100):
            self.passlist.insert(tk.END, "Line" + str(line))
        
        self.root.mainloop()

        

    def changeText(self):
        self.passwordcache = pu.genpassword(16, self.UsingLetters.get(), self.UsingNumbers.get(), self.UsingSymbols.get(), self.CopyList.get())
        self.text.set(self.passwordcache)

    def savePassword(self):
        name = self.passname.get()
        password = self.text.get()
        result = pr.savePassword(name, password)
        if not result == '':
            self.errormessage.set(result)

    def deletePassword(self):
        
        warnstate = self.warnstate.get()
        if warnstate == 'Are you sure?':
            print('deleting (debugging)')
            
            name = self.deletename.get()
            print(name)
            pr.delete_json(name)
            
            self.deletebutton.configure(bg="white")
            
            self.warnstate.set('Delete Password')
            
        elif warnstate == 'Delete Password':
            print('confirming (debugging)')
            self.warnstate.set('Are you sure?')
            self.deletebutton.configure(bg="red")
        else:
            print('edgecase (debugging)')

    def loadPassword(self):
        pass # will work on this at home and update on github when its finished
