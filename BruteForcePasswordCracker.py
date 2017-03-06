#Zach Nandapurkar
#ITP 125
#Brute Force Password Cracker

#Import statements
import hashlib
import sys
import time

#Open the target file and create an object for its contents
hashfile = open("hashes.txt", 'rw+')

#Define the range of possible characters to check against the different password combinations
PossibleChars = range(32,127)

#combine will recursively test out different combinations of letters starting from
#one letter and eventually moving on to two, then three, etc.  it sends all raw 
#combinations to the matchPassword function below
def combine(width, pos, startString, hashty):
    #current pos
    for char in PossibleChars:
        if (pos < width - 1):
            #if combine is true, keep checking passwords
            if (combine(width, pos + 1, startString + "%c" % char, hashty) == True):
                return True
        else:
            #if matchPassword is ever true, you have a match, return it and move on
            if (matchPassword(startString + "%c" % char, hashty) == True):
                return True
    return False

#matchPassword takes in a password guess string and a hash string that has been read in
#It then converts the password guess to an md5 hash and checks the generated md5 vs the original
def matchPassword(password, hashGuy):
    m = hashlib.md5(password)
    if (m.hexdigest() == hashGuy):
        print "Another Cracked! Password is: " + password + ""
        #If the password was successfully found return true, so the code can move to the next function
        return True

#loop through all the lines in the file
for line in hashfile:
    #Acquire the time in seconds to comare
    start_time = time.time()

    #set the current hash string to the first line of code
    hash = line
    hash=hash.rstrip('\n')

    print "Current hash is: {" + hash + "}"

    #Stops the cpu from running the program with too much memory
    charStop = 14
    for startWidth in range(1, charStop + 1):
        #check to see if combine is true to continue in the loop, if so break from the loop
        if (combine(startWidth, 0, "", hash) == True):
            print("Time to crack: %s seconds" % (time.time() - start_time))
            break



#close the file and exit
hashfile.close()
sys.exit()