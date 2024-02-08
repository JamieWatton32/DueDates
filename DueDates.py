from datetime import datetime
import csv
import xlrd
import tkinter as tk
import requests
from bs4 import BeautifulSoup
#Setting Website URL to var
url = 'https://nscconline.brightspace.com/d2l/lms/quizzing/user/quizzes_list.d2l?ou=299885'

Data = requests.get(url)

Soup = BeautifulSoup(Data.content,"html.parser")

with open("BooksToScrape.txt", "w") as MyFile:
    MyFile.write(Soup.prettify())



def CountDown(PythonTime):
   count = PythonTime - datetime.now()
   return count

def Networking():
   File = open("DueDates.csv","r")
   CsvReader = csv.DictReader(File)
   for row in CsvReader:
      if row["NetTime"] == "":
         break 
      ExcelTime = float(row["NetTime"])
      PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
      if PythonDate < datetime.now() + 4:
         pass
      else:
          print(f'The next assignment for Networking is:\n')
          print(f'{row["Networking"]} is due at {PythonDate} or in {CountDown(PythonDate)}')
          break
        

def WindowsAdmin():
      File = open("DueDates.csv","r")
      CsvReader = csv.DictReader(File)
      for row in CsvReader:
         ExcelTime = float(row["OsysTime"])
         PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
         if PythonDate < datetime.now():
            pass
         else:
            print(f'The next assignment for Windows Admin is:\n')
            print(f'{row["Osys"]} is due at {PythonDate} or in {CountDown(PythonDate)}')
            
            break


def main():

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