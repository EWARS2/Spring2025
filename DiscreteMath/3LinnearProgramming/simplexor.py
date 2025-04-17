# Bazinga - Simplex method is as simple as it gets, but ironically
# it's quite complex.
# WIP
from math import sumprod

test = [0, 0, 0, 0]

objectives = [18, -15, 20, 9]
constraints = [
    [[2, -10, 4,  3], '>=', 36],
    [[3,  -5, 5, -6], '>=', 24]
]

def update(test, objectives, constraint_functions):
    set_objective = sumprod(test, objectives)
    constraints = []
    for i in constraint_functions:
        i[0] = sumprod(i[0], test)
        # Python is estupidamente and cannot directly .join non-strings
        constraints.append(" ".join(str(j) for j in i))
    print(constraints)

update()