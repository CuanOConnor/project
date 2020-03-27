# Cuan O Conchuir
# Shunting yard algorithm for regular expressions

# Input
infix = "(a|b).c*"
print("Input is: ", infix)
#Expected output: "ab|c*."
# a or b followed by any number of c's
print("Expected: ", "ab|c*.")

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
            postfix.append(opers.push())
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
postfix = ''.join(postfix)

# Print the result.
print("Output is:", postfix)
