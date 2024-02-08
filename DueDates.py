from datetime import datetime
import csv
import xlrd

def CountDown(PythonTime):
   count = PythonTime - datetime.now()
   return count

def Networking(CsvFile):
   CsvReader = csv.DictReader(CsvFile)
   for row in CsvReader:
      if row["NetTime"] == "":
         break 
      ExcelTime = float(row["NetTime"])
      PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
      if PythonDate < datetime.now():
         pass
      else:
          print(f'{row["Networking"]} is due at {PythonDate} or in {CountDown(PythonDate)}')
          break
        

   
def WindowsAdmin(CsvFile):
      CsvReader = csv.DictReader(CsvFile)
      for row in CsvReader:
         ExcelTime = float(row["OsysTime"])
         PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
         if PythonDate < datetime.now():
            pass
         else:
            print(f'{row["Networking"]} is due at {PythonDate} or in {CountDown(PythonDate)}')
            break


def main():
   File = open("DueDates/DueDates.csv","r")
   ClassName = input("Osys or Networking?").lower()
   
   if ClassName == "Networking":
      Networking(File)
   if ClassName == "Osys":
      WindowsAdmin(File)


if __name__ == "__main__":
   main()