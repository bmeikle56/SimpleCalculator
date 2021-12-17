#Simple Calculator

#strings that begin or end with an operation are invalid
#number of parentheses %2=0 and #( = #)
#() is ignored
#Operation object is 

from Exceptions import DivideByZeroException, OperatorSyntaxException, ParenthesesSyntaxException, UndefinedCharacterException


class SimpleCalculator:
    def __init__(self):
        inp = input("Enter your 4-function calculation: ")
        self.operation = inp

    def getOpStr(self):
        return self.operation

    def __isOperator(char):
        #private method
        #send this method only one character
        match char:
            case "*" | "/" | "+" | "-":
                return True
            case _:
                return False

    def __isInvalid(char):
        #private method
        #send this method only one character
        #would be more efficient to check invalid characters but this is simpler for now
        match char:
            case "*" | "/" | "+" | "-" | "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" | " ":
                return False
            case _:
                return True

    def __parseString(rawStr, self):
        #private method
        #removes white space AND accounts for bad parentheses
        #initial traversal of the string

        #WILL concatenate number -> "3 1     +4" becomes "31+4" = 35

        numOfParen = 0
        newStr = ""
        lastChar = ""
        try:
            for i in range(rawStr.len()):
                currChar = rawStr[i]

                if (self.__isInvalid(currChar)):
                    raise UndefinedCharacterException()

                if (i > 0):
                    #set lastChar to be the last character, which you can only do
                    #after the first index
                    lastChar = rawStr[i - 1]

                if (numOfParen < 0):
                    #) without a ( before it
                    break #failure
                elif (self.__isOperator(lastChar) & self.isOperator(currChar)):
                    raise OperatorSyntaxError() #failure
                elif (currChar != ' '):
                    newStr += currChar

                if (currChar == '('):
                    numOfParen += 1
                elif (currChar == ')'):
                    numOfParen -= 1

            if (numOfParen != 0):
                raise ParenthesesSyntaxError() #failure
        except ParenthesesSyntaxError as p:
            print(p.message)
        except OperatorSyntaxError as o:
            print(o.message)
        
        return newStr

    def interpret(self):
        newStr = self.__parseString(self)
            
        return newStr #keep for now to run the program





    
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
