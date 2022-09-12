import logging


logging.basicConfig(filename='text-eater.log', level=logging.DEBUG)

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
        logging.debug("Promt: %s", inp)
        logging.debug("Action: Registering text")

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
    logging.debug("Promt: %s", inp)

    command = inp.split(" ")
    if command[0].lower() == "exit":
        print("Goodbye!")
        logging.debug("Action: Shutting down")

        break;
    elif command[0].lower() == "compare":
        index1 = int(command[1]) - 1
        index2 = int(command[2]) - 1
        bounds1 = True  if index1 in range(len(stack)) else False 
        bounds2 = True if index2 in range(len(stack)) else False
        logging.debug("Action: Comparing") 
        if bounds1 and bounds2:
            logging.debug("Action: Comparing %s and %s", stack[index1], stack[index2])
            if stack[index1] == stack[index2]:
                print("The text are equal")
                logging.debug("Output: The text are equal")
            else:
                print("The text are different")
                logging.debug("Output: The text are different")
        else:
            print ("Sorry, can't compare those text")
            logging.warning("Can't compare: out of bounds")


    elif command[0].lower() == "get":
        logging.debug("Action: get")
        index = int(command[1]) - 1
        if index not in range(len(stack)):
            print ("Sorry, can't retrieve that text")
            logging.warning("Can't compare: out of bounds")

        else:
            print(stack[index])
            logging.debug("Action: Retrieving value")

    else:
        print("I didn't get what you want, please follow my instructions.")
        logging.warning("Unrecognized input: %s ", inp)
