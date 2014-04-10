#------------------------------
# functions and definitions
#------------------------------

import os

phone_book ={} #dictonary containing your phonbook

def cleer_screen(confirm=True): # function to clear screen between menu selections
	if confirm == True: # do i want the user to press enter before clearing or not defaulted to true
		spacer()
		cont = raw_input("press enter to continue")
	os.system('cls' if os.name == 'nt' else 'clear')

def spacer(): # just adding 2 lines of nothing :)
	print " "
	print " "

def print_menu(): # print ouy main menu
	spacer()
	print " #############################################"
	print " #     phone book v0.1                       #"
	print " #############################################"
	print " # 1. add Person/number                      #"
	print " # 2. del Person/number                      #"
	print " # 3. find number                            #"
	print " # 4. List all numbers                       #"
	print " # s. Save phone book                        #"
	print " # l. Load phone book                        #"
	print " # q  Quit                                   #"
	print " #############################################"
	spacer()

def add_number(): # add number to phone_book var
	spacer()
	name = 	raw_input("enter name: ")
	number = raw_input("enter number: ")
	phone_book[name] = number
	cleer_screen(False)

def del_number(): # del a entry from the phonebook
	spacer()
	name = raw_input("enter name to delete: ")
	print "are you sure you want to delete " + name 
	yesno = raw_input("y/n: ")
	if yesno == "y" or yesno == "Y": # just a safty to make sure you want do del the name you entered
		try: # had to put this in a try except so the program would not crash if user enter a name thats not in the book 
			print "deleting " + name + " - " + phone_book[name] 
			del phone_book[name]
		except:
			print "name not found"
	cleer_screen()

def find_number(): # find a number by name 
	spacer()
	name = raw_input("enter name: ")
	try: # had to use try exept in case some one enters a name thats not in the dictonary
		print name + " " + phone_book[name]
		cleer_screen()
	except :
		print "that name is not in the phone book"
		cleer_screen()

def list_numbers(): # list all names and numbers in the phone book
	spacer()
	print "number -  name"
	for x,y in enumerate(sorted(phone_book)):
		print  phone_book[y] + " - " + y
	cleer_screen()

def save_book(): #save the array to a file
	file = open('phone-book.dat' , 'w+')
	for (id, item) in phone_book.items():
		#print id, item
		file.write(str(id) + '-' + str(item) + '\n')
		
def load_book(): #open the phone-book.dat
	try:
		file = open('phone-book.dat' , 'r+')
		for line in file:
			tmpInput = line.split('-')
			tmpInput2 = tmpInput[1].split()
			phone_book[tmpInput[0]] = tmpInput2[0]
	except:
		print "there is no saved phonebook"
		cleer_screen()
	
 	
#------------------------------
# application
#------------------------------
cleer_screen(False)
while True : # main while loop 
	print_menu()
	input = raw_input("make your selection ")
	cleer_screen(False)
	if input == "1":
		add_number()
	if input == "2":
		del_number()
	if input == "3":
		find_number()
	if input == "4":
		list_numbers()
	if input == "s":
		save_book()
	if input == "l":
		load_book()
	if input.strip() == 'Q' or input.strip() == 'q' :
		print "Bye !"
		break
