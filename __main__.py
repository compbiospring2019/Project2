import utils
import sys
from decision_tree import DecisionTree

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

    decision_tree = DecisionTree(fasta, sa)
    decision_tree.build_feature_matrix()
    decision_tree.build_tree()

    decision_tree.walk_tree({
        'hydrophobic': 1,
        'polar': 0,
        'charged': 0,
        'positive': 0,
        'negative': 0,
        'small': 1,
        'tiny': 1,
        'aliphatic': 0,
        'aromatic': 0,
        'proline': 0
    })  # A, returns B

    decision_tree.walk_tree({
        'hydrophobic': 0,
        'polar': 1,
        'charged': 1,
        'positive': 1,
        'negative': 0,
        'small': 0,
        'tiny': 0,
        'aliphatic': 0,
        'aromatic': 0,
        'proline': 0
    })  # K, returns B

    decision_tree.walk_tree({
        'hydrophobic': 1,
        'polar': 0,
        'charged': 0,
        'positive': 0,
        'negative': 0,
        'small': 0,
        'tiny': 0,
        'aliphatic': 0,
        'aromatic': 1,
        'proline': 0
    })  # F, returns E


if __name__ == '__main__':
    main()
