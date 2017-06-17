from PDBUtility import get_pdbs_with_ligands_list, parse_pdb_structure

pdb_list, folder_path = get_pdbs_with_ligands_list()
proteins_list = parse_pdb_structure(pdb_list, folder_path)
for protein in proteins_list:
    print(protein.name)
    print(protein.id)
    print(protein.ligands)
    print('--------------')