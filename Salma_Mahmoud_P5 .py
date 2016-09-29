#------------------------------------------------------------------------------
#Student Name: Salma Mahmoud / Assignment: P#3 / Date: 10/05/2012
#------------------------------------------------------------------------------
#Honor Code Statemant: I receivied no assistance on this assignment that 
#violates the ethical guidelines set fourth by professor and class syllabus
#------------------------------------------------------------------------------
#References: Class powerpoints, Python textbook, tutoring
#------------------------------------------------------------------------------
#Comments: N/A
#------------------------------------------------------------------------------
#Pseudocode: 
#BEGIN
#	print 1 - Open Address Book
#	print 2 - Add Entry
#	print 3 - Remove Entry
#	print 4 - Store Address Book
#	print 5 - View Address Book By Name, Alphabetically
#	print 6 - View Address Book By Email, Alphabetically
#	print 7 - Search Email Adresses
#	print 8 - Search Names
#	print 9 - Search Names and Email
#	print 10 - Quit
#	option=integer input Choose an option: 
#	choose=True
#	while choose:
#		if option=1
#			def function
#				dictionary={}
#				add_book=input 'Enter file name: '
#				file=open(add_book, "rU")
#				file.reading()
#				list=[]
#				for x in file.readlines()
#					list.append x
#				for (x,y) in list
#					dictionary[email]=name
#		elif option==2:
#			def function2:
#				function1
#				dictionary={}
#				name=input("Enter Name: ")
#				email=input("Enter Email: ")
#				dictionary[email]=name
#		elif option==3:
#			def function3:
#				funtion1
#				name=input 'Enter Name: '
#				email=input 'Enter Email: '
#				delete dictionary[email]=name
#		elif option=4
#			function1
#				add_book=input("Enter file name: ")
#				file=open(add_book, "a+U")
#				file.close()
#		elif option=5
#			def function5
#				function1()
#				for x in sorted dictionary.values()
#					print x
#		elif option=6
#			def function6
#				funtion1()
#				for x in sorted dictionary.keys()
#					print x
#		elif option=7
#			def function7 
#				funtion1()
#				email=input 'Enter email: '
#				if email in list dictionary.keys()
#					print 'dictionary[email]'
#				else:
#					print 'Invalid entry. Try again'
#		elif option=8
#			def function8
#				funtion1()
#				name=input 'Enter name: ' 
#				for x in range length list dictionary.values()
#					if name = list(dictionary.values)[x]
#						print 'list dictionay.keys()[x]'
#		elif option=9
#			def funtion9
#				function1()
#				email=input 'Enter email: '
#				name=input 'Enter name: '
#				if email in list(dictionary.keys()):
#					print(dictionary[email])
#				else:
#					print("Invalid entry. Try again")
#				for x in range(len(list(dictionary.values()))):
#					if name == list(dictionary.values)[x]:
#						print(list(dictionay.keys()[x]))
#		elif option=10
#			break
#		else
#			print "Invalid input. Please try again!"
#			option=int(input("Enter option: "))
#END
#------------------------------------------------------------------------------

print("1 - Open Address Book")
print("2 - Add Entry")
print("3 - Remove Entry")
print("4 - Store Address Book")
print("5 - View Address Book By Name, Alphabetically")
print("6 - View Address Book By Email, Alphabetically")
print("7 - Search Email Adresses")
print("8 - Search Names")
print("9 - Search Names and Email")
print("10 - Quit")
option=int(input("Choose an option: "))
choose=True
while choose:
	if option==1:
		def function1:
			dictionary={}
			add_book=input("Enter file name: ")
			file=open(add_book, "rU")
			file.reading()
			list=[]
			for x in file.readlines():
				list.append(x)
			for (x,y) in list:
				dictionary[email]=name
			return fuction1
	elif option==2:
		def function2:
			function1()
			dictionary={}
			name=input("Enter Name: ")
			email=input("Enter Email: ")
			dictionary[email]=name
			return function2
	elif option==3:
		def function3:
			funtion1()
			name=input("Enter Name: ")
			email=input("Enter Email: ")
			del.dictionary[email]=name
			return function3
	elif option==4:
		function1
		add_book=input("Enter file name: ")
		file=open(add_book, "a+U")
		file.close()
		return function4
	elif option==5:
		def function5:
			function1()
			for x in sorted(dictionary.values()):
				print(x)
			return function5
	elif option==6:
		def function6:
			funtion1()
			for x in sorted(dictionary.keys()):
				print(x)
			return function6
	elif option==7:
		def function7:
			funtion1()
			email=input("Enter email: ")
			if email in list(dictionary.keys()):
				print(dictionary[email])
			else:
				print("Invalid entry. Try again")
			return function7
	elif option==8:
		def function8:
			funtion1()
			name=input("Enter name: ")
			for x in range(len(list(dictionary.values()))):
				if name == list(dictionary.values)[x]:
					print(list(dictionay.keys()[x]))
			return function8
	elif option==9:
		def funtion9:
			function1()
			email=input("Enter email: ")
			name=input("Enter name: ")
			if  email in list(dictionary.keys()):
				print(dictionary[email])
			else:
				print("Invalid entry. Try again")
			for x in range(len(list(dictionary.values()))):
				if name == list(dictionary.values)[x]:
					print(list(dictionay.keys()[x]))
			return function9
	elif option==10:
		break
	else:
		print("Invalid input. Please try again!")
		option=int(input("Enter option: "))