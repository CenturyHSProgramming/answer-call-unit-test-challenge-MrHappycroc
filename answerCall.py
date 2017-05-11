# answerCall.py
# by Matteus

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()

# Make sure it returns a value

import re

def answerCall(callerCode, sameAreaCode, time):
    pattern=re.compile("[^\w']")
    intTime = int(pattern.sub('', time))
    if intTime > 2200 or intTime < 700:
        return False
    elif callerCode == 'F' or callerCode == 'R':
        return True
    elif callerCode == 'T':
        return False
    elif callerCode == 'U' and sameAreaCode == True:
        return True
    else:
        return False
        

if __name__ == '__main__':
    print(answerCall('U',False,'10:00'))
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
