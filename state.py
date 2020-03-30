# Cuan O'Conchuir
# Classes used in Thompsons Construction

class State:
    # Every state has 0, 1 or 2 edges from it.
    edges = []

    # Lavel for the arrows. None means epsilon.
    label = None

    # Constructor for the class.
    def __init__(self, label = None, edges = []):
        self.edges = edges
        self.label = label

class Frag:
    # Start state of NFA fragment
    start = None
    # Accept state of NFA fragment
    accept = None
    
    # Constructor.
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


def shunt(infix):
    # Convert input to a stack-ish list (LIFO)
    infix = list(infix) [::-1]

    # Operator stack.
    # temporarily holds output to be put in the stack
    opers = []

    # Output list.
    postfix = []

    # Operator prescedence. (numbers used are arbitrary)
    # Must tell python with a dictionary.
    prec = {'*':100, '.':80, '|':60, ')':40, '(':20}

    # Loop through the input one character at a time.
    while infix:
    # pop a character from the input
        # remove last element then return
        c = infix.pop()

        # Decide what to do based on the character.
        if c == '(':
            # push an open bracket to the opers stack
            opers.append(c)
        elif c == ')':
            # Pop the operators stack until you find an (.
            while opers[-1] != '(':
                postfix.append(opers.pop())
            # Get rid of the '('.
            opers.pop()
        elif c in prec:
            # if there is an operator at the top of the stack with higher prescedence push them before current operator
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            # Push c to the operator stack
            opers.append(c)
        # typically we push the character to output
        else:
            postfix.append(c)

    # Pop all operators to the output.
    # take the last element off the end of opers and append that to postfix
    while opers:
        postfix.append(opers.pop())

    # Convert output list to string.
    # Join the elements of the list, convert them to strings
    return ''.join(postfix)



def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]# convert to a list

    # will keep track of all fragments created from postfix regex
    nfa_stack = []


    while postfix:
        # loop through reg expression
        # Pop a character from postfix.
        c = postfix.pop()
        if c == '.':
            # pop two fragments off the stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Point frag2s accept state at frag1s start state
            frag2.accept.edges.append(frag1.start)
            # Create new instance of fragment to represent the new NFA.
            newfrag = Frag(frag2.start, frag1.accept)
        elif c == '|':
            # Pop two fragments off the stack.
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Create new start and accept states.
            accept = State()
            start = State(edges = [frag2.start, frag1.start])
            # Point the old accept states at the new one.
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            newfrag = Frag(start, accept)
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges = [frag.start, accept])
            # Point the arrows
            frag.accept.edges = ([frag.start, accept]) 
            newfrag = Frag(start, accept)
        else:
            accept = State()
            start = State(label = c, edges = [accept])
            newfrag = Frag(start, accept)
        
        # Push the new NFA to the NFA stack
        nfa_stack.append(newfrag)


    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()


def match(regex, s):
    # This function will return True if and only if the regular expression
    # regex (fully) matches the string s. It returns false otherwise

    # NFA is Non-deterministic finite automata
    # Compile the regular expression into an NFA.
    nfa = regex_compile(regex)
    # Ask the NFA if it matches the string s.
    return nfa

print(match("a.b|b*", "bbbbbbbbbbb"))
