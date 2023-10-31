#test code
from sys import argv
import os

def createFiles():

    if len(argv) != 3:
        print("Too little or too many arguments\n")
        print("Please input a number and a folder path")
        exit()
    

    quantity = int(argv[1])
    list = [None] * quantity # array where file names will be stored
    destination = argv[2]

    if not os.path.exists(destination):
        print(f"The specified folder '{destination}' does not exist.")
        exit()

    print("Please input the names of the files you wish to create.\n")
    print(f"Input {quantity} file names. If you are pasting them all at once, seperate by newspace")

    for i in range(quantity):
        name = input() #grab it
        name = name.replace(" ", "_").lower()# give them underscoress
        
        list[i] = name
    
    message = input("please input the string you would like to write to the initial files:\n")

    print(" ")
    print(f"Are you sure you would like to write {message} to all the files specified above?\n")
    final_choice = input("y/n: \n")

    if final_choice != "y":
        print("aborting.. ")
        exit()
    else:
        for i in list:
            extend  = f"{i}.txt"
            file_path = os.path.join(destination, extend)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(message)

    #test


createFiles()



