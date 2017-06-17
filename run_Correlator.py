from PDBUtility import *

pdb_list, folder_path = get_pdbs_with_ligands_list()
proteins_list = parse_pdb_structure(pdb_list, folder_path)
for protein in proteins_list:
    print(protein)
    print(protein.ligands)
    print('-----')
ligand_list = protein_clasterization_via_ligand(proteins_list)
for ligand in ligand_list:
    print(ligand.id)
    print(ligand.proteins)
    print('------')