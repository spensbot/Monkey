strip(reference)

def strip(reference):

    #load files
    original = open(reference + ".txt",'r')
    stripped = open(reference + "_stripped.txt", 'w')

    text = original.read()

    #iterate over the file
    for char in text:

        #If the character is alphabetic, write it's lower case form to the stripped file.
        if char.isalpha():
            stripped.write(char.lower())

    #close files
    original.close()
    stripped.close()