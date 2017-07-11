from numpy import genfromtxt


# write to file
def write_to_file(filename, extension, data, folder_path):
    file = open(folder_path + "/" + filename + "." + extension, "w")
    file.write(data)
    file.close()

    return file


# find exact ligand
def find_ligand_with_id(ligands, id):
    for ligand in ligands:
        if ligand.id == id:
            return ligand
    return None


# construct the list of standard AA
def get_standard_aa():
    standard_res_list = []
    for res in genfromtxt('standard_residues.txt', dtype=None, delimiter=', '):
        standard_res_list.append(res.decode('UTF-8'))

    return standard_res_list