# Cuan O'Conchuir
# Classes used in Thompsons Construction

class State:
    """
    A State with one or two edges, all edges labeled by label
    """
    def __init__(self, label = None, edges = []):
        # Every state has 0, 1, or 2 edges from it
        self.edges = edges
        # Label for the arrows. None meas epsilon
        self.label = label

class Frag:
    """
    An NFA fragment with a start and accept state
    """
    def __init__(self, start, accept):
        # Start state of NFA fragment
        self.start = start
        # Accept state of NFA fragment
        self.accept = accept

def shunt(infix):
    """
    Return the infix regular expression in postfix.
    """
    # Convert input to a stack-ish list (LIFO)
    infix = list(infix) [::-1]

    # Operator stack.
    # temporarily holds output to be put in the stack
    opers = []

    # Postfix regular expression.
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

def compile(infix):
    """
    Return an NFA fragment, representing the infix regular expression
    """
    # Convert infix to postfix
    postfix = shunt(infix)
    # Make postfix a stack of characters
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
            # The new start state is frag2's
            start = frag2.start
            # The new accept state is frag1's
            accept = frag1.accept
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
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges = [frag.start, accept])
            # Point the arrows
            frag.accept.edges = ([frag.start, accept]) 
        else:
            accept = State()
            start = State(label = c, edges = [accept])

        # Create new instance of Frag to represent the new NFA
        newfrag = Frag(start, accept)
        # Push the new NFA to the NFA stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()

def followes(state, current):
    """
    Add a state to a set and follow all of the e(psilon) arrows.
    """
    # Only do something when we havent already seen the state.
    if state not in current:
        # Put the state itself in current.
        current.add(state)
        # See whether state is labelled by e(psilon).
        if state.label is None:
            # Loop through the states pointed to by this state.
            for x in state.edges:
                # Follow all of their e(psilon)s too.
                followes(x, current)

def match(regex, s):
    """
    This function will return True if and only if the regular expression
    regex (fully) matches the string s. It returns false otherwise
    """
    # NFA is Non-deterministic finite automata
    # Compile the regular expression into an NFA.
    nfa = compile(regex)
    # Try to match the regular expression to the string s.
    # Current set of states.
    current = set()
    # Add the first state, and follow all e(psilon) arrows.
    followes(nfa.start, current)
    # Previous set of states.
    previous = set()

    # loop through characters in s.
    for c in s:
        # keep track of where we were.
        previous = current
        # Create a new empty set for states we're about to be in.
        current = set()
        # Loop through the previous states
        for state in previous:
            # Only folow arrow not labelled by e(psilon).
            if state.label is not None:
                # If the label of the state is equal to the character we've read:
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    followes(state.edges[0], current)

    # Ask the NFA if it matches the string s.
    return nfa.accept in current
