# problem.py

from domain import Domain
from constraint import Constraint

class Problem(object):
    def __init__(self, solver = None):
        self._solver = solver
        self._constraints = []
        self._variables = {} # Variable and color

    def add_variable(self, variable: str, domain: list):
        domain = Domain(domain)
        self._variables[variable] = domain

    def add_variables(self, variables: list, domain: list):
        self.all_variables = variables
        for variable in variables:
            self.add_variable(variable, domain)

    def add_constraint(self, constraint, variables = None):
        constraint = Constraint(constraint)
        self._constraints.append((constraint, variables))

    def _get_args(self):
        domains = self._variables.copy()
        constraints = self._constraints
        vconstraints = {}
        for variable in domains:
            vconstraints[variable] = []
        for constraint, variables in constraints:
            for variable in variables:
                vconstraints[variable].append((constraint, variables))
        for domain in domains.values():
            domain.reset_state()
        return domains, constraints, vconstraints

    def get_solution(self):
        domains, constraints, vconstraints = self._get_args()
        if not domains:
            return None
        self._solution = self._solver.solve(domains, constraints, vconstraints)
        return self._solution