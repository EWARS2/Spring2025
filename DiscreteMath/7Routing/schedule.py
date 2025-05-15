#WIP
EMPTY_CHAR = '-'

my_preference = 'ABCDEFGHIJK'
my_project = {
    'A': [ 2, ''],
    'B': [ 4, ''],
    'C': [10, ''],
    'D': [15, ''],
    'E': [ 7, 'AB'],
    'F': [ 3, 'B'],
    'G': [ 4, 'CD'],
    'H': [ 5, 'CD'],
    'I': [15, 'EF'],
    'J': [ 5, 'H'],
    'K': [20, 'IG']
}

def schedule(pref=my_preference, project=my_project, processors=2):
    # Create strings for each output and processor
    o = []
    p = []
    for i in range(processors):
        o.append('')
        p.append(EMPTY_CHAR)

    # Run until all tasks have completed
    t = 0
    while len(pref) > 0:
        # For every processor,
        for i in range(len(p)):
            # assign it a task that is not taken
            # by checking if the current task is valid
            # TODO: precedence
            x = 0
            while p[i] not in pref:
                if pref[x] in p:
                    x += 1
                else:
                    p[i] = pref[x]
                if x >= len(pref):
                    p[i] = EMPTY_CHAR
                    break


        # Remove finished tasks from queue
        for i in p:
            if i != EMPTY_CHAR:
                project[i][0] -= 1
                if project[i][0]<=0:
                    pref = pref.replace(i, '')


        # Update output
        for i in range(len(p)):
            o[i] += p[i]


    print(o)

schedule()