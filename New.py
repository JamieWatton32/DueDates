from datetime import datetime
import xlrd
import tkinter as tk
import pandas as pd
import numpy as np

def main():
   File = pd.read_csv("DueDates.csv")
   CleanedFile = File.dropna()
   Data = CleanedFile.to_numpy()
   Rows = Data.shape[0]
   Cols = Data.shape[1]
   Data = pd.DataFrame()
   for x in range(0,Rows):
      for y in range(0,Cols):
        if type(Data[x,y]) == float:
         pass

           


if __name__ == "__main__":
   main()