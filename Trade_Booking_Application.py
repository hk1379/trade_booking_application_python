#
#Trading Platform
#

from tkinter import *
from tkinter import ttk

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
        #creating a paned window
        self.panedwindow = ttk.Panedwindow(master, orient = HORIZONTAL, width = 1000)
        
        #ensuring the paned window expands when the window size is increased
        self.panedwindow.pack(fill = BOTH, expand = True)
      
        #defining frame1
        global self.frame1
        global self.frame2
        global self.frame3
        global self.frame4
        global self.frame5
        self.frame1 = ttk.Frame(self.panedwindow, width = 400, height = 300,
                           relief = SUNKEN)
        self.frame2 = None
        self.frame3 = None
        self.frame4 = None
        self.frame5 = None
        
        #defining frame2
        #self.frame2 = ttk.Frame(self.panedwindow, width = 800, height = 300,
        #                   relief = SUNKEN)
        
        #adding notebooks to panedwindow
        #weight defines how quickly one frame expands relative to the window size increasing
##        self.notebook = ttk.Notebook(self.panedwindow)
##        self.panedwindow.add(self.notebook, weight = 0)
##        self.notebook.add(self.frame0, text = 'FX')
##        self.notebook.add(self.frame1, text = 'Non FX')
        
        #adding the frames to the panedwindows
        self.panedwindow.add(self.frame1, weight = 0)
        #self.panedwindow.add(self.frame2, weight = 1)
        
        #adding treeview to the frame
        self.treeview = ttk.Treeview(self.frame1)
        self.treeview.pack(fill = BOTH, expand = True)
        self.treeview.heading('#0', text = 'Template')
        #insert method (first parameter = the parent node of item being created)
        #root node has special name which is an empty string
        #second paramaeter = position of the node you want to add
        #third character = choose name of item being added
        self.treeview.insert('',0,'item0', text = 'Swap')
        self.treeview.insert('',1,'item1', text = 'FX Swap')
        self.treeview.insert('',2,'item2', text = 'Bond')
        self.treeview.insert('',3,'item3', text = 'Fra')

        #adding entry widgets to frame2
        def widgets(template, frame, frame_object):
            #destroying frame if it exists
            if frame_object is None:
                #defining frame2 and adding it to the panedwindow
                self.frame = ttk.Frame(self.panedwindow, width = 800, height = 300,
                           relief = SUNKEN)
                self.panedwindow.add(self.frame, weight = 1)
            
                self.label0 = ttk.Label(self.frame, text = template, style = 'TLabel')
                self.label0.grid(row = 0, column = 2, pady = 5)

                self.label1 = ttk.Label(self.frame, text = 'Start Date', style = 'TLabel')
                self.label1.grid(row = 1, column = 0, padx = 15, pady = 5)

                self.entry0 = ttk.Entry(self.frame)
                self.entry0.grid(row = 1, column = 1, pady = 5)

                self.label2 = ttk.Label(self.frame, text = 'End Date', style = 'TLabel')
                self.label2.grid(row = 1, column = 3, padx = 15, pady = 5)

                self.entry1 = ttk.Entry(self.frame)
                self.entry1.grid(row = 1, column = 4, pady = 5)

                self.label3 = ttk.Label(self.frame, text = 'Notional', style = 'TLabel')
                self.label3.grid(row = 2, column = 0, padx = 15, pady = 5)

                self.entry2 = ttk.Entry(self.frame)
                self.entry2.grid(row = 2, column = 1, pady = 5)

                self.label4 = ttk.Label(self.frame, text = 'Currency 1', style = 'TLabel')
                self.label4.grid(row = 3, column = 0, padx = 15, pady = 5)

                self.entry3 = ttk.Entry(self.frame)
                self.entry3.grid(row = 3, column = 1, pady = 5)

                self.label5 = ttk.Label(self.frame, text = 'Currency 2', style = 'TLabel')
                self.label5.grid(row = 3, column = 3, padx = 15, pady = 5)

                self.entry4 = ttk.Entry(self.frame)
                self.entry4.grid(row = 3, column = 4, pady = 5)

                self.button0 = ttk.Button(self.frame, text = 'Book')
                self.button0.grid(row = 4, column = 2, pady = 5)
            else:
            #frame_object.destroy()
                print('success')

        def callback(event):
            if self.treeview.focus() == 'item0':
                widgets('Swap', 'frame2', self.frame2)
            elif self.treeview.focus() == 'item1':
                widgets('FX Swap', 'frame3', self.frame3)
            elif self.treeview.focus() == 'item2':
                widgets('Bond', 'frame4', self.frame4)
            elif self.treeview.focus() == 'item3':
                widgets('Fra', 'frame5', self.frame5)
            
        #pressing widgets in the GUI
        self.treeview.bind('<<TreeviewSelect>>', callback)
        
def main():
    root = Tk()
    root.title('Booking Application')
    panedwindow = HkPanedWindow(root)
    menu = HkMenu(root)

if __name__ == '__main__':
    main()
