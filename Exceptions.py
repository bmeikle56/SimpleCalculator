#Exceptions

class ParenthesesSyntaxException(Exception):
    #((3 + 2)
    def __init__(self, message = "Improper parentheses syntax"):
        self.message = message
        super().__init__(self.message)

class DivideByZeroException(Exception):
    def __init__(self, message = "Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)

class OperatorSyntaxException(Exception):
    #"" * 4 + 1" or "6** - 3"
    def __init__(self, message = "Improper operator syntax"):
        self.message = message
        super().__init__(self.message)

class UndefinedCharacterException(Exception):
    def __init__(self, message = "Cannot use undefined character"):
        #"4 - 2 + f" or "gg8 / 8n + e"
        self.message = message
        super().__init__(self.message)