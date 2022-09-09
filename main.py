stack = list()

welcomeText = "Welcome to the text eater"
promt = "Please write any text and I will eat it after pressing enter." + " If you press enter without writing, you can ask me to do something else.\n"

elsePromt = """Write "get" and then a number to retrieve a word. 
Write "compare" and then two numbers to compare 2 words.
Write "exit" to stop the program and leave me be.
"""

print(welcomeText)
inp = " "

largestText = None
smallestText = None
info = "biggest text eaten: {0}. Smallest text eaten {1}."

while True:
    while inp != "":
        print("-----")
        if largestText != None:
            print(info.format(largestText, smallestText))
        inp = input(promt)
        if inp != "":
            stack.append(inp)
            if largestText == None:
                largestText = len(inp)
                smallestText = len(inp)
            else:
                if len(inp) > largestText:
                    largestText = len(inp)
                if len(inp) < smallestText:
                    smallestText = len(inp)
    print("-----")
    inp = input(elsePromt)
    command = inp.split(" ")
    if command[0].lower() == "exit":
        print("Goodbye!")
        break;
    elif command[0].lower() == "compare":
        index1 = index = int(command[1]) - 1
        index2 = index = int(command[2]) - 1
        bounds1 = True  if index1 in range(len(stack)) else False 
        bounds2 = True if index2 in range(len(stack)) else False 
        if bounds1 and bounds2:
            if stack[index1] == stack[index2]:
                print("The text are equal")
            else:
                print("The text are different")
        else:
            print ("Sorry, can't compare those text")

    elif command[0].lower() == "get":
        index = int(command[1]) - 1
        if index not in range(len(stack)):
            print ("Sorry, can't retrieve that text")
        else:
            print(stack[index])
    else:
        print("I didn't get what you want, please follow my instructions.")