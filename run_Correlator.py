from PDBUtility import *

pdb_list, folder_path = get_pdbs_with_ligands_list()
proteins_list = construct_proteins_list(pdb_list, folder_path)
for protein in proteins_list:
    print(protein)
    print(protein.ligands)
    print('-----')
ligand_list = construct_ligands_list(proteins_list)
for ligand in ligand_list:
    print(ligand.id)
    print(ligand.proteins)
    print('------')