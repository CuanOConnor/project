# Cuan O'Conchuir
# Run a few regular expressions

import regex
import argparse
import textwrap

parser = argparse.ArgumentParser(
    prog="Regex.py running on myscripts.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
            Comparing a regular expression string to a users input string.
             --------------------------------------------------------------
                 - Upon running the program the user is promted to enter a string that they want to compare to the regular expression.
                 - The program then prompts them for a string that will be the regular expression.
                 - Finally, the program will then use the match() method in the regex.py file to compare the two and display either TRUE or FALSE
            '''))

args = parser.parse_args()
print(args)

user_var = input("Please enter the string you wish to compare to the regular expression: ")
regex_var = input("Now enter the regular expression you wish to compare it to: ")

print("Comparing regex: " + regex_var + " to " + user_var)

print(regex.match(regex_var, user_var))


