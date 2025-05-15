import itertools

"""
adjacency = [
    [0, 500, 200, 185, 205],
    [500, 0, 305, 360, 340],
    [200, 305, 0, 320, 165],
    [185, 360, 320, 0, 302],
    [205, 340, 165, 302, 0]
]
"""

my_adjacency = [
    [0,  10, 12,  2,  30, 30],
    [10,  0, 11,  30,  4, 30],
    [12, 11,  0,  30, 30,  6],
    [2,  30, 30,  0,   3,  7],
    [30,  4, 30,  3,   0,  5],
    [30, 30,  6,  7,   5,  0]
]

my_route = 'DABEFCD'

def letter_to_num(s):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out = ''
    for i in s:
        out += str(alpha.index(i))
    return out

def cost(route=my_route, adjacency=my_adjacency):
    route = letter_to_num(route.replace('-', ''))
    cost = 0
    spot = route[0]
    for i in route:
        cost+=adjacency[int(spot)][int(i)]
        spot = i
    return cost

def calc_all(vertices="ABCDEF", adjacency=my_adjacency):
    permutations = itertools.permutations(vertices)
    costs = {}
    for p in permutations:
        p = ''.join(p)
        costs[p] = cost(p + p[0], adjacency)
    return costs



"""
routes = [
    "D-A-B-E-F-C-D",
    "B-E-D-A-C-F-B",
    "C-F-E-D-A-B-C",
    "A-D-E-B-C-F-A"
]

for i in routes:
    print(cost(i))
"""


"""
my_dict = calc_all()
my_max = max(my_dict, key=my_dict.get)
print(my_max)
print(my_dict[my_max])
"""
