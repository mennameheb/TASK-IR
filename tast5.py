lst = [5, 3, 2, 4, 7, 6, 9]
root = Node(lst[0])
for i in lst[1:]:
    root.insert(i)

# Print the initial binary tree
print("Initial binary tree:\n", root)

# Prompt the user for their choice
while True:
    print("\nChoose an option:")
    print("1. Add a new element.")
    print("2. Delete an element.")
    choice = input("Enter 1 or 2: ")
    
    # Add a new element to the binary tree
    if choice == '1':
        val = int(input("Enter a new integer to add: "))
        root.insert(val)
        print("New binary tree:\n", root)
        
    # Delete an element from the binary tree
    elif choice == '2':
        val = int(input("Enter an integer to delete: "))
        node = root.search(val)
        if node:
            node.delete()
            print("New binary tree:\n", root)
        else:
            print("Value not found in binary tree.")
    
    # Invalid choice
    else:
        print("Invalid choice. Try again.")