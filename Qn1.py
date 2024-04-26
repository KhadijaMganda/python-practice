#!/usr/bin/env python
class StringManipulation:
    userInput =""

    def get_String(self, userInput):
        self.userInput = userInput
        return self.userInput
    
    def print_String(self):
        print(self.userInput)


userString = input("Enter the String to Manupulate: ")

strings = StringManipulation()

strings.get_String(userString.upper())
strings.print_String()
