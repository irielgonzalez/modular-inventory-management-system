# modular-inventory-management-system

## Overview

This project implements a modular, object-oriented system to manage items across multiple container types, including single-compartment, multi-compartment, and specialised container configurations.

The system allows users to interactively manage inventory, organise storage structures, and simulate hierarchical storage behaviour through scalable and reusable components.

## Technical Concepts Applied
- Object-Oriented Programming (OOP)
- Abstraction and encapsulation
- Inheritance and polymorphism
- Modular system design
- Structured input validation

The system allows users to:
- Create containers
- Add items dynamically
- Manage multi-compartment configurations
- Simulate structured storage environments

## Learning Outcomes:
This project strengthened my understanding of system modelling, modular architecture, and scalable software design.

__________________________________________________________________________________________
__________________________________________________________________________________________

Steps followed for this project in detail:

# Items and containers 

This program that reads items and containers from files items.csv and containers.csv, and prints the list of items.

Items
An item has:
- a name, and
- a weight.

We recommend you create a class to represent items.

Containers (In this case we represent containers with classes)

A container has: 
- a name,
- an empty weight, i.e. their weight when they are empty, and
- a weight capacity, i.e. the maximum combined weight that the container can hold.

-- Two copies of the same item or container can exist. If two items or containers have the same name, then they have the same characteristics (e.g. weight).
-- Throughout the assignment, all weights and weight-related measures (i.e. weight capacities) are non-negative integers.

After reading all items and containers, do not print them, but instead ask the user for a container to pick for the adventure. For example,

Enter the name of the container: A backpack
Main menu
Then, a menu with three options will be shown repeatedly. The program prompt of the main menu looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1. Loot item.

Upon entering 1, the program will then ask for the name of an item to loot. If the item can fit in the container given the remaining capacity, the program indicates so, as shown in the following.

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".

If, instead, the remaining capacity is not sufficient to store the item, the item is not looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's recursive call count
Failure! Item "Fibonnaci's recursive call count" NOT stored in container "A backpack".

If the item's name is not one of the known items, then the user is asked for the name again:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A smaller Fibonnaci's recursive call count
"A smaller Fibonnaci's recursive call count" not found. Try again.
Enter the name of the item: Fibonnaci's rabbytes family tree
Success! Item "Fibonnaci's rabbytes family tree" stored in container "A backpack".

See Example 1 below for a complete example.

Consider using exceptions (including custom ones) to handle the case where a container cannot store an item.

2. List looted items.
Upon entering 2, the program will then print the container and the list of content, in the order they have been looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 186, empty weight: 40, capacity: 146/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
   A rock (weight: 1)

Notice how the total weight and capacity of the backpack are updated based on the contents.

An additional file, multi_containers.csv, now provides the description of containers that have multiple compartments, each behaving like an independent container. The menu itself does not change.

# Container with multiple compartments

The empty weight of a container with multiple compartments is the sum of the empty weights of the compartments.

When looting an item, the item can be looted if it fits in one compartment. If it fits in multiple compartments, it is placed in the first one (in the order listed in the file). Once an item is placed in a compartment, it is not moved, even if that would allow looting more items.

Displaying a container with multiple compartments now shows the items stored in each compartment.

An additional file, magic_containers.csv, now provides the description of containers that behave like containers with a single compartment, but that do no increase in weight if items are stored in them. They still have a maximum capacity, though.

# Magic containers

The total weight remains equal to the empty way. The capacity is computed as for a non-magical container. 

An additional file, magic_multi_containers.csv, now provides the description of containers that behave like containers with multiple compartments, and, like the other magic containers, do no increase in weight if items are stored in them. Each compartment still has a maximum capacity.

# Magic containers with multiple compartments

The total weight remains equal to the empty way. The capacity is computed as for a non-magical container with multiple compartments, which is that it is computed and displayed at the compartment level. See Example 1 for a complete example.
