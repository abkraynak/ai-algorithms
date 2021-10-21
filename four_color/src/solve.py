# solve.py

import random
from variable import Unassigned

class Solver(object):
    def __init__(self):
        self.counter = 0

class BacktrackingSolver(Solver):
    def __init__(self):
        super().__init__()

    def get_title(self):
        return 'Backtracking'

    def backtracking(self, solutions: list, domains: dict, vconstraints: dict, assignments: dict, one: bool):
        # Minimum remaining value
        l = [(len(domains[variable]), variable) for variable in domains]
        l.sort()
        for item in l:
            if item[-1] not in assignments: # Unassigned varaible
                break
        else: # All variables assigned
            solutions.append(assignments.copy())
            return solutions

        variable = item[-1]
        assignments[variable] = Unassigned
        for value in domains[variable]:
            assignments[variable] = value
            for constraint, variables in vconstraints[variable]:
                self.counter += 1
                if not constraint(variables, domains, assignments):
                    break
            else:
                self.backtracking(solutions, domains, vconstraints, assignments, one)
                if solutions and one:
                    return solutions
        del assignments[variable]
        return solutions

    def solve(self, domains: dict, constraints: list, vconstraints: dict):
        self.counter = 0
        solutions = self.backtracking([], domains, vconstraints, {}, False)
        return solutions and solutions[0] or None

class BacktrackingForwardCheckingSolver(Solver):
    def __init__(self, forwardcheck = True):
        super().__init__()
        self._forwardcheck = forwardcheck

    def get_title(self):
        return 'Backtracking with Forward Checking'

    def backtracking(self, solutions: list, domains: dict, vconstraints: dict, assignments: dict, one: bool):
        # Minimum remaining value
        l = [(len(domains[variable]), variable) for variable in domains]
        l.sort()
        for item in l:
            if item[-1] not in assignments: # Unassigned variable
                break
        else: # All variables assigned
            solutions.append(assignments.copy())
            return solutions

        variable = item[-1]
        assignments[variable] = Unassigned
        pushdomains = [domains[x] for x in domains if x not in assignments]
        for value in domains[variable]:
            assignments[variable] = value
            for domain in pushdomains:
                domain.push_state()
            for constraint, variables in vconstraints[variable]:
                self.counter += 1
                if not constraint(variables, domains, assignments, pushdomains):
                    break
            else:
                self.backtracking(solutions, domains, vconstraints, assignments, one)
                if solutions and one:
                    return solutions
            for domain in pushdomains:
                domain.pop_state()
        del assignments[variable]
        return solutions

    def solve(self, domains: dict, constraints: list, vconstraints: dict):
        self.counter = 0
        solutions = self.backtracking([], domains, vconstraints, {}, False)
        return solutions and solutions[0] or None

class MinConflictsSolver(Solver):
    def __init__(self, steps = 1000):
        super().__init__()
        self._steps = steps

    def get_title(self):
        return 'Min-Conflicts'

    def min_conflict(self, domains, vconstraints):
        self.counter = 0
        assignments = {}

        # Initial assignments done randomly
        for variable in domains:
            assignments[variable] = random.choice(domains[variable])
        
        for _ in range(self._steps):
            conflict = False
            l = list(domains.keys())
            random.shuffle(l)
            for variable in l:
                # Check for conflicts
                for constraint, variables in vconstraints[variable]:
                    self.counter += 1
                    if not constraint(variables, domains, assignments):
                        break
                else:
                    continue

                # Find the least conflicts
                mincount = len(vconstraints[variable])
                minvalues =[]
                for value in domains[variable]:
                    assignments[variable] = value
                    count = 0
                    for constraint, variables, in vconstraints[variable]:
                        self.counter += 1
                        if not constraint(variables, domains, assignments):
                            count += 1
                    if count == mincount:
                        minvalues.append(value)
                    elif count < mincount:
                        mincount = count
                        del minvalues[:]
                        minvalues.append(value)
                # Choose at random from minvalues for new assignment
                assignments[variable] = random.choice(minvalues)
                conflict = True
            if not conflict:
                return assignments
        return None

    def solve(self, domains, constraints, vconstraints):
        return self.min_conflict(domains, vconstraints)