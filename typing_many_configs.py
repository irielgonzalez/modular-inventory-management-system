"""
This program asks for a string and plans Robbie's
actions to type the string choosing the fastest option
between different keyboards, in order to perform
the least amount of operations possible.

"""

# Keyboards from which we will select the fastest alternative to type a string.
configuration_0 = ["abcdefghijklm", 
                    "nopqrstuvwxyz"]

configuration_1 = ["789", 
                    "456", 
                    "123", 
                    "0.-"]

configuration_2 = ["chunk",
                    "vibex",
                    "gymps",
                    "fjord",
                    "waltz"]

configuration_3 = ["bemix",
                    "vozhd",
                    "grypt",
                    "clunk",
                    "waqfs"]

# Asking the user for a string
str_to_type = str(input("Enter a string to type: ")).lower()

# Store keyboards in a list
configurations = [configuration_0,configuration_1, configuration_2, configuration_3]


# Every character of the input must appear in some row of that keyboard.
# Keyboards that can type the string:
valid_configurations = []

for i in range(len(configurations)):
    can_type = True
    
    for letter in str_to_type:
        found = False
        
        for row in configurations[i]:
            if letter in row:
                found = True
                break
        
        if not found:
            can_type = False 
            break
    
    if can_type:
        valid_configurations.append(i)

if len(valid_configurations) == 0:
    print("The string cannot be typed out.")
else:
    results = []
    
    for index in valid_configurations:
        configuration = configurations[index]
        total_moves = 0

        # Define the actions that Robbie can take.
        actions = []

        # The list has two columns, and the starting point is 
        # the top left position of the choosen keyboard.
        initial_row = 0
        initial_col = 0

        for character in str_to_type:
            # Find the target position of each letter
            for i in range(len(configuration)):
                # We check each row until it finds the letter
                if character in configuration[i]:
                    destination_row = i
                    # We convert to string because argument of type 'int' is not iterable
                    destination_col = configuration[i].index(character)
                    break
            # We add the counter of the total moves in order to find
            # the least amount of actions that Robbie will take.
            # Go right
            while initial_col < destination_col:
                initial_col += 1
                actions.append("r") 
                total_moves += 1
            # Go left
            while initial_col > destination_col:
                initial_col -= 1
                actions.append("l")
                total_moves += 1
            # Go down
            while initial_row < destination_row:
                initial_row += 1
                actions.append("d")
                total_moves += 1
            # Go up
            while initial_row > destination_row:
                initial_row -= 1
                actions.append("u")
                total_moves +=1
            # Press the key
            actions.append("p")
            total_moves +=1

        # Save the results for this keyboard
        results.append((total_moves, index, "".join(actions)))

    # Choose the configuration with the fewest total moves
    results.sort()  # Sorts by total_moves, then index, etc
    best_moves, best_index, best_actions = results[0]

    # Display the chosen configuration and the actions
    max_length = max(len(row) for row in configurations[best_index])+4
    print("Configuration used:")
    print("-"*max_length)
    for row in configurations[best_index]:
        print("|", row, "|")
    print("-"*max_length)

    print("The robot must perform the following operations:")
    print(best_actions)
