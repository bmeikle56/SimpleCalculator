#Exceptions

class ParenthesesSyntaxError(Exception):
    #((3 + 2)
    def __init__(self, message = "Improper parentheses syntax"):
        self.message = message
        super().__init__(self.message)

class DivideByZeroError(Exception):
    def __init__(self, message = "Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)

class OperatorSyntaxError(Exception):
    #"" * 4 + 1" or "6** - 3"
    def __init__(self, message = "Improper operator syntax"):
        self.message = message
        super().__init__(self.message)

class DivideByZeroError(Exception):
    def __init__(self, message = "Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)