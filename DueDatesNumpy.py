from datetime import datetime, timedelta
import xlrd
import tkinter as tk
import pandas as pd
import numpy as np

File = pd.read_csv("DueDates.csv")
class DataTime():
    def __init__(self,File=File):
        self.File=File
        self.BuildFrames()
        self._ConvertToArray()
        self.WindowsAnalyze()
       
        self._CountDown()
       
    def BuildFrames(self):
        OsysDateTimes = self.File[["Osys","OsysTime"]].copy()
        df = self.File[["Networking","NetTime"]].copy()
        Networking = df.dropna()
        self.NetDataFrame = Networking.sort_values(by="NetTime",ascending=True)
        self.OsysDataFrame = OsysDateTimes.sort_values(by="OsysTime",ascending=True)
    
    def _CountDown(self):
        count = self.PythonDate - datetime.now()
        return count

    def _ConvertToArray(self):
        Windows = self.OsysDataFrame
        Networking = self.NetDataFrame
        self.WinArray = Windows.to_numpy()
        self.NetArray = Networking.to_numpy()

    def WindowsAnalyze(self):
        for row in self.WinArray:
            ExcelTime = float(row[1])
            self.PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
            if self._CountDown() > timedelta(days=14):
                break
            if self.PythonDate < datetime.now():
                pass
            else:
                print(f'The next assignment for Windows Admin is:\n')
                print(f'{row[0]} is due at {self.PythonDate} or in {self._CountDown()}')
            
    def NetAnalyze(self):
        for row in self.NetArray:
            ExcelTime = float(row[1])
            self.PythonDate = datetime(*xlrd.xldate_as_tuple(ExcelTime, 0))
            if self._CountDown() > timedelta(days=14):
                break
            if self.PythonDate < datetime.now():
                pass
            else:
                print(f'The next assignment for Networking is:\n')
                print(f'{row[0]} is due at {self.PythonDate} or in {self._CountDown()}')



def main():
    Frames = DataTime()
    Frames.WindowsAnalyze()

if __name__ == "__main__":
    main()