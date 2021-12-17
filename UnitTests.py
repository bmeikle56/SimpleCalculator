#Unit Tests for this project
#Followed Test Driven Development principles
#These were created before or simultaneously with code development

from SimpleCalculator import SimpleCalculator



class UnitTests:
    def main():
        testStarFirstChar()
        return

    def testStarFirstChar():
        test = "* 8 + 7 - 2"
        SimpleCalculator sc1 = SimpleCalculator(test)
        print(sc1.interpret(test))
        return

    def testMissingParentheses():
        test = "5 - (4 - 3 + 2"
        SimpleCalculator sc1 = SimpleCalculator(test)
        print(sc1.interpret(test))
        print("Expected: Failure")
        return

    def testBasicOO():
        test = "2 * 10 - 3 * 4"
        SimpleCalculator sc1 = SimpleCalculator(test)
        print(sc1.interpret(test))
        print("Expected: -2")
        return
