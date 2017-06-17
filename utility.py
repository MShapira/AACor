def write_to_file(filename, extension, data, folder_path):
    file = open(folder_path + "/" + filename + "." + extension, "w")
    file.write(data)
    file.close()

    return file


# looking_for_entity: by default "True" (if we need ligand by itself), if "False": we are checking out if we already
        #  have such ligand
def find_ligand_with_id(ligands, id):
    for ligand in ligands:
        if ligand.id == id:
            return ligand
        else:
            return None