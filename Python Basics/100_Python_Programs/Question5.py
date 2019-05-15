##Define a class which has at least two methods:
##getString: to get a string from console input
##printString: to print the string in upper case.
##Also please include simple test function to test the class methods.
##
##Hints:
##Use __init__ method to construct some parameters

class GetPrintString():

    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input('Enter a string:')

    def printString(self):
        print(self.string.upper())


def main():
    test = GetPrintString()
    test.getString()
    test.printString()

    test1 = GetPrintString()
    test1.getString()
    test1.printString()

if __name__ == '__main__':
    main()
