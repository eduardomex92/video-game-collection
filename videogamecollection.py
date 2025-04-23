'''
Heiner Alcala-Salas
October 22, 2024
Video Game Collection
'''
import os

#verification function
def verify(FILENAME):
    """Verifies if the file exists, and if not, creates it with table headings."""
    if not os.path.exists(FILENAME): #if no file exists it will create it
        f = open(FILENAME, 'w') #opens file in write mode
        #writes tubular table headings 
        f.write("%-15s%-15s%-15s\n" % ("Title", "Platform", "Market Value"))
        f.write("%-15s\n" % ("-" * 50))
        f.close()
    return FILENAME #returns file

#dictionary to store games(Title: [Platform, Market Value])
#initialize dictionary
game_collection = {}
#load file if exist already
def load_games_file(FILENAME):
    """Loads existing games from the file into the game_collection dictionary."""
    f = open(FILENAME, 'r') #opens file in read mode
    f.readline() #reads lines
    for line in f: #loops through lines
        data = line.strip().split('$') #splits market value by the $ sign from title and platform
        if len(data) == 2: #check we have both the game details and the market value
            title_platform = data[0].rsplit(' ', 1) #split into title and platform by the last white space
            if len(title_platform) == 2: #checks we have title and platform
                title, platform = title_platform #saves title and platform individually
                market_value = float(data[1]) #converts market value to float
                game_collection[title] = [platform, market_value] #adds existing content into dictionary
    f.close()

#display game function
def add_game(FILENAME):
    """Add games to your collection, including title, platform, and market value."""
    title = input("Enter title of game: ") #inut for title of game
    platform = input("Enter platform: ") #input for platform
    market_value = float(input("Enter the market value of the game: $")) #input for market value

    #adds the game to the dictionary
    game_collection[title] = [platform, market_value]

    #adds the game to the file
    f = open(FILENAME, 'a')
    f.write("%-15s%-15s$%-14.2f\n" % (title, platform, market_value))
    f.close()

    message = str(title) + " added to the collection"
    return message

def display_games(FILENAME):
    """Display all games in your collection."""
    print("\nCurrent game collection (so far):\n") #prints message
    #builts list message to display all content
    messages = []
    messages.append("%-15s%-15s%-15s" % ("Title", "Platform", "Market Value"))

    #reads and prints from the file
    f = open(FILENAME, 'r')
    f.readline() #reads line
    any_games = False 
    for line in f: #loops through lines
        line_content = line.strip() #saves line content in message
        if line_content:
            messages.append(line_content)#add lines in a list to display as a single output
            any_games = True 
    f.close()
    if not any_games: #if no games added yet display message
        messages.append("No games in your collection yet.")
    return "\n".join(messages) #returns messages

#calculate function
def calculate_worth():
    """Calculates the total worth of your collection."""
    #variables
    total_value = 0
    count = 0

    #loops through the dictionary and adds the market value of games
    for title, data in game_collection.items():
        total_value += data[1] #data[1] is the market value index 1 of 0 and 1
        count += 1 #adds value of game through each loop
    
    #Build the message
    message = "\nYou have " + str(count) + " games in your collection worth $" + "%.2f" % total_value + ".\n"
    return message

#exit function
def exit_program():
    """Exit the program."""
    print("Exiting collection. Goodbye!")
    exit() #exits program

#main function
def main():
    FILENAME = "game_collection.txt" #variable
    verify(FILENAME) #verify file exists
    load_games_file(FILENAME) #load existing games from the file

    #jump table to navigate the menu
    jump_table = {
        "1": lambda: print(add_game(FILENAME)),
        "2": lambda: print(display_games(FILENAME)),
        "3": lambda: print(calculate_worth()),
        "4": exit_program
    }

    #while loop
    while True:
        print("\n--- My Video Game Collection ---")
        print("1. Add a game to your collection")
        print("2. Display all games in your collection")
        print("3. Calculate the total worth of your collection")
        print("4. Exit")

        choice = input("Choose an option from the menu: ")
        action = jump_table.get(choice)
        #if statement to validate jump table menu entry
        if action:
            action()
        else:
            print("Invalid choice, please try again.")

# The entry point for the program execution
if __name__ == "__main__":
    main()
