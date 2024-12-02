import random

def randList(int):
    outList = []
    for i in range(0, int):
        outList.append(random.randint(-100, 100))
    return outList


def maxSubList(inList):
    maxSum = inList[0]
    tempSum = inList[0]
    start = 0
    end = 0
    tempStart = 0

    for i in range(1, len(inList)):
        if tempSum + inList[i] > inList[i]:
            tempSum += inList[i]
        else:
            tempSum = inList[i]
            tempStart = i

        if tempSum > maxSum:
            maxSum = tempSum
            start = tempStart
            end = i + 1

    return inList[start:end], maxSum


promptForLength = True
while promptForLength:
    try:
        userInput = int(input("Please enter an integer for the length of list you would like to generate.\n"))
        if userInput > 0:
            print("Generating a list with " + str(userInput) + " values.")
            userList = randList(userInput)
            print("New List: " + str(userList))
            promptIfProcess = True
            while promptIfProcess:
                try:
                    userInput = input(
                        "Would you like to process this list? If no you will be prompted to generate a new list. Y/N\n")
                    if userInput == 'Y' or userInput == 'y':
                        subList, maxSum = maxSubList(userList)
                        print(f'Original list: {userList}\nSublist with the highest sum: {subList}\nSum of subList: {maxSum}')
                        promptForLength = False
                        promptIfProcess = False
                    elif userInput == 'N' or userInput == 'n':
                        promptIfProcess = False
                    else:
                        print("Please enter Y or N")
                except:
                    print("Unknown Error, terminating process")
                    promptForLength = False
                    promptIfProcess = False
        else:
            print("Number should be greater than 0")
    except:
        print("Unknown Error, terminating process")
        promptForLength = False


