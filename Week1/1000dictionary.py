import random

dictionary = []
f = open("1-1000.txt", 'r')
dictionary = f.readlines()
f.close()
dictionary.sort()

mode = input("Choose play mode 1 or 2: ")

def mode1(dictionary):
    word = dictionary[random.randint(0,len(dictionary)-1)]
    print("Assume that each page describes one word. Your task is to find where the word '" + word[:-1] \
         +"' is in the dictionary.")
    print("Please keep in mind that the dictionary starts at page 0 and ends at page 999")
    print("Press Ctrl-Z to quit\n")

    counter = 0
    while True:
        index = int(input("What page? "))
        counter = counter + 1
        try:
            print(dictionary[index])
            if dictionary[index] == word:
                print("Bravo! It's on page " + str(index))
                print("You make it after " + str(counter) + " guesses")
                break
        except:
            print("No such page!")
            break

def mode2(dictionary):
    word_list = ['hello\n', 'bag\n', 'shopping\n', 'shower\n', 'teacher\n', 'message\n', 'text\n', 'computer\n']
    coin_toss = random.randint(0,1)
    if coin_toss == 0:
        word = word_list[random.randint(0,len(word_list)-1)]
    else:
        word = dictionary[random.randint(0,len(dictionary)-1)]

    print("Same rule as mode 1. But now you have to decide whether '" + word[:-1]+"' is in dictionary or not")

    counter = 0
    while True:
        index = (input("What page? (press 'a' to give answer) "))
        if index == 'a':
            answer = input("Is \"" + word[:-1] + "\" in dictionary? (y/n): ")
            if 'y' in answer.lower():
                answer = 1
            else:
                answer = 0
            if answer == coin_toss:
                print("Bravo, you make perfect answer after", counter,"guesses")
                break
            else:
                print("No no, It's not correct!")
                break
        else:
            index = int(index)
            counter = counter + 1
            try:
                print(dictionary[index])
                if dictionary[index] == word:
                    print("Ah, you found it!")
                    break
            except:
                print("No such page!")
                break

if mode == "1":
    mode1(dictionary)
else:
    mode2(dictionary)
