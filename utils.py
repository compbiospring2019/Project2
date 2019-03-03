# Utils for Project 2
import os
import json

# Get the parent directory of this code
this_script = os.path.abspath(__file__)
parent_directory = os.path.dirname(this_script)


# Read a biological sequence or RSA sequence from a file:
def read_sequence(file_path, dir=None):
    if file_path is None:
        return None
    sequence = ''
    if dir:
        file_path = os.path.join(dir, file_path)
    with open(file_path, 'r') as f:
        # Ignore the title line
        title = f.readline()
        for line in f:
            sequence += line.strip()

    return sequence.upper()


def read_directory_contents(path, file_extension):
    if not os.path.isdir(path):
        # This is not a valid directory!
        raise Exception('Not a valid directory!')

    # Return a list of files with the file extension
    ls_dir = os.listdir(path)
    return [file_name for file_name in ls_dir if file_name.endswith(file_extension)]


def write_json(file_name, json_object, dir=parent_directory):
    # Write JSON object to a file
    if dir:
        file_name = os.path.join(dir, file_name)
    with open(file_name, 'w') as outfile:
        json.dump(json_object, outfile)


def read_json():
    # Reads in the JSON object from model.json
    json_file = os.path.join(parent_directory, 'model.json')
    with open(json_file, 'r') as file:
        contents = json.load(file)

    return contents


def print_alignment(fasta_seq, predicted_seq, sa_seq=None):
    if sa_seq is None:
        # Now print things 80 chars wide
        full_lines = int(len(fasta_seq) / 80)
        for i in range(full_lines):
            print(fasta_seq[i * 80:(i + 1) * 80])
            print(predicted_seq[i * 80:(i + 1) * 80])
            print('')

        print(fasta_seq[full_lines * 80:])
        print(predicted_seq[full_lines * 80:])
    else:
        alignment = ''
        for i in range(len(fasta_seq)):
            char_1 = predicted_seq[i]
            char_2 = sa_seq[i]
            if char_1 == char_2:
                alignment += '|'
            else:
                alignment += ' '

        # Now print things 80 chars wide
        print('Key:\n\tFASTA sequence\n\tExpected sequence (from .sa file)')
        print('\t<alignment> (| for same)\n\tPredicted sequence (calculated)\n')
        full_lines = int(len(fasta_seq)/80)
        for i in range(full_lines):
            print(fasta_seq[i * 80:(i + 1) * 80])
            print(sa_seq[i * 80:(i + 1) * 80])
            print(alignment[i * 80:(i + 1) * 80])
            print(predicted_seq[i * 80:(i + 1) * 80])
            print('')

        print(fasta_seq[full_lines * 80:])
        print(sa_seq[full_lines * 80:])
        print(alignment[full_lines * 80:])
        print(predicted_seq[full_lines * 80:])
