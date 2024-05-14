index = 0

def listFinder(name) :
    global index
    list = ["ahad", "hamza", "hamid", "zia", "noor", "ahad"]
    data = list[index]
    if data == name :
        print(f"Your input '{name}' matches at {index}")
        
    index = index + 1
    if index < len(list) :
        listFinder(name)
    else :
        print("Recursion ends here")

def App() :
    print("List finder...")
    print("--------------------------------")
    name = input("Enter name to search :\n")
    listFinder(name)
App()