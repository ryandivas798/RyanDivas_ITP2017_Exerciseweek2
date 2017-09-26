dictionary = {
	"test":"123",
	"hello":"1234",
	"wth":"541"
}

print('Type "help" for list of commands')
# made the entire program a loop that will break if the "do" variable is equal to "exit" 
while True:
	do = input("What would you like to do? ")
	
	if do == "exit":
		break
			
	elif do == "search":
		search = input("Word: ")
		for i,j in dictionary.items():
			if i == search:
				print("Definition: ", j)
# ~~~~~~			

	elif do == "add":
# added a check if the same word is already in the dictionary
		add_word = input("What word would you like to add? ")
		if add_word in dictionary.keys():
			ans = input("Word already exist in the dictionary, would you like to replace the definition? (yes/no)")
			if ans == "yes":
				add_definition = input("What is the new definition? ")
		else:
			add_definition = input("What is the definition? ")
		dictionary[add_word] = add_definition
		
	elif do == "remove":
		remove_word = input("what word would you like to remove? ")
		if remove_word not in dictionary.keys():
			print("Word does not exist in the dictionary")
		else:
			del dictionary[remove_word]
	
	elif do == "display":
		print(list(dictionary.keys()))
			
	elif do == "help":
		print('''Search for a word\t\t: "search"
Add a word\t\t\t: "add"
Remove a word\t\t: "remove"
Display all words in dictionary\t: "display"
Exit proram\t\t\t: "exit"
		''')