class Ligand:
    def __init__(self, id, name=None, residue=None):
        self.id = id
        self.name = name
        self.residue = residue
        self.proteins = []

    def __str__(self):
        return '  ID: ' + self.id + '\n' + \
               '  Name: ' + self.name + '\n'

    # looking_for_entity: by default "True" (if we need ligand by itself), if "False": we are checking out if we already
        #  have such ligand
    def find_ligand_with_id(ligands, id, looking_for_entity=True):
        if not looking_for_entity:
            for ligand in ligands:
                if ligand.id == id:
                    return True
                else:
                    return False
        else:
            for ligand in ligands:
                if ligand.id == id:
                    return ligand
                else:
                    return None