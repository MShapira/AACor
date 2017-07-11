from PDBUtility import *

pdb_list, folder_path = get_pdbs_with_ligands_list()
proteins_list = construct_proteins_list(pdb_list, folder_path)
for protein in proteins_list:
    for ligand in protein.ligands:
        atomic_neighbor_search(ligand, protein, 2.0)