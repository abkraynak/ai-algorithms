# domain.py

class Domain(list):
    def __init__(self, set: list):
        list.__init__(self, set)
        self._hidden = []
        self._states = []

    def reset_state(self):
        self.extend(self._hidden)
        del self._hidden[:]
        del self._states[:]

    def push_state(self):
        self._states.append(len(self))

    def pop_state(self):
        d = self._states.pop() - len(self)
        if d:
            self.extend(self._hidden[-d:])
            del self._hidden[-d:]

    def hide_value(self, value):
        list.remove(self, value)
        self._hidden.append(value)