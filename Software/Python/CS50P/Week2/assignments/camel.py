word = input("enter a word: ")
result = ""    #start with an empty string variable so the string can be build piece by piece in the loop.

for letter in word:
    if letter.isupper():
        result += "_" + letter.lower() # when using =+ means ad this to whatever there allready is, also add to self.
    else:
        result += letter
result = result.strip("_")   #result.strip removes the specified character from the end and the beginning but never in between. 
print (result)
