# Project Submission README for GraphTheory 2020
### Cuan O'Conchuir

***Running The Program***

The main file that contains the core of the submission is regex.py.
This can be run on its own, and the classes and methods will compile as intended.
regex.py contains output of assertions to test on various regular expressions provided
another way regex.py can be run is by using the provided myscripts.py to compile the program using an import of the classes and methods.
this will return a boolean value of true or false depending on the input values of regular expressions.

## Contents and structure

***regex.py contains 2 classes and 4 methods.***

***class State:*** 
Is a definition for a state with one or two edges, with all edges labelled by label.

***class Frag:*** 
Is an NFA fragment with a start and accept state.

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
- Returns the NFS if it matches the string
           
## Testing

The program also includes some test cases at the end in the form of an assert statement that is looped for how many test cases are written.
           
              




