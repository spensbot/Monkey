#import statements
import random
import time

#Parameters
reference = "shakespear"

#open the stripped file, create a string of it, and close the file.
f = open(reference + "_stripped.txt", 'r')
text = f.read()
f.close()

#initialize counter variables
count = 0
max_count = 0
attempts = 0
start = time.time()

while True:

    for letter in text:

        #if the randomly generated number does not match the next letter, start over. Else, add to the counter and continue.
        if chr(random.randint(97,122)) != letter:
            break
        count += 1

    #check to see if the counter reached a new high.
    attempts += 1
    if count > max_count:
        print(repr(count) + "     " + repr(attempts))
        max_count = count
        print("Elapsed Time (s): " + repr(time.time()-start))

    #if the counter is the length of the text string, end the program
    if count == len(text):
        break

    count = 0

