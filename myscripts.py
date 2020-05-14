# Cuan O'Conchuir
# Run a few regular expressions

import regex
import argparse
import textwrap

'''
Argument Parser that displays this simple help message when -h or --help is included as a suffix to running the file
e.g. python3 myscripts.py --help
'''
parser = argparse.ArgumentParser(
    prog="Regex.py running on myscripts.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
            Comparing a regular expression string to a users input string.
             --------------------------------------------------------------
                 - Authors: Ian McLoughlin and Cuan O'Conchuir
                 - Upon running the program the user is prompted to enter a string that they want to compare to the regular expression.
                 - The program then prompts them for a string that will be the regular expression.
                 - Finally, the program will then use the match() method in the regex.py file to compare the two and display either TRUE or FALSE
            '''))

args = parser.parse_args()

'''
User input segment that takes in input for both the regex and the user string
compares the two using the match() function in regex.py
Displays the result as either TRUE or FALSE
'''
user_var = input("Please enter the string you wish to compare to the regular expression: ")
regex_var = input("Now enter the regular expression you wish to compare it to: ")

print("Comparing regex: " + regex_var + " to " + user_var) 
print("Result: ")
print(regex.match(regex_var, user_var))


