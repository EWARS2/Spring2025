# Created by Ethan Reed, Feb 18 2025 for Digital Logic
# with the help of ChatGPT in variable typing for eval()

import itertools

SYMS_ONLY = ['<->', '<=>']
SYMS_IF   = ['->', '=>']
SYMS_NOT  = ['~', '-', '_']
SYMS_AND  = ['^', '&', '*', '.']
SYMS_OR   = ['v', '+']
SYMS_XOR  = ['xor']
SYMS_NAND = ['nand']  # TODO
SYMS_NOR  = ['nor']  # TODO

'''
Colors from here:
https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
'''

class col:
    T = '\033[92m'
    F = '\033[93m'
    ERR = '\033[91m'
    END = '\033[0m'

# Everything to print a truth table
def truth_table(expr):
    expr, var = eval_expr(expr)
    try:
        table(expr, var)
    except SyntaxError as e:
        print(col.ERR)
        print(e)
        print("Be sure to add parenthesis to NOTs.")
        print("Otherwise Python thinks you're trying to treat a NOT as a value!\n")
        print("E.g. 'Q XOR ~R' becomes 'Q XOR (~R)'")
        print("If there's an elegant way to fix this, please let me know.")
        print(col.END)

def eval_expr(expr):
    print("\nInput:             ", expr)
    expr, var = assess(expr)
    print("In Python Syntax:  ", expr, '\n')
    return expr, var

def assess(expr):
    # Convert expression to Python statement.
    # Order of replacement matters.
    expr = expr.lower()
    for i in SYMS_ONLY:
        expr = expr.replace(i, " == ")
    for i in SYMS_IF:
        expr = expr.replace(i, " <= ")
    for i in SYMS_NOT:
        expr = expr.replace(i, " not ")
    for i in SYMS_AND:
        expr = expr.replace(i, " and ")
    for i in SYMS_OR:
        expr = expr.replace(i, " or ")
    for i in SYMS_XOR:
        expr = expr.replace(i, " ^ ")

    # Isolate & get variables
    var = expr
    for i in ['and','not','or']:
        var = var.replace(i, ' ')
    var = sorted(set(filter(str.isalpha, var)))

    return expr, var

# Print truth table
def table(expr, var):
    # Header
    for i in var:
        print(f'{i:10}', end=' ')
    print()

    # Row
    for values in itertools.product([False, True], repeat=len(var)):
        # Table Inputs
        for j in values:
            if j:
                print(col.T, end='')
            else:
                print(col.F, end='')
            print(f'{j:<10}', end=' ')

        # Table Outputs
        result = eval(expr, dict(zip(var, values)))
        if result:
            print(col.T, end='')
        else:
            print(col.F, end='')
        print(result)

    print(col.END)

# Main code
truth_table("(A and C) v B")
truth_table("~(~(A AND C) AND ~B)")
