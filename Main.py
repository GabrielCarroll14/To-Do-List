# Import the random module
import random

# Create a variable for the amount of items in the list
items =  0

# Create all the items in the list (Max 10)
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
print ("Welcometo To-Do List, you have a maximum of ten items. ")

# Create a loop
while items < 11:
    
    print ("You have " + str(items) + " items remaining. ")
    
    # Ask the user if they would like to create or delete an item
    choice = int(input("Press 1 to create a item, or 2 to delete an item. "))
    
    # If the user decides to create an item
    if choice == 1:
        
        # Print the list
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
        
        # Ask the user what they would like to add to the list
        uitem = input ("What would you like to add to the to do list? ")
        
        # Check which item on the list to asign the text to
        
        # If item 1 is free the item will be assigned to there
        if it1 == "0":
            it1 = (uitem)
        
        elif it1 != "0":
            
            if it2 == "0":
                it2 = (uitem)
            
            elif it2 != "0":
                
                if it3 == "0":
                    it3 = (uitem)
                
                elif it3 != "0":
                    
                    if it4 == "0":
                        it4 = (uitem)
                    
                    elif it4 != "0":
                        
                        if it5 == "0":
                            it5 = (uitem)
                        
                        elif it5 != "0":
                            
                            if it6 == "0":
                                it6 = (uitem)
                            
                            elif it6 != "0":
                                
                                if it7 == "0":
                                    it7 = (uitem)
                                
                                elif it7 != "0":
                                    
                                    if it8 == "0":
                                        it8 = (uitem)
                                    
                                    elif it8 != "0":
                                        
                                        if it9 == "0":
                                            it9 = (uitem)
                                        
                                        elif it9 != "0":
                                            
                                            if it10 == "0":
                                                it10 = (uitem) 

    