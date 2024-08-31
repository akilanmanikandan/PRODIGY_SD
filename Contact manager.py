import os


# Function to load contacts from file into dictionary
def load_contacts() :
	if os.path.exists ( "contacts.txt" ) :
		with open ( "contacts.txt", "r" ) as file :
			lines = file.readlines ( )
			contacts = {}
			for line in lines :
				name, phone, email = line.strip ( ).split ( "," )
				contacts[name] = {"phone" : phone, "email" : email}
		return contacts
	else :
		return {}


# Function to save contacts from dictionary to file
def save_contacts(contacts) :
	with open ( "contacts.txt", "w" ) as file :
		for name, info in contacts.items ( ) :
			file.write ( f"{name},{info['phone']},{info['email']}\n" )


# Function to add a new contact
def add_contact(contacts) :
	name = input ( "Enter name: " )
	phone = input ( "Enter phone number: " )
	email = input ( "Enter email address: " )
	contacts[name] = {"phone" : phone, "email" : email}
	save_contacts ( contacts )
	print ( "Contact added successfully!" )


# Function to view all contacts
def view_contacts(contacts) :
	if contacts :
		print ( "---- Contacts ----" )
		for name, info in contacts.items ( ) :
			print ( f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}" )
		print ( "------------------" )
	else :
		print ( "No contacts found." )


# Function to edit an existing contact
def edit_contact(contacts) :
	name = input ( "Enter name of contact to edit: " )
	if name in contacts :
		print ( "Enter new information (leave blank to keep existing)" )
		phone = input ( f"Enter new phone number for {name}: " )
		email = input ( f"Enter new email address for {name}: " )
		if phone :
			contacts[name]['phone'] = phone
		if email :
			contacts[name]['email'] = email
		save_contacts ( contacts )
		print ( "Contact updated successfully!" )
	else :
		print ( "Contact not found." )


# Function to delete a contact
def delete_contact(contacts) :
	name = input ( "Enter name of contact to delete: " )
	if name in contacts :
		del contacts[name]
		save_contacts ( contacts )
		print ( "Contact deleted successfully!" )
	else :
		print ( "Contact not found." )


# Main function
def main() :
	contacts = load_contacts ( )

	while True :
		print ( "\n------ Contact Manager ------" )
		print ( "1. Add Contact" )
		print ( "2. View Contacts" )
		print ( "3. Edit Contact" )
		print ( "4. Delete Contact" )
		print ( "5. Exit" )
		choice = input ( "Enter your choice (1-5): " )

		if choice == "1" :
			add_contact ( contacts )
		elif choice == "2" :
			view_contacts ( contacts )
		elif choice == "3" :
			edit_contact ( contacts )
		elif choice == "4" :
			delete_contact ( contacts )
		elif choice == "5" :
			print ( "Thank you for using Contact Manager!" )
			break
		else :
			print ( "Invalid choice. Please enter a number between 1 and 5." )


if __name__ == "__main__" :
	main ( )
