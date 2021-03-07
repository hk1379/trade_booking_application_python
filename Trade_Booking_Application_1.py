#
#Trading Platform
#

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
trade_id = 100000
confirmation_window = None
frame2 = None

class HkMenu:
    def __init__(self, master):
        
        #ensuring root will not have a tearable menu
        master.option_add('*tearOff', False)
        
        #adding menubar to root
        self.menubar = Menu(master)
        
        #setting the menubar object created
        master.config(menu = self.menubar)
        
        #all menu options will be a child of the menubar object
        self.file_menu = Menu(self.menubar)
        self.edit_menu = Menu(self.menubar)
        self.help_menu = Menu(self.menubar)
        
        #adding the menu options to frame2
        self.menubar.add_cascade(menu = self.file_menu, label = 'File')
        self.menubar.add_cascade(menu = self.edit_menu, label = 'Edit')
        self.menubar.add_cascade(menu = self.help_menu, label = 'Help')

class HkPanedWindow:
    def __init__(self, master):
        #creating a style
        style = ttk.Style(master)
        style.theme_use("clam")
        style.configure("Treeview", background = "white",
                        fieldbackground = "white", foreground = "black")
        style.configure("TFrame", background = "white",
                        fieldbackground = "white", foreground = "black")
        style.configure("TLabel", background = "white",
                        fieldbackground = "white", foreground = "black")
        style.configure("H.TLabel", background = "white",
                        fieldbackground = "white", foreground = "black", text = ('Helvetica', 14, 'bold'))

        #creating a paned window
        self.panedwindow = ttk.Panedwindow(master, orient = HORIZONTAL, width = 1050)
        
        #ensuring the paned window expands when the window size is increased
        self.panedwindow.pack(fill = BOTH, expand = True)
      
        #defining frame1
        global frame1
        frame1 = ttk.Frame(self.panedwindow, width = 400, height = 400,
                           relief = SUNKEN)
        #defining frame2
        global frame2
        frame2 = ttk.Frame(self.panedwindow, width = 650, height = 400,
                           relief = SUNKEN)
        
        #adding notebooks to panedwindow
        #weight defines how quickly one frame expands relative to the window size increasing
##        self.notebook = ttk.Notebook(self.panedwindow)
##        self.panedwindow.add(self.notebook, weight = 0)
##        self.notebook.add(self.frame0, text = 'FX')
##        self.notebook.add(self.frame1, text = 'Non FX')
        
        #adding the frames to the panedwindows
        self.panedwindow.add(frame1, weight = 0)
        self.panedwindow.add(frame2, weight = 1)
        
        #adding treeview to the frame
        self.treeview = ttk.Treeview(frame1)
        self.treeview.pack(fill = BOTH, expand = True)
        self.treeview.heading('#0', text = 'Template')
        #insert method (first parameter = the parent node of item being created)
        #root node has special name which is an empty string
        #second paramaeter = position of the node you want to add
        #third character = choose name of item being added
        self.treeview.insert('',0,'item0', text = 'Swap')
        self.treeview.insert('',1,'item1', text = 'Repo')
        self.treeview.insert('',2,'item2', text = 'Bond')
        self.treeview.insert('',3,'item3', text = 'Fra')
        self.treeview.insert('',4,'item4', text = 'Swaption')
        self.treeview.insert('',5,'item5', text = 'FX Swap')
        self.treeview.insert('',6,'item6', text = 'NDF')
        self.treeview.insert('',7,'item7', text = 'Vanilla Option')
        self.treeview.insert('',7,'item8', text = 'Hurdle')

        #returns trade id       
        def trade_id():
            global trade_id
            trade_id +=1
            return trade_id
        
        def booking_confirmation():
            global confirmation_window
            
            confirmation_window = Toplevel(master)
            confirmation_window.attributes("-topmost", True)

            if not self.entry0.get().strip() or not self.entry1.get().strip() or not self.spinbox0.get().strip():
                confirmation_window.title('Not Booked')
                self.label9 = ttk.Label(confirmation_window, text = 'Start Date, End Date and Notional fields are mandatory')
                self.label9.grid(row = 0, column = 0, pady = 5, padx = 5)
            else:
                master.state('withdrawn')
                confirmation_window.title('Confirmation')
                self.label10 = ttk.Label(confirmation_window, text = 'Trade Confirmation', font = ('Helvetica', 14, 'bold'))
                self.label10.grid(row = 0, column = 0, pady = 5, padx = 5)

                self.label11 = ttk.Label(confirmation_window, text = 'Template: ' + self.label0.cget('text'))
                self.label11.grid(row = 1, column = 0)

                self.label12 = ttk.Label(confirmation_window, text = 'Notional: ' + self.spinbox0.get())
                self.label12.grid(row = 2, column = 0)
            
                self.label13 = ttk.Label(confirmation_window, text = 'Trade ID: ' + str(trade_id()))
                self.label13.grid(row = 3, column = 0)

                self.button1 = ttk.Button(confirmation_window, text = 'OK', command = close_window)
                self.button1.grid(row = 4, column = 0, pady = 5)

                confirmation_window.protocol('WM_DELETE_WINDOW', close_window)

        def close_window():
            global confirmation_window
            global frame2
            confirmation_window.destroy()
            frame2.destroy()
            frame2 = ttk.Frame(self.panedwindow, width = 800, height = 300, relief = SUNKEN)
            self.panedwindow.add(frame2, weight = 1)
            master.state('normal')
        
        #adding entry widgets to frame2
        def widgets(template):
            global frame2
            self.executing_entity = StringVar()
            self.counterparty = StringVar()
            self.year = StringVar()
            #destroying the frame
            frame2.destroy()
            #defining frame2 and adding it to the panedwindow
            frame2 = ttk.Frame(self.panedwindow, width = 800, height = 300,
                        relief = SUNKEN)
            self.panedwindow.add(frame2, weight = 1)
            
            self.label0 = ttk.Label(frame2, text = template, style = 'TLabel', font = ('Helvetica', 14, 'bold'))
            self.label0.grid(row = 0, column = 2, pady = 5)

            self.label1 = ttk.Label(frame2, text = 'Start Date', style = 'TLabel')
            self.label1.grid(row = 1, column = 0, padx = 15, pady = 5)

            self.entry0 = ttk.Entry(frame2)
            self.entry0.grid(row = 1, column = 1, pady = 5)

            self.label2 = ttk.Label(frame2, text = 'End Date', style = 'TLabel')
            self.label2.grid(row = 1, column = 3, padx = 15, pady = 5)

            self.entry1 = ttk.Entry(frame2)
            self.entry1.grid(row = 1, column = 4, pady = 5)

            self.label3 = ttk.Label(frame2, text = 'Notional', style = 'TLabel')
            self.label3.grid(row = 2, column = 0, padx = 15, pady = 5)

            self.spinbox0 = Spinbox(frame2, textvariable = self.year)
            self.spinbox0.config(values = ('0', '1M', '2M', '3M', '4M', '5M',
                                           '6M', '7M', '8M', '9M', '10M'))
            self.spinbox0.grid(row = 2, column = 1, padx = 15, pady = 5)

            self.label4 = ttk.Label(frame2, text = 'Currency 1', style = 'TLabel')
            self.label4.grid(row = 3, column = 0, padx = 15, pady = 5)

            self.entry2 = ttk.Entry(frame2)
            self.entry2.grid(row = 3, column = 1, pady = 5)

            if template in ('Bond','Repo'):
                self.label5 = ttk.Label(frame2, text = 'Security', style = 'TLabel')
                self.label5.grid(row = 3, column = 3, padx = 15, pady = 5)

                self.entry3 = ttk.Entry(frame2)
                self.entry3.grid(row = 3, column = 4, pady = 5)

            if template not in ('Bond', 'Repo'):
                self.label6 = ttk.Label(frame2, text = 'Currency 2', style = 'TLabel')
                self.label6.grid(row = 3, column = 3, padx = 15, pady = 5)

                self.entry4 = ttk.Entry(frame2)
                self.entry4.grid(row = 3, column = 4, pady = 5)

            self.label7 = ttk.Label(frame2, text = 'Executing Entity', style = 'TLabel')
            self.label7.grid(row = 4, column = 0, padx = 15, pady = 5)

            self.combobox0 = ttk.Combobox(frame2, textvariable = self.executing_entity)
            self.combobox0.grid(row = 4, column = 1, pady = 5)
            self.combobox0.config(values = ('LOYD', 'LBCM', 'BOS', 'LBCW'))

            self.label8 = ttk.Label(frame2, text = 'Counterparty', style = 'TLabel')
            self.label8.grid(row = 4, column = 3, padx = 15, pady = 5)

            self.combobox1 = ttk.Combobox(frame2, textvariable = self.counterparty)
            self.combobox1.grid(row = 4, column = 4, pady = 5)
            self.combobox1.config(values = ('HSBC', 'Deutche', 'JaguarLandrover',
                                            'Morgan Stanely', 'JP Morgan', 'Citibank'))
            
            self.button0 = ttk.Button(frame2, text = 'Book', command = booking_confirmation)
            self.button0.grid(row = 6, column = 2, pady = 5)
            

        def callback(event):
            if self.treeview.focus() == 'item0':
                widgets('Swap')
            elif self.treeview.focus() == 'item1':
                widgets('Repo')
            elif self.treeview.focus() == 'item2':
                widgets('Bond')
            elif self.treeview.focus() == 'item3':
                widgets('Fra')
            elif self.treeview.focus() == 'item4':
                widgets('Swaption')
            elif self.treeview.focus() == 'item5':
                widgets('FX Swap')
            elif self.treeview.focus() == 'item6':
                widgets('NDF')
            elif self.treeview.focus() == 'item7':
                widgets('Vanilla Option')
            elif self.treeview.focus() == 'item8':
                widgets('Hurdle')
            
        #pressing widgets in the GUI
        self.treeview.bind('<<TreeviewSelect>>', callback)
        
def main():
    root = Tk()
    root.title('Booking Application')
    panedwindow = HkPanedWindow(root)
    menu = HkMenu(root)

if __name__ == '__main__':
    main()
