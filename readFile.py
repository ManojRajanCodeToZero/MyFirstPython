import os, sys
import hashlib


def main():
	#f = open(r"C:\Users\1599212\Documents\Study\Python\TestData\sampleData.txt","r")
	#if f.mode == "r":
		#content = f.read()
		#print(content)
		
		# To read line by line
		#f1 = f.readlines()
		#for x in f1:
			#for 
			#print(x)
	for allDirPath,subdirs,fileList in os.walk(r"C:\Users\1599212\Documents\Study"):
		print("Directory Path : ", allDirPath)
		#for subFolder in subdirs:
		#	print("Sub Folder : ", subFolder)
		for fileName in fileList:
			print("File Name : ", fileName)
			path = os.path.join(allDirPath, fileName)
			hasher = hashlib.md5()
			print(hasher)
			print("File Path and Name : ",path)
	
	
if __name__=="__main__":
	main()
