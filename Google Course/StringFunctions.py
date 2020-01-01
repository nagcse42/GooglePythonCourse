import sys

#Checking type of string
def checkTypeOfString(inputString):
    if inputString.isalpha():
        return 'Alpha'
    elif inputString.isdigit():
        return 'Digit'
    elif inputString.isspace(): 
        return 'Space'

def stringStartAndEndCheck(inputString, isStartCheck, checkString):
    if isStartCheck:
        return (inputString+' starts with '+ checkString) if inputString.startswith(checkString) else (inputString+' not starts with '+ checkString)
    else :
        return (inputString+' ends with '+ checkString) if inputString.endswith(checkString) else (inputString+' not ends with '+ checkString)

def main():
    print 'String'
    print checkTypeOfString('Nagarjuna')
    print stringStartAndEndCheck('Nagarjuna', True, 'Nag')
    print stringStartAndEndCheck('Nagarjuna', True, 'Arjun')
    print stringStartAndEndCheck('Nagarjuna', False, 'una')
    print stringStartAndEndCheck('Nagarjuna', False, 'UNA')

if __name__ == "__main__":
        main()