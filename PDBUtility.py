import pypdb
import os
import time
from utility import write_to_file, find_ligand_with_id, get_standard_aa
from Bio.PDB import *
from protein import Protein
from ligand import Ligand
from Bio import SeqIO


# download pdb files from PDB db
def get_pdbs_with_ligands_list():
    pdb_list_query = pypdb.make_query('Ligand', querytype='AdvancedKeywordQuery')
    pdb_list = pypdb.do_search(pdb_list_query)
    protein_pdb_list = []
    for pdb in pdb_list[:3]:
        if isinstance(pypdb.get_all_info(pdb)['polymer'], list):
            if pypdb.get_all_info(pdb)['polymer'][0]['@type'] == 'protein':
                protein_pdb_list.append(pdb)
        else:
            if pypdb.get_all_info(pdb)['polymer']['@type'] == 'protein':
                protein_pdb_list.append(pdb)

    folder_path = 'results/' + str(time.ctime()).replace(':', '-').replace(' ', '_')
    os.makedirs(folder_path)

    for pdb in protein_pdb_list:
        pdb_structure = pypdb.get_pdb_file(pdb, filetype='pdb', compression=False)

        write_to_file(str(pdb), "pdb", pdb_structure, folder_path)

    return protein_pdb_list, folder_path


# getting sequence from .pdb file
def extract_sequence(file_name):
    file = open(file_name, 'r')
    seq = ''

    for record in SeqIO.parse(file, "pdb-seqres"):
        if len(record.seq) > len(seq):
            seq = record.seq

    file.close()
    return seq


# construction of protein list
def construct_proteins_list(protein_pdb_list, folder_path):
    parser = PDBParser(PERMISSIVE=1)
    proteins_list = []
    standard_res_list = get_standard_aa()

    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for pdb in protein_pdb_list:
            for pdb_file in filenames:
                if pdb in pdb_file:
                    protein = Protein(id=pdb)
                    protein.sequence = str(extract_sequence(folder_path + '/' + pdb_file))
                    protein.name = pypdb.get_all_info(pdb)['polymer']['macroMolecule']['@name']
                    structure = parser.get_structure('', folder_path + '/' + pdb_file)
                    protein.structure = structure
                    for model in structure:
                        for chain in model:
                            for residue in chain:
                                if residue.get_resname() not in standard_res_list:
                                    protein.ligands.append(residue)
                    proteins_list.append(protein)

    return proteins_list


# protein clasterization via ligand type
def construct_ligands_list(protein_list):
    ligands_list = []
    for protein in protein_list:
        if len(protein.ligands) != 0:
            for ligand in protein.ligands:
                meta_ligand = find_ligand_with_id(ligands_list, ligand.get_resname())
                if meta_ligand is not None:
                    meta_ligand.proteins.append(protein.id)
                else:
                    meta_ligand = Ligand(id=ligand.get_resname())
                    meta_ligand.residue = ligand
                    meta_ligand.proteins.append(protein.id)
                    ligands_list.append(meta_ligand)

    return ligands_list


# getting residue atoms
def get_residue_atoms(residue):
    atoms = []
    for atom in residue:
        atoms.append(atom)

    return atoms


# search for a atomic contacts between ligand and proteins residues
def atomic_neighbor_search(ligand_residue, protein, radius):
    ligand_atoms = get_residue_atoms(ligand_residue) # todo: get the class of the input data residue/ligand
    protein_atoms = []
    contacts = []

    for model in protein.structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    protein_atoms.append(atom)

    ns = NeighborSearch(protein_atoms)
    for atom in ligand_atoms:
        local_contact = ns.search(atom.get_coord(), radius, 'A')
        contacts.append(local_contact)

    print(contacts) # todo: construct pairs of the ligand_atom - protein_atom and save them to ligand entity
    print('--------')