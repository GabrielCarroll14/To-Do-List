# Import the random module
import random

# Create a variable for the amount of items in the list
items =  0

# Create all ten items in the list 
it1 = "0"
it2 = "0"
it3 = "0"
it4 = "0"
it2 = "0"
it5 = "0"
it6 = "0"
it7 = "0"
it8 = "0"
it9 = "0"
it10 = "0"

# Print a welcome message to the user
print ("Welcome to To-Do List, you have a maximum of ten items. ")

# Create a loop
while items < 11:
    
    # Print the list
    print (" ") # Print two gap's so when running, the code doesn't seem so bunched up
    print (" ")
    print (it1)
    print (it2)
    print (it3)
    print (it4)
    print (it5)
    print (it6)
    print (it7)
    print (it8)
    print (it9)
    print (it10)
    print (" ") # Print two gaps at the end to stop the code from seeing bunched up
    print (" ")
    
    # Use the word "Item" instead of "Items" if the amount of items on the list is less than 2
    if items < 2:
        print ("You have " + str(items) + " item remaining. ")
        
    # Use the word "items" instead of "item" if the amount of items is more than 1
    if items > 1:
        print ("You have " + str(items) + " items remaining. ")
    
    # Ask the user if they would like to create or delete an item
    choice = int(input("Press 1 to create a item, or 2 to delete an item. "))
    
    # If the user decides to create an item
    if choice == 1:
        
        # Ask the user what they would like to add to the list
        uitem = input ("What would you like to add to the to do list? ")
        
        # Check which item on the list to asign the users input item to
        if it1 == "0":
            it1 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
        
        elif it2 == "0":
            it2 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
            
        elif it3 == "0":
            it3 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                
        elif it4 == "0":
            it4 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                    
        elif it5 == "0":
            it5 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                        
        elif it6 == "0":
            it6 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                            
        elif it7 == "0":
            it7 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                                
        elif it8 == "0":
            it8 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                                    
        elif it9 == "0":
            it9 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                                        
        elif it10 == "0":
            it10 = (uitem) # Assign the users text into the new variable
            items = items + 1 # Add one item to the amount of items
                                                
    # When the user decides to delete an item
    if choice == 2:
        
        # Print a message to the user confirming that they are going to delete a item
        print ("You have decided to delete an item. ")
        
        # Print all available items to delete
        print (" ") # Print a gap so the code doesnt seem so bunched up
        print ("1: " + it1)
        print ("2: " + it2)
        print ("3: " + it3)
        print ("4: " + it4)
        print ("5: " + it5)
        print ("6: " + it6)
        print ("7: " + it7)
        print ("8: " + it8)
        print ("9: " + it9)
        print ("10: " + it10)
        print (" ") # Print a gap so the code doesnt seem so bunched up
        
        # Ask user what item they would like to delete
        dell = input("What item would you like to delete? ")
        
        # Delete the option the user has asked to be deleted
        if dell == "1":
            it1 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "2":
            it2 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "3":
            it3 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "4":
            it4 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
        
        if dell == "5":
            it5 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "6":
            it6 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "7":
            it7 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "8":
            it8 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "9":
            it9 = "0" # Because the user has deleted the item from the list, this deletes it from the amount
            
        if dell == "10":
            it10 = "0" # Because the user has deleted the item from the list, this deletes it from the amount