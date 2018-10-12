import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
from subprocess import Popen, PIPE
import linecache


 
##get diff
##TODO

##student file 
class studentFile:
	def __init__(self, ID, stuFile, grade):
		self.ID = ID
		self.stuFile = stuFile
		self.grade = grade
	def getFileName:
		return self.stuFile
	def setFileName(x):
		self.stuFile=x
	def getID:
		return self.ID
	def setID(x):
		self.ID=x
	def getGrade:
		return self.grade
	def setGrade(x):
		self.grade = x



#this function will get rid of spaces on both ends
#and it will also make every character a lowercase
#character so there is no mistake with that
def morphString(myString):
	myString = myString.lower()
	##this section gets rid of the spaces from the left to right 
	i=0
	while myString[i]==" ":
		myString=myString[(i+1)::]
		i=i+1

	##this section gets rid of the spaces from the right to the left
	i=len(myString)
	while myString[i]==" ":
		myString=myString[::(i-1)]
		i=i-1
	return myString

def readTextFile(myFile):
	#read the file here and then return what it is supposed to say
	#returns the list where the first element is the name of the 
	#file and the second element is the string of what the output 
	#should be 


	#returns ---> results = [name_of_file, expected_result]

	name_of_file = ""
	expected_result = ""

	fp = open(myFile, 'r') 
	name_of_file=fp.readline()
	with open(myFile) as fp:  
   		line = fp.readline()
   		while line:
   			expected_result = expected_result+line
       		line = fp.readline()
	fp.close()

	results= []
	results.append(name_of_file)
	results.append(expected_result)

	return results

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

# hide main window
def main():


	#this contains three different files, the program asks 
	#for the csv file, what the result should be text file
	#and also the folder with all the student files

	root = tkinter.Tk()
	Label(root, text="Enter Output File Name:").grid(row=0)
	e1 = Entry(root)
	e1.grid(row=0, column=1)

	#ask for the csv file 
	csv_file = filedialog.askopenfilename(initialdir = 
		"/",title = "Select csv file")
	#if nothing is selected, exit 
	pathException(csv_file)

	#here is the filename of the answer file 
	root.filename =  filedialog.askopenfilename(initialdir = 
		"/",title = "Select file",filetypes = (("py files","*.py"),("txt files","*.txt"),
			("jpeg files","*.jpg"),("all files","*.*")))
	#if nothing is selected, exit 
	pathException(root.filename)

	#get the folder
	folder = filedialog.askdirectory(title = "Student Submissions Folder")
	pathException(folder)
	pathlist = Path(folder).glob(("all files","*.*"))
	studentList = []


	##create a list of empty student files based on how many files there are 
	for i in len(pathlist):
		sampleFile = studentFile("0","empty",0)
		studentList.append(sampleFile)
	###


	hwName, output = readTextFile(root.filename)
	
	print("the filename is: "+hwName)
	print("and this file contains: ")
	print(output)

	##going to read throught the csv file here #####
	#name_of_file=fp.readline()
	with open(csv_file) as fp:  
   		line = fp.readline()
   		while line:
       		line = fp.readline()
	fp.close()




	##RUN THE ANSWER FILE & STORE OUTPUT HERE###
	justFileName = pathToFileName(root.filename)
	print(justFileName)
	sys.append(root.filename)
	process = Popen(['python3', justFileName], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
	ansOUT = stdout
	##ansOUT is what the output should be 
	########################	

	# message box display
main()