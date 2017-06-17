import pypdb
import os
import time
from utility import write_to_file
from Bio.PDB import PDBParser
from protein import Protein
from ligand import Ligand
from Bio import SeqIO


def get_pdbs_with_ligands_list():
    pdb_list_query = pypdb.make_query('Ligand', querytype='AdvancedKeywordQuery')
    pdb_list = pypdb.do_search(pdb_list_query)
    protein_pdb_list = []
    for pdb in pdb_list:
        if isinstance(pypdb.get_all_info(pdb)['polymer'], list):
            if pypdb.get_all_info(pdb)['polymer'][0]['@type'] == 'protein':
                protein_pdb_list.append(pdb)
        else:
            if pypdb.get_all_info(pdb)['polymer']['@type'] == 'protein':
                protein_pdb_list.append(pdb)

    folder_path = 'results/' + str(time.ctime()).replace(':', '-').replace(' ', '_')
    os.makedirs(folder_path)

    for pdb in protein_pdb_list[:15]:
        pdb_structure = pypdb.get_pdb_file(pdb, filetype='pdb', compression=False)

        write_to_file(str(pdb), "pdb", pdb_structure, folder_path)

    return protein_pdb_list, folder_path


def extract_sequence(file_name):
    file = open(file_name, 'r')
    seq = ''

    for record in SeqIO.parse(file, "pdb-seqres"):
        if len(record.seq) > len(seq):
            seq = record.seq

    file.close()
    return seq


def parse_pdb_structure(protein_pdb_list, folder_path):
    parser = PDBParser(PERMISSIVE=1)
    proteins_list = []

    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for pdb in protein_pdb_list:
            for pdb_file in filenames:
                if pdb in pdb_file:
                    protein = Protein(id=pdb)
                    protein.sequence = str(extract_sequence(folder_path + '/' + pdb_file))
                    protein.name = pypdb.get_all_info(pdb)['polymer']['chain']['macroMolecule']['@name']
                    structure = parser.get_structure('', folder_path + '/' + pdb_file)
                    for model in structure:
                        for chain in model:
                            for residue in chain:
                                if str(residue).split(' ')[2] != 'het=W' and str(residue).split(' ')[2] != 'het=':
                                    protein.ligands.append(residue)
                    proteins_list.append(protein)

    return proteins_list


def protein_clasterization_via_lignad(protein_list):
    ligands =
    for protein in protein_list:
        if len(protein.ligands) != 0:
            for ligand in protein.ligands:
                if find_ligand_with_id()