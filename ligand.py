class Ligand:
    def __init__(self, id, name=None, residue=None):
        self.id = id
        self.name = name
        self.residue = residue
        self.proteins = []

    def __str__(self):
        return '  ID: ' + self.id + '\n' + \
               '  Name: ' + self.name + '\n'

