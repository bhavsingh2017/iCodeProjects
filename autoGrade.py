import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
from tkinter import Button
from subprocess import call
from subprocess import check_output
import os
import linecache
import sys
from pathlib import Path
import difflib
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def runFile(string, directoryFileList):
	if string in directoryFileList==False:
		return "Incorrect File Name"
	out = check_output(["python3", string])
	return out

def noSpacesNoQuote(stringx):
	for i in range(0, len(stringx)):
		if(stringx[i]==" " or stringx[i]=="'" or stringx[i]=='"'):
			stringx = stringx[i+1::]
		else:
			break
	for i in range(len(stringx), 0):
		if(stringx[i]==" "):
			stringx = stringx[::i-1]
		else:
			break
	return stringx

def findFile(fileKey, directory):

	for path in directory:
		numCompare = path[6]+path[7]
		if(len(fileKey))>2:
			numCompare=path[6]+path[7]+path[8]
		if(numCompare==fileKey):
			return path

	return -1

def grade(string1, string2):
	string1 = string1.lower()
	string2 = string2.lower()
	string1 = noSpacesNoQuote(string1)
	string2 = noSpacesNoQuote(string2)
	string1 = str(string1)
	string2 = str(string2)

	sim = similar(string1, string2)
	print("String1: "+string1)
	print("String2: "+string2)
	print("SIMILARITY RATIO: "+str(sim))
	return sim

def pathException(path):
	if path!="":
		print("you picked: "+path)
	else:
		print("Exited, please pick a location")
	return
#returns just the fileName & not the path
def pathToFileName(name):
	new_name=""
	i = len(name)-1
	while name[i]!="/":
		new_name=new_name+name[i]
		i=i-1
	##reverse the string
	return new_name[::-1]

def errorWindow(string):
	messagebox.showerror('User Error', string)
	return

# hide main window
def main():

	#Filetypes
	ftypes = [
    	('Python code files', '*.py'), 
    	('Perl code files', '*.pl;*.pm'),  # semicolon trick
    	('Java code files', '*.java'), 
    	('C++ code files', '*.cpp;*.h'),   # semicolon trick
    	('Text files', '*.txt'), 
    	('Excel files', '*.csv'),
    	('All files', '*'), 
	]

	root = tkinter.Tk()
	if(len(sys.argv)!=2):
		print("Invalid Number of Arguments")
		return
	outputName = str(sys.argv[1])+".txt"
	print("The output file is: "+outputName)

	root.withdraw()

	x = input("Select csv_file--->Press Enter to Continue")
	
	csv_file = filedialog.askopenfilename(title = "Ask for csv file", filetypes=ftypes)
	pathException(csv_file)
	
	x = input("Select Answer File--->Press Enter to Continue")
	root.filename =  filedialog.askopenfilename(initialdir = 
		"/",title = "Select Answer File",filetypes = ftypes)
	pathException(root.filename)

	if csv_file=="" or root.filename=="":
		errorWindow("Chosen file error, exiting...")
		return
	f = open(outputName,"w+")


	######----------------------Traverse Answer File----------------------######

	answer = open(root.filename, "r")
	expectedFileName = linecache.getline(root.filename, 1)
	expectedFileName=expectedFileName.rstrip('\n')
	expectedOutput =""

	indice = 2
	getLineAnswer = linecache.getline(root.filename, indice)
	while getLineAnswer:
		expectedOutput =expectedOutput+getLineAnswer
		indice=indice+1
		getLineAnswer= linecache.getline(root.filename, indice)

	print(expectedFileName)
	print(expectedOutput)

	answer.close()

	x = input("Select Student File Folder--->Press Enter to Continue")
	folder = filedialog.askdirectory(title = "All Student Submissions For This HW")
	pathException(folder)
	pathlist = Path(folder).glob('**/*.py')


	######----------------------Traverse CSV File----------------------######


	#This loop will ignore the file if the submission number is blank*
	#This loop will add the student to be checked only if they submitted a .py file

	notPyFile=[]
	studentIDS = []  #refers to the user id
	studentSubmissionNumber = [] #refers to the student submission number 
	key = '"en";"' #this is the part that has the ID
	getZero = '"ext"":""py"'
	print("the key is: "+key) 
	i=2
	getLine = linecache.getline(csv_file, i)
	while getLine: #read in all lines
		#print(getLine)
		strt = getLine.find(key) #find the key 

		studentGetsZero = False
		if getLine.find(getZero)==-1: 
			studentGetsZero=True

		strt = strt+len(key)
		number = ""
		ID = ""
		while getLine[strt]!='"':
			ID = ID+getLine[strt]
			strt=strt+1
		strt=1
		while getLine[strt]!='"':
			number = number+getLine[strt]
			strt=strt+1

		if(studentGetsZero):
			notPyFile.append(ID)
			print("Added "+ID+" to pyList*********************************************")
			print("Student_ID:"+ID)
			print("Submission:"+number)
		if(((ID!="" and ID!=";" and ID!=" " and ID!="  ") and studentGetsZero==False)):
			studentIDS.append(ID)
			studentSubmissionNumber.append(number)
			print("Student_ID:"+ID)
			print("Length:"+str(len(ID)))
			print("Submission:"+number)
		i=i+1
		getLine = linecache.getline(csv_file, i)
		print()
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print()


	######----------------------Traverse CSV File----------------------######

	######----------------------Now do the grading----------------------######

	#if another correct submission was not for the same student then
	#print that the student gets a zero in the output file
	print("These many students didn't submit .py files: "+str(len(notPyFile)))
	index = 0

	while index<len(notPyFile):
		if (notPyFile[index] in studentIDS)==False:
			f.write("User: "+notPyFile[index]+" gets a 0%\n")
		index=index+1
	#empty this list, we don't need it anymore
	notPyFile[:] = []

	######----------------------Now do the grading----------------------######


	print("Submission list size: "+str(len(studentSubmissionNumber)))
	print("Student_ID list size: "+str(len(studentIDS)))
	print(expectedFileName)
	runFileName=""
	sys.path.append(folder)
	print("appending to--> "+folder)

	files = os.listdir(folder)

	for i in range(0, len(files)):
		print(files[i])

	mypath = Path().absolute()
	print("mypath"+str(mypath))
	sys.path.append(os.path.join(os.path.dirname(folder), ".."))
	os.path.abspath(folder)

	for i in range(0, len(studentSubmissionNumber)):
		print(i) 
		if (int(studentSubmissionNumber[i])<10): #submission is less than ten
			#runFileName = "0000"+studentSubmissionNumber[i]+"_0"+studentSubmissionNumber[i]+"_00-"
			#runFileName=runFileName+expectedFileName
			fileSubmission = "0"+studentSubmissionNumber[i]
			runFileName=findFile(fileSubmission, files)
			if(runFileName==-1):
				continue
			print("File to Run: "+runFileName)
		if (int(studentSubmissionNumber[i])<=99 and (int(studentSubmissionNumber[i])>=10)): #10-99
			#runFileName = "000"+studentSubmissionNumber[i]+"_"+studentSubmissionNumber[i]+"_00-"
			#runFileName=runFileName+expectedFileName
			fileSubmission = studentSubmissionNumber[i]
			runFileName=findFile(fileSubmission, files)
			if(runFileName==-1):
				continue
			print("File to Run: "+runFileName)
		if (int(studentSubmissionNumber[i])<=999 and (int(studentSubmissionNumber[i])>=100)): #100-999
			#do something here
			#runFileName = "00"+studentSubmissionNumber[i]+"_"+studentSubmissionNumber[i]+"_00-"
			#runFileName=runFileName+expectedFileName
			fileSubmission = studentSubmissionNumber[i]
			runFileName=findFile(fileSubmission, files)
			if(runFileName==-1):
				continue
			print("File to Run: "+runFileName)

		exists = runFileName in files
		runFileName=folder+"/"+runFileName
		if exists == False:
			print(studentIDS[i]+" has wrong filename gets 0%")
			f.write("User: "+studentIDS[i]+" gets a 0%\n")
			continue
		outputFromFile=""
		if exists == True:
			try:
				outputFromFile = runFile(runFileName, files)
				print("Running "+runFileName)
				print("Output: "+str(outputFromFile))
			except:
				print(studentIDS[i]+" has wrong syntax gets 0%")
				f.write("User: "+studentIDS[i]+" gets a 0%\n")
		grade1 = grade(outputFromFile, expectedOutput)
		grade1 =round(grade1,2)
		certainRatio = .023
		gradeString = str((grade1+certainRatio)*100)+"%"
		print(gradeString)
		f.write("User: "+studentIDS[i]+" gets a "+gradeString+"%\n")
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		
		
	f.close()
	#what I have left is to read the right directory
	#get the grades 

main()
