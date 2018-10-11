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
	root = tkinter.Tk()
	Label(root, text="Enter Output File Name:").grid(row=0)
	e1 = Entry(root)
	e1.grid(row=0, column=1)
	#root.withdraw()
	csv_file = filedialog.askopenfilename(initialdir = 
		"/",title = "Select csv file")

	root.filename =  filedialog.askopenfilename(initialdir = 
		"/",title = "Select file",filetypes = (("py files","*.py"),("txt files","*.txt"),
			("jpeg files","*.jpg"),("all files","*.*")))
	pathException(root.filename)


	##RUN THE ANSWER FILE & STORE OUTPUT HERE###
	justFileName = pathToFileName(root.filename)
	print(justFileName)
	sys.append(root.filename)
	process = Popen(['python3', justFileName], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
	ansOUT = stdout
	##ansOUT is what the output should be 
	########################




	##need to search the csv file###
	###need to search for 
	studentIDS = []

	####here get students IDSfrom csv file######
	
	key = '"en";"'
	print("the key is: "+key)
	i=2
	while getLINE = linecache.getline(csv_file, i):
		strt = getLINE.find(key)
		strt = strt + len(key)
		ID = " "
		while getLine[strt]!='"':
			ID = ID+getLine[strt]
		studentIDS.append(ID)
		i++

	####///////////////////////////////////////////////######

	##get the time stamp for the csv file 
	


	folder = filedialog.askdirectory(title = "All Student Submissions For This HW")
	pathException(folder)
	pathlist = Path(folder).glob('**/*.py')

	#ID is the student's identification number#

	##traverse through all the students solutions in the folder
	for path in pathlist:
		if path == ID:
			print("student found!")
		studentString = str(path) #this is the filename of the student
		studentOutput = ""
		##RUN THE STUDENT FILE & STORE OUTPUT HERE###

		########################
		errors = returnDifferences(studentOutput, root.filename)
		

	# message box display
main()