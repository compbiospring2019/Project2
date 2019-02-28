import utils
import sys

err_msg = '''
Please enter two file names (absolute paths)
of sequences for Decision Tree training data
with double quotes around them (if they have spaces)'''


def parse_args():
    if len(sys.argv) < 3:
        print(err_msg)
        sys.exit()

    try:
        sequence_1 = utils.read_sequence(sys.argv[1])
        sequence_2 = utils.read_sequence(sys.argv[2])
    except:
        # File parsing has failed. Oops.
        print(err_msg)
        sys.exit()

    # Return fasta, sa
    if sys.argv[1].endswith('.sa'):
        return sequence_2, sequence_1
    return sequence_1, sequence_2


def main():
    # Read in the sequences:
    fasta, sa = parse_args()

    print(fasta)
    print(sa)


if __name__ == '__main__':
    main()
