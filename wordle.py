import random
from termcolor import colored
# MAKE THE COLORS WORKKK
def rowfind(letter,fr,sr,lr):
    if letter.upper() in fr:
        return fr
    elif letter.upper() in sr:
        return sr
    else:
        return lr
    
def wordcheck(x,y):
    for num in range(len(y)):
        if y[num] == x:
            return True
    return False
def wordbank():
    words = "trope plate trash paper plane names loops brick spicy water jeans genes strip fires roman grape paced vault amber nanny scalp drift piles scalp final trace quite quiet dense cocky based doubt baggy click feint these puffy diver slept speed fetus pound gland globe teach"
    words = words.split()
    rand = random.randint(0,len(words))
    return words[rand]
word = wordbank()
result = []
for num in range(len(word)):
    result.append("▢ ")
print(" ".join(result))
print("\n")
count = 0
finalprint = []
wronglist = []
firstrow = ["Q","W","E","R","T","Y","U","I","O","P"]
secondrow = ["A","S","D","F","G","H","J","K","L"]
lastrow = ["Z","X","C","V","B","N","M"]
while True:
    count = count + 1
    guess = input("\n")
    guess = list(guess)
    result = []
    victory = []
    for num in range(len(word)):
        result.append("")
    if len(guess) != 5:
        print("\ninvalid guess. enter 5 letters.")
        continue
    else:
        for i in range(len(word)):
            row = rowfind(guess[i], firstrow,secondrow,lastrow)
            if guess[i] == word[i]:
                result[i] = colored(guess[i], "green")
                victory.append(guess[i])
                for uu in range(len(row)):
                    if guess[i].upper() == row[uu]:
                        row[uu] = colored(guess[i].upper(), "green")
            else:    
                for x in range(len(word)):
                    if guess[i] == word[x] and guess[i] != word[i]:
                        result[i] = colored(guess[i], "yellow")
                        for ee in range(len(row)):
                            if guess[i].upper() == row[ee]:
                                row[ee] = colored(guess[i].upper(), "yellow")
                        break
                    elif guess[i] != word[x] and guess[i] != word[i]:
                        result[i] = guess[i]
                        for qq in range(len(row)):
                            if guess[i].upper == row[qq]:
                                row[qq] = " "
                            
    print("".join(result))
    wronglist = sorted(wronglist)
    print(" ".join(firstrow))
    print(" ".join(secondrow))
    print(" ".join(lastrow))
    finalprint.append("".join(result))
    if count == 1:
        attempt = "attempt."
    else:
        attempt = "attempts."
    if "".join(victory) == word:
        print("You got it! The word was " + word + ".")
        print("It took", count, attempt)
        print("Here are your attempts.\n")
        for p in range(len(finalprint)):
            print(finalprint[p])
        break



