from datetime import datetime, timedelta
import xlrd
import pandas as pd
import numpy as np

File = pd.read_csv("DueDates.csv")
class DataTime:
    def __init__(self,File=File):
        self.File=File
        self.BuildFrames()
        self._ConvertToArray()
        self.WindowsAnalyze()
        self.NetAnalyze()
        self._CountDown()
       
        
       
    def BuildFrames(self):
        OsysDateTimes = self.File[["Osys","OsysTime"]].copy()
        df = self.File[["Networking","NetTime"]].copy()
        Networking = df.dropna()
        self.NetDataFrame = Networking.sort_values(by="NetTime",ascending=True)
        self.OsysDataFrame = OsysDateTimes.sort_values(by="OsysTime",ascending=True)

    def _CountDown(self):
        Count = self.PythonDate - datetime.now()
        self.Days = Count.days
        self.Hours = Count.seconds/3600
        self.Mins = (self.Hours*60)%60
        return Count
        

    def _ConvertToArray(self):
        Windows = self.OsysDataFrame
        Networking = self.NetDataFrame
        self.WinArray = Windows.to_numpy()
        self.NetArray = Networking.to_numpy()

    def WindowsAnalyze(self):
        WindowsList = []
        for row in self.WinArray:
            ExcelTime = float(row[1])
            self.PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
            if self._CountDown() >timedelta(days=14):
                break
            elif self.PythonDate > datetime.now():
                WindowsList.append(f'{row[0]} for Windows Admin is due at {self.PythonDate} or in {self.Days} days,'
                                   f'{int(self.Hours)} hours and, {int(self.Mins)} minutes')
        return WindowsList    
    
               
            
    def NetAnalyze(self):
        NetList = []
        for row in self.NetArray:
            ExcelTime = float(row[1])
            self.PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
            if self._CountDown() >timedelta(days=14):
                break
            elif self.PythonDate > datetime.now():
                NetList.append(f'{row[0]} for Networking is due at {self.PythonDate} or in {self.Days} days,'
                               f'{int(self.Hours)} hours and, {int(self.Mins)} minutes')
        return NetList    
    
       



def main():
    print(f'Upcoming Due Dates:')
    print(f'------------------------------')
    for i in DataTime().NetAnalyze():
        print(i)
    print(f'------------------------------')
    for i in DataTime().WindowsAnalyze():
        print(i)
    
    


if __name__ == "__main__":
    main()