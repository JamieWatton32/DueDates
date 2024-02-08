from tkinter import *
Root=Tk()
# add widgets here
Root.title('Hello Python')
RootFrame=Frame(Root,width=500,height=500,bg='green')
RootFrame.pack()
OsysButton=Button(RootFrame,text='OSYS')
OsysButton.pack(side='bottom')
NetworkingButton = Button(RootFrame,text='Networking')
NetworkingButton.pack(side='bottom')
  def CreateFrame(self):
   
      DisplayFrame = Frame(master=self)
      DisplayFrame.pack()
       

   def Networking(self):
      CsvReader = csv.DictReader(self.File)
      for row in CsvReader:
         if row["NetTime"] == "":
            break 
         ExcelTime = float(row["NetTime"])
         PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
         if PythonDate < datetime.now():
           return PythonDate
         
         
   def WindowsAdmin(self):
         CsvReader = csv.DictReader(self.File)
         for row in CsvReader:
            ExcelTime = float(row["OsysTime"])
            PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
            if PythonDate < datetime.now():
               return PythonDate