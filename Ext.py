        '''self.topFrame = Frame(window,width = 100)
        self.topFrame.place(x = 0, y = 0)
        self.viewFrame = Frame(window,width = 30,height = 20)
        self.viewFrame.place(x = 0,y = 50)
        self.butFrame = Frame(window,width = )
        self.Tlabel = Label(self.topFrame,text = 'Title',width = 10,height = 1)
        self.TEntry = Entry(self.topFrame)
        self.Alabel = Label(self.topFrame,text = 'Author',width = 10,height = 1)
        self.AEntry = Entry(self.topFrame)
        self.Ylabel = Label(self.topFrame,text = 'Year',width = 10,height = 1)
        self.YEntry = Entry(self.topFrame)
        self.Ilabel = Label(self.topFrame,text = 'ISBN',width = 10,height = 1)
        self.IEntry = Entry(self.topFrame)
        '''
        
                # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)
