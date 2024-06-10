class Magazine:
    def __init__(self, name, category):
        self.id = None
        self._name = name
        self.category = category
    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f'<Magazine {self.name}>'
