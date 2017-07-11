class Protein:
    def __init__(self, id, name=None, sequence=None, structure=None):
        self.id = id
        self.name = name
        self.sequence = sequence
        self.ligands = []
        self.structure = structure

    def __str__(self):
        return '  ID: ' + self.id + '\n' + \
               '  Name: ' + self.name + '\n' + \
               '  Sequence: ' + self.sequence + '\n'


def find_protein_with_id(proteins, id):
    for protein in proteins:
        if protein.id == id:
            return protein
        else: return None


# def find_protein_with_group(proteins, group):
#     for protein in proteins:
#         if protein.group == group:
#             return protein
#         else: return None
