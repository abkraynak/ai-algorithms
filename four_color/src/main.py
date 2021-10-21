# main.py

import time as tme

from problem import Problem
from solve import BacktrackingSolver, BacktrackingForwardCheckingSolver, MinConflictsSolver

# Variables: the US states
# Domains: possible values for the US states; the four colors 
# Constraints: conditions on the values held by variables; connected states cannot have same color

states = ['NC', 'SC', 'VA', 'TN', 'KY', 'WV', 'GA', 'AL', 'MS', 'FL']
borders = [('NC', 'SC'), ('NC', 'VA'), ('NC', 'TN'), ('NC', 'GA'), ('SC', 'GA'),
           ('VA', 'TN'), ('VA', 'KY'), ('VA', 'WV'), ('TN', 'KY'), ('TN', 'GA'), 
           ('TN', 'AL'), ('TN', 'MS'), ('KY', 'WV'), ('GA', 'AL'),
           ('GA', 'FL'), ('AL', 'MS'), ('AL', 'FL')]
colors = ['red', 'yellow', 'green', 'blue']

def check_border(variables, *args):
    z = list(zip(variables, args))
    return z[0][1] != z[1][1]

def solve(method):
    # Set up the problem with the variables, constraints, and domains
    problem = Problem(method)
    problem.add_variables(states, colors)
    for state in states:
        border_list = [borders[index] for (index, border) in enumerate(borders)]
        if border_list:
            for border in border_list:
                problem.add_constraint(check_border, list(border))

    # Solve and record the time
    start = tme.time()
    solution = problem.get_solution()
    end = tme.time()
    duration = end - start

    # Print results
    print(method.get_title(), ':', duration, 'seconds')
    print('Solution =', solution)
    print()

if __name__ == '__main__':
    methods = [BacktrackingSolver(), BacktrackingForwardCheckingSolver(), MinConflictsSolver()]
    for method in methods:
        solve(method)