import utils
import sys
from decision_tree import DecisionTree

err_msg = '''
Please enter two directory names (absolute paths)
containing sequences for Decision Tree training data
(with double quotes around them if they have spaces).
The directory with FASTA files should come first, 
followed by the path to the .sa files.'''


def parse_args():
    if len(sys.argv) < 3:
        print(err_msg)
        sys.exit()

    try:
        # Get the lists of fasta and sa file names
        fasta = utils.read_directory_contents(sys.argv[1], '.fasta')
        sa = utils.read_directory_contents(sys.argv[2], '.sa')
    except:
        # Given paths are not valid directories
        print(err_msg)
        sys.exit()

    return fasta, sa


def main():
    # Read in the file names
    fasta, sa = parse_args()

    # Create the decision tree and train the model
    decision_tree = DecisionTree(fasta, sa, sys.argv[1], sys.argv[2])
    decision_tree.build_feature_matrix()
    decision_tree.build_tree()
    decision_tree.evaluate_model()


if __name__ == '__main__':
    main()
