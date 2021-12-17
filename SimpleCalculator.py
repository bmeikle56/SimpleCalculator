#Simple Calculator

#strings that begin or end with an operation are invalid
#number of parentheses %2=0 and #( = #)
#() is ignored
#Operation object is 

from Exceptions import DivideByZeroError, ParenthesesSyntaxError


class SimpleCalculator:
    def __init__(self):
        inp = input("Enter your 4-function calculation: ")
        self.operation = inp

    def getOpStr(self):
        return self.operation

    def __parseString(rawStr):
        #private method
        #removes white space AND accounts for bad parentheses
        #initial traversal of the string

        #WILL concatenate number -> "3 1     +4" becomes "31+4" = 35

        numOfParen = 0
        newStr = ""
        lastChar = ""
        try:
            for i in range(rawStr.len()):
                if (i > 0):
                    #set lastChar to be the last character, which you can only do
                    #after the first index
                    lastChar = rawStr[i - 1]
                if (numOfParen < 0):
                    #) without a ( before it
                    break #failure
                elif (lastChar)
                elif (rawStr[i] != ' '):
                    newStr += rawStr[i]
                if (rawStr[i] == '('):
                    numOfParen += 1
                elif (rawStr[i] == ')'):
                    numOfParen -= 1

            if (numOfParen != 0):
                raise ParenthesesSyntaxError() #failure
        except ParenthesesSyntaxError as p:
            print(p.message)
        
        return newStr

    def interpret(self):
        rawStr = getOpStr(self)
        
        #eliminate white space to make it simpler
        str = __removeWhiteSpace(rawStr)


            
        





    
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if (b == 0):
            raise DivideByZeroError()
        return a / b
