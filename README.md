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

## Install necessary packages/utilities and python3

- This program was developed and run in ***python3*** on a ***linux virtual machine***, it is advised that when trying to run/edit the files that you do the same.
- The first command you should run is ***sudo apt update***. 
  - This will attempt to download/update your Linux/Debian packages so they are up to date.
- Then you can choose to upgrade the files you downloaded using ***sudo apt upgrade*** (not entirely necessary)
- Next you'll likely need git to pull/push any files from the repository.
  - Install using the command ***sudo apt install git***
- We'll need VIM in order to edit/view our code in a more streamlines way.
  - use ***sudo apt-get install vim***
- Python3 usually comes pre-intalled on linux, however if you do not have it use:
  - ***sudo apt-get install python3***
- You might also want wget for, which is useful for downloading files
  - ***sudo apt install wget***
- Finally, you may want to clone this repository to your own computer/VM
  - simply use the command ***git clone https://github.com/G00300230/project.git***
  - use ***ls*** to view the files/folders
  - ***cd [folder name]*** might be necessary for you to navigate into the correct folder (named ***project*** for this project) to access the files.

## Running The Program

- The main file that contains the core of the submission is ***regex.py***.
  - Run using ***python3 regex.py***
- This can be run on its own, and the classes and methods will compile as intended.
- However it contains no screen output, all of which is contained in other files and classes. (explained below)
- Another way ***regex.py*** can be run is by using the provided ***myscripts.py*** to compile the program using an import of the classes and methods.
  - Run using ***python3 myscripts.py***
  - Also contains an argparse call that will allow you to at least perform a ***--help*** action on the file
  - Like so: ***python3 myscripts.py --help***
  - This will display some usefull information about the file and how to use it.
- ***myscripts.py*** will accept user input. It will take in two *string* values, one is the regular expression that the user wishes to use, and the other is the string they wish to compare to the regular expression. This in turn will call the ***match()*** method from ***regex.py*** and compare the two strings as best it can, then it will return a boolean value of true or false depending on the input values of regular expressions and some output.
- Some test cases have also been written and are contained in the file ***testcases.py***

- The main executable for the program is the ***myscripts.py*** file.
- To begin you must run the command ***python3 myscripts.py***.
- All the code is available in the github repository and can be viewed at your leisure.


## Testing

The github repo contains a file which will allow you to run some test cases on a few pre-set strings.
- Assertions are used as a bases to test using boolean values.
- It compares the strings in the assertion tests using the ***match()*** method in ***regex.py***.
- ***try/except*** blocks are used in order to prevent the program having a fatal error and not loading the subsequent test cases.
  - as a result all test cases and their expected results are shown to the user.
  - Run using: ***Python3 testcases.py***
  - code available in the repository
  
## Contents and structure of the core working parts

***regex.py contains 2 classes and 4 methods.***

***class State:*** 
Is a definition for a state with one or two edges, with all edges labelled by label.

***class Frag:*** 
Is an NFA (a non-deterministic finite automaton) fragment with a start and accept state.

***def shunt:*** 
- Is our main shunting algorithm which takes in our infix regular expression and changes it to postfix
- It will take in and read operators in the expression assign them levels of prescedence and act on that.
- Using if elif structure it will decide what to pop() and when to pop() it then append to our postfix
           
***def compile:*** 
- Will return an NFA fragment, representing the infix regular expression
- Contains a call to shunt() to perform the above stated operations
- Converts it to a list
- From there we loop through the list and and pop() characters from the stack
- manages the start and accept states of the stack
- A new fragment is created at the end to represent our new NFA
- The new NFA is pushed to the NFA stack
             
***def followes:*** 
- Will add a state to a set and follow all of the e(psilon) arrows(edges)
- Checks if the state is already seen or not
- Loops through states edges
- Has a call to itself
      
***def match:*** 
- Will return true if the regular expression matches a string, returns false otherwise
- Compiles the regular expression into an NFA
- Try to match to string
- Defines current set of states
- Calls followes() ands adds the first state ad follows the edges
- Defines previous set of states
- Loops through the characters keeping track of the position
- Creates an empty set of states that it is about to be in
- If the label of the state is equal to the character read, the state is added to the end of the current edge
- Returns the NFA if it matches the string

Below is a simple Diagram of the anatomy of an NFA.
- Each one is a potential regular expression and its corresponding diagram.
- It shows the transitions through the NFA and how it is resolved.
- This is a good visual guide for how our program will process the NFA.

![Example NFA Diagram](https://github.com/G00300230/project/blob/master/NFADiagram.png)


## References

Information on apt and installing/updating using apt
- https://linuxize.com/post/how-to-use-apt-command/ 

Good resource for learning vim basics
- https://opensource.com/article/19/3/getting-started-vim 

Extra info on Automata and NFA
- https://www.javatpoint.com/non-deterministic-finite-automata 

Some code I used to help with Assertion fatal exceptions
- https://stackoverflow.com/questions/40324492/how-continue-execute-program-after-assertion-in-python/40324537 

Doc-style info on assertions and how to use them
- https://www.tutorialspoint.com/python3/assertions_in_python.htm

More info on assertion-error exception used in this program
- https://airbrake.io/blog/python-exception-handling/python-assertionerror

Argparse documentation and information, with code snippets as exmaples
- https://docs.python.org/3/library/argparse.html 

More info on argparse
- https://docs.python.org/2/howto/argparse.html 
