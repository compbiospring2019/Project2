# Utils for Project 2


# Read a biological sequence or RSA sequence from a file:
def read_sequence(file_path):
    sequence = ''
    with open(file_path, 'r') as f:
        title = f.readline()
        for line in f:
            sequence += line.strip()

    return sequence.upper()
