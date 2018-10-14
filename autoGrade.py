import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
from tkinter import Button
from subprocess import Popen, PIPE
import linecache
import sys
	           

def runFile(string, directoryAppend):
	sys.append(directoryAppend)
	process = Popen(['python3', string], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate() 

def returnDifferences(studentFile, asnwerFile):
	return 1
def getGrade(errors, answer):
	charCount = len(answer)
	if(errors >= charCount):
		return 0
	else:
		return 100
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
	sys.append(folder)
	print("appending to--> "+folder)
	for i in range(0, len(studentSubmissionNumber)):
		print(i)
		if (int(studentSubmissionNumber[i])<10): #submission is less than ten
			runFileName = "0000"+studentSubmissionNumber[i]+"_0"+studentSubmissionNumber[i]+"_00-"
			runFileName=runFileName+expectedFileName
			print("File to Run: "+runFileName)

		if (int(studentSubmissionNumber[i])<=99 and (int(studentSubmissionNumber[i])>=10)): #10-99
			runFileName = "000"+studentSubmissionNumber[i]+"_"+studentSubmissionNumber[i]+"_00-"
			runFileName=runFileName+expectedFileName
			print("File to Run: "+runFileName)
		if (int(studentSubmissionNumber[i])<=999 and (int(studentSubmissionNumber[i])>=100)): #100-999
			#do something here
			runFileName = "00"+studentSubmissionNumber[i]+"_"+studentSubmissionNumber[i]+"_00-"
			runFileName=runFileName+expectedFileName
			print("File to Run: "+runFileName)
	f.close()




	##traverse through all the students solutions in the folder
	# for path in pathlist:
	# 	if path == ID:
	# 		print("student found!")
	# 	studentString = str(path) #this is the filename of the student
	# 	studentOutput = ""
	# 	##RUN THE STUDENT FILE & STORE OUTPUT HERE###

	# 	########################
	# 	errors = returnDifferences(studentOutput, root.filename)
		

	# message box display
main()
