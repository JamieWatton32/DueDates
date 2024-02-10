from datetime import datetime
import csv
import xlrd
import tkinter as tk
import pandas as pd


def CountDown(PythonTime):
   count = PythonTime - datetime.now()
   return count

def Networking():
   File = pd.read_csv("DueDates.csv")
   CsvReader = pd.DataFrame.to_dict(File)
   for row in CsvReader:
      if row["NetTime"] == "":
         break 
      ExcelTime = float(row["NetTime"])
      PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
      if PythonDate < datetime.now():
         pass
      else:
          print(f'The next assignment for Networking is:\n')
          print(f'{row["Networking"]} is due at {PythonDate} or in {CountDown(PythonDate)}')
          break
        

def WindowsAdmin():
      File = pd.read_csv("DueDates.csv")
      CsvReader = pd.DataFrame.to_dict(File)
      for row in CsvReader:
         ExcelTime = float(row[1])
         PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
         if PythonDate < datetime.now():
            pass
         else:
            print(f'The next assignment for Windows Admin is:\n')
            print(f'{row["Networking"]} is due at {PythonDate} or in {CountDown(PythonDate)}')
            break


def main():
   File = pd.read_csv("DueDates.csv")
   CsvReader = pd.DataFrame.to_dict(File)
   print(CsvReader)
   root = tk.Tk()
   entry = tk.Entry(root)
   entry.pack()

   button1 = tk.Button(root, text="Osys", command=WindowsAdmin)
   button2 = tk.Button(root, text="Networking", command=Networking)
 
   button1.pack()
   button2.pack()


   root.mainloop()
   
if __name__ == "__main__":
   main()