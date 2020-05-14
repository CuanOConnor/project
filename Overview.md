# Overview of The Project
*This Doc serves as a guide/wiki on the project, and tells you how to use and interact with the program from an outside view*
### Author: Cuan O'Conchuir

***Introduction***

Hello and welcome to my project submission for Graph Theory 2020.

It involves writing a program in Python3 to execute regular expressions on
strings using an algorithm known as Thompson’s construction, named after
the well-known computer scientist Ken Thompson. 

The problem presented to us was to create, using research and resources available to use, a program or engine that could take regular expressions and to build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.

A regular expression is a string containing a series of characters, some of which may have a special meaning. For example, the three characters ., |, and * have the special meanings concatenate, or, and Kleene star respectively. 

For example, the regular expression 0.1 means a 0 followed by a 1, 0|1 means a 0 or a 1, and 1* means any number of 1’s.


***Running The Program***

- The main file that contains the core of the submission is ***regex.py***.
- This can be run on its own, and the classes and methods will compile as intended.
- ***regex.py*** contains output of assertions to test on various regular expressions provided.
- Another way ***regex.py*** can be run is by using the provided ***myscripts.py*** to compile the program using an import of the classes and methods.
- This will return a boolean value of true or false depending on the input values of regular expressions.

- The main executable for the program is the ***myscripts.py*** file.
- This file calls its core functionality from the ***regex.py*** file.
- To begin you must run the command ***python3 myscripts.py***.
- Additional help can be displayed to the screen using the same command but with the --help or -h suffix.
- E.g. ***python3 myscripts.py --help***
- This will show how to run the program and what running the program entails.




***References:***
https://stackoverflow.com/questions/40324492/how-continue-execute-program-after-assertion-in-python/40324537

https://www.tutorialspoint.com/python3/assertions_in_python.htm

https://airbrake.io/blog/python-exception-handling/python-assertionerror

https://docs.python.org/3/library/argparse.html

https://docs.python.org/2/howto/argparse.html
