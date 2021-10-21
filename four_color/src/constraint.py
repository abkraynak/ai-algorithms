# constraint.py

from variable import Unassigned

class Constraint(object):
    def __init__(self, func, assigned = True):
        self._func = func
        self._assigned = assigned
    
    def __call__(self, variables, domains, assignments, forwardcheck = False, _unassigned = Unassigned):
        params = [assignments.get(x, _unassigned) for x in variables]
        missing = params.count(_unassigned)
        if missing:
            return (self._assigned or self._func(variables, * params)) and (not forwardcheck or self.forward_check(variables, domains, assignments))
        return self._func(variables, *params)

    def forward_check(self, variables, domains, assignments, _unassigned = Unassigned):
        unassigned_variable = _unassigned
        for v in variables:
            if v not in assignments:
                if unassigned_variable is _unassigned:
                    unassigned_variable = v
                else:
                    break

        else:
            if unassigned_variable is not _unassigned:
                domain = domains[unassigned_variable]
                if domain:
                    for val in domain[:]:
                        assignments[unassigned_variable] = val
                        if not self(variables, domains, assignments, forwardcheck = False):
                            domain.hide_value(val)
                    del assignments[unassigned_variable]
                if not domain:
                    return False
        return True