import pandas as pd
import glob

filesPath = input("Enter the set of files path: ")


all_Data = pd.DataFrame()
for f in glob.glob(filesPath):
    df = pd.read_excel(f)
    all_Data = all_Data.append(df,ignore_index=True)
    
    
        
writeToFilePath = input("Enter the File Name pattern's with path to write to the data frame: ")
writer = pd.ExcelWriter(writeToFilePath)
all_Data.to_excel(writer,"ConsolidatedSheet")
writer.save()

print("Data Frame saved in to the Location : "+writeToFilePath)
