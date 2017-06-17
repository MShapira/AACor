class Ligand:
    def __init__(self, id, residue=None):
        self.id = id
        self.residue = residue
        self.proteins = []

    def __str__(self):
        return '  ID: ' + self.id + '\n'

