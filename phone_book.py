#------------------------------
# functions and definitions
#------------------------------

import os

phone_book ={}

def cleer_screen(confirm=True):
	if confirm == True:
		spacer()
		cont = raw_input("press enter to continue")
	os.system('cls' if os.name == 'nt' else 'clear')
def spacer():
	print " "
	print " "

def print_menu():
	spacer()
	print " #############################################"
	print " #     phone book v0.1                       #"
	print " #############################################"
	print " # 1. add Person/number                      #"
	print " # 2. del Person/number                      #"
	print " # 3. find number                            #"
	print " # 4. List all numbers                       #"
	print " # q  Quit                                   #"
	print " #############################################"
	spacer()

def add_number():
	spacer()
	name = 	raw_input("enter name: ")
	number = raw_input("enter number: ")
	phone_book[name] = number
	cleer_screen(False)

def del_number():
	spacer()
	name = raw_input("enter name to delete: ")
	print "are you sure you want to delete " + name 
	yesno = raw_input("y/n: ")
	if yesno == "y" or yesno == "Y":
		try:
			print "deleting " + name + " - " + phone_book[name] 
			del phone_book[name]
		except:
			print "name not found"
	cleer_screen()

def find_number():
	spacer()
	name = raw_input("enter name: ")
	try:
		print name + " " + phone_book[name]
		cleer_screen()
	except :
		print "that name is not in the phone book"
		cleer_screen()

def list_numbers():
	spacer()
	print "number -  name"
	for x,y in enumerate(sorted(phone_book)):
		print  phone_book[y] + " - " + y
	cleer_screen()
 	
#------------------------------
# application
#------------------------------
cleer_screen(False)
while True :
	print_menu()
	input = raw_input("make your selection ")
	print input
	cleer_screen(False)
	if input == "1":
		add_number()
	
	if input == "2":
		del_number()

	if input == "3":
		find_number()

	if input == "4":
		list_numbers()


	if input.strip() == 'Q' or input.strip() == 'q' :
		print "Bye !"
		break
		
