EOL = "\n"

def promtUserForAction():
    print("Welcome to Substitute santa wish list 1.0")
    print("1. Create new list")
    print("2. Load existing list")
    return input(">>>")

def createList():
    print("Create new list")
    filename = input("Enter filename:")
    file = open(filename, "wt")
    childName = input("Enter child name:")
    file.writelines(childName + EOL)
    done = False
    counter = 0
    while not done:
        counter += 1
        item = input("Item " + str(counter) + ":")
        if item == "":
            break
        file.write(item + EOL)
    return True

def readList():
    print("Read existing list")
    filename = input("Enter filename:")
    file = open(filename, "rt")
    childName = file.readline()
    print("----- Wish list " + filename + " -----")
    print("Child name: " + childName, end="")
    done = False
    counter = 0
    while not done:
        counter += 1
        item = file.readline()
        if (item == ""):
            break
        print("Item " + str(counter) + ": " + item, end="")
    return True

done = False
while not done:
    action = promtUserForAction()
    if (action == "1"):
        done = createList()
    elif (action == "2"):
        done = readList()