class Variable(object):
    def __init__(self, name: str):
        self.name = name
    
    def __repr__(self):
        return self.name

Unassigned = Variable('Unassigned')