"""
This program allows items and containers to be managed
interactively by the user. This time, we have containers
with a single compartment, multiple compartments, magic
containers, and a new type of containers, magic containers
with multiple compartments.
"""

#################### Main Menu ####################
def main_menu(container):
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Loot item.")
        print("2. List looted items.")
        print("0. Quit.")
        print("==================================")
        choice = input()
        if choice == "1":
            container = loot_item(container)
        elif choice == "2":
            list_looted(container)
        elif choice == "0":
            break

#################### Global Data ####################
items_dict = {}
containers_dict = {}
looted_items = []

class Item:
    def __init__(self, name, weight):
        """
        Represents an item that can be looted into containers.
        They all have a name and weight.
        """
        self.name = name
        self.weight = weight

class Container:
    """
    Represents a container that can store items.
    They all have a name, weight, capacity, and items.
    """
    def __init__(self, name, weight, capacity):
        """
        Constructor of Container that sets the base information
        to create all following objects.
        """  
        self.name = name
        self.weight = weight
        self.capacity = capacity
        self.contents_weight = 0
        self.items = []

    def check_and_store(self, item):
        """
        Check capacity and store
        """
        if self.contents_weight + item.weight <= self.capacity:
            self.contents_weight += item.weight
            self.items.append(item)
            return True
        return False

    def display(self):
        """
        Print's container's information and items stored inside.
        """
        print(f"{self.name} (total weight: {self.weight + self.contents_weight}, empty weight: {self.weight}, capacity: {self.contents_weight}/{self.capacity})")
        for item in self.items:
            print(f"   {item.name} (weight: {item.weight})")

class Multicontainer(Container):
    """
    Represents a container that has multiple compartments.
    """
    def __init__(self, name, compartments):
        """
        Initialises a Multicontainer object with multiple compartments.
        """
        total_weight = sum(i.weight for i in compartments)
        super().__init__(name, total_weight, 0)
        self.compartments = compartments
    
    def check_and_store(self, item):
        """
        Initialises a Multicontainer object with multiple compartments.
        """
        for i in self.compartments:
            if i.check_and_store(item):
                self.contents_weight += item.weight
                self.items.append(item)
                return True
        return False
    
    def display(self):
        """
        Displays the multicontainer information, and the content of each compartment.
        """
        print(f"{self.name} (total weight: {self.weight + self.contents_weight}, empty weight: {self.weight}, capacity: 0/0)")
        for i in self.compartments:
            print(f"   {i.name} (total weight: {i.weight + i.contents_weight}, empty weight: {i.weight}, capacity: {i.contents_weight}/{i.capacity})")
            for item in i.items:
                print(f"      {item.name} (weight: {item.weight})")

class Magic(Container):
    """
    Represents a "Magic" Container which behave like containers with 
    a single compartment (inherits from the base Container Class). They
    do not increase in weight. they do have a maximum capacity.
    """
    def __init__(self, name, weight, capacity):
        """
        Initialises a Magic container by calling the Container constructor.
        """
        super().__init__(name, weight, capacity)

    def check_and_store(self, item):
        """
        Check capacity and store.
        """
        if self.contents_weight + item.weight <= self.capacity:
            self.contents_weight += item.weight
            self.items.append(item)
            return True
        return False

    def display(self):
        """
        Displays the magic container information, and the content of each compartment.
        """
        print(f"{self.name} (total weight: {self.weight}, empty weight: {self.weight}, capacity: {self.contents_weight}/{self.capacity})")
        for item in self.items:
            print(f"   {item.name} (weight: {item.weight})")

class MultiMagic(Container):
    """
    A magic multicontainer behaves like a multicontainer but uses the special
    'Magic' rules. (They do not increase in weight and they do have a maximum capacity).
    """
    def __init__(self, name, compartments):
        """
        Initialises a MultiMagic container. Where the name of the multicontainer,
        and a list of container objects (compartments) are arguments.
        """
        total_weight = sum(i.weight for i in compartments)
        super().__init__(name, total_weight, 0)
        self.compartments = compartments
    
    def check_and_store(self, item):
        """
        Attempts to store an item in one of the compartments.
        """
        for i in self.compartments:
            if i.check_and_store(item):
                self.items.append(item)
                return True
        return False
    
    def display(self):
        """
        Prints the multicontainer's details and the contents of each compartment.
        """
        empty_weight = sum(comp.weight for comp in self.compartments)
        total_weight = empty_weight
        print(f"{self.name} (total weight: {total_weight}, empty weight: {empty_weight}, capacity: 0/0)")
        for i in self.compartments:
            print(f"   {i.name} (total weight: {i.weight + i.contents_weight}, empty weight: {i.weight}, capacity: {i.contents_weight}/{i.capacity})")
            for item in i.items:
                print(f"      {item.name} (weight: {item.weight})")
#################### Message ####################
def message():
    """
    Reads items and containers from their CSV files. And prints 
    a summary message that shows how many items and containers were initialised.
    """
    item_lines = read_file("items.csv")
    container_lines = read_file("containers.csv")
    multi_container_lines = read_file("multi_containers.csv")
    magic_container_lines = read_file("magic_containers.csv")
    magic_multi_container_lines = read_file("magic_multi_containers.csv")
    total = len(item_lines) + len(container_lines) + len(multi_container_lines) + len(magic_container_lines) + len(magic_multi_container_lines)
    print(f"Initialised {total} items including {len(container_lines) + len(multi_container_lines) + len(magic_container_lines) + len(magic_multi_container_lines)} containers.\n")

#################### File Reading ####################
def read_file(filename: str):
    """
    Reads a CSV file and returns all lines except the header.
    """
    with open(filename, "r") as file:
        lines = file.readlines()[1:] # Skip header
    return lines

def items():
    """
    Reads item data from 'items.csv', sorts the items alphabetically by name, and 
    prints the weight and name of the item.
    """
    lines = read_file("items.csv")
    for l in sorted(lines, key=lambda x: x.strip().split(",")[0].lower()):
        name, weight = l.strip().split(",")
        items_dict[name] = Item(name, int(weight)) # Store items in the dictionary now using Item class

def containers():
    """
    Reads item data from 'items.csv', sorts the items alphabetically by name, and 
    prints the weight and name of the item.
    """
    lines = read_file("containers.csv")
    for l in sorted(lines, key=lambda x: x.strip().split(",")[0].lower()):
        name, weight, capacity = map(str.strip,l.strip().split(","))
        containers_dict[name] = Container(name, int(weight), int(capacity)) # Contents weigth = 0
        
def multi_containers():
    """
    Loads multicontainers from 'multi_containers.csv' into the global containers_dict.
    Each multicontainer has the containers found in the file.
    """
    lines = read_file("multi_containers.csv")
    for l in sorted(lines, key=lambda x: x.strip().split(",")[0].lower()):
        sections = l.strip().split(",")
        name = sections[0]
        compartments = []
        # Process each compartment listed after the name
        for comp_name in sections[1:]:
            comp = comp_name.strip()
            if comp in containers_dict:
                new = containers_dict[comp]
                # Create a fresh Container obect with same properties
                compartment = Container(comp, new.weight, new.capacity)
            compartments.append(compartment)
        # Store
        containers_dict[name] = Multicontainer(name, compartments)

def magic_containers():
    """
    Loads magic containers from 'magic_containers.csv' into the global containers_dict.
    """
    lines = read_file("magic_containers.csv")
    for l in sorted(lines, key=lambda x: x.strip().split(",")[0].lower()):
        name, given_name = map(str.strip,l.strip().split(","))
        if given_name in containers_dict:
            given = containers_dict[given_name]
            containers_dict[name] = Magic(name, given.weight, given.capacity) # Contents weigth = 0
 
def magic_multi_containers():
    """
    Loads magic multicontainers from 'magic_multi_containers.csv' into the global
    containers_dict. Each line of this file defines a new magic multicontainer by
    referencing an existing multicontainer already stored in containers_dict.
    """
    lines = read_file("magic_multi_containers.csv")
    for l in sorted(lines, key=lambda x: x.strip().split(",")[0].lower()):
        name, given_name = map(str.strip,l.strip().split(","))
        if given_name in containers_dict:
                given = containers_dict[given_name]
                # Only proceed if the base is a Multicontainer
                if isinstance(given, Multicontainer):
                    compartments_magic = []
                    # Clone each compartment into a fresh Container object
                    for comp in given.compartments:
                        compartments_magic.append(Container(comp.name,comp.weight,comp.capacity))
                    # Store new MultiMAgic container
                    containers_dict[name] = MultiMagic(name, compartments_magic)

#################### Looting Logic ####################
def loot_item(container):
    """
    Prompts the user to loot (store) an item into a chosen container.
    Recieving the container currently in use as an argument, and 
    returning the updated container.
    """
    if container is None:
        print("Enter the name of the container:")
        container_name = input()
        if container_name not in containers_dict:
            print(f"{container_name} not found. Try again.")
            return container
    else:
        container_name = container
    # Asking the user a name of the item to loot.
    item_name = str(input("Enter the name of the item: "))
    if item_name not in items_dict:
        print(f"{item_name} not found. Try again.")
        return container     

    item = items_dict[item_name]
    container = containers_dict[container_name]

    if container.check_and_store(item):
        looted_items.append((item_name, container_name)) # Wrapping the, in a tuple so 
                                                         # append() takes onlu one argument
        print(f'Success! Item "{item_name}" stored in container "{container_name}".')
    else:
        print(f'Failure! Item "{item_name}" NOT stored in container "{container_name}".')
    return container_name 

#################### Listing Looted Items ####################
def list_looted(container_name):
    """
    Diplays contents of a given container (argument), including weight 
    and capacity usage.
    """
    container = containers_dict[container_name]
    container.display()
    
#################### Start of Program ####################
items()
containers()
multi_containers()
magic_containers()
magic_multi_containers()
message()

container_name = input("Enter the name of the container: ")

while container_name not in containers_dict:
    print(f"{container_name} not found. Try again.")
    print("Enter the name of the container:")
    container_name = input()

main_menu(container_name)
