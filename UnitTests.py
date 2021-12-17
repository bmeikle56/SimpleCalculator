#Unit Tests for this project
#Followed Test Driven Development principles
#These were created before or simultaneously with code development

from SimpleCalculator import SimpleCalculator

class UnitTests:
    def main():
        print("Working")
        #self.testBeginner()
        #self.testBasicOO()
        #self.testMissingParentheses()
        #self.testStarFirstChar()
        return

    def testStarFirstChar():
        test = "* 8 + 7 - 2"
        sc1 = SimpleCalculator(test)
        print(sc1.interpret(test))
        print("Expected: Improper operator syntax")
        return

    def testMissingParentheses():
        test = "5 - (4 - 3 + 2"
        sc1 = SimpleCalculator(test)
        print(sc1.interpret(test))
        print("Expected: Improper parentheses syntax")
        return

    def testBasicOO():
        test = "2 * 10 - 3 * 4"
        sc1 = SimpleCalculator(test)
        print(sc1.interpret(test))
        print("Expected: -2")
        return

    def testBeginner():
        test = "2 + 2"
        sc1 = SimpleCalculator(test)
        print(sc1.interpret(test))
        print("Expected: 4")
        return