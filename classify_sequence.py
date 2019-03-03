import sys
import utils
from train_and_evaluate import err_msg
from decision_tree import DecisionTree


def parse_args():
    if len(sys.argv) < 2:
        print(err_msg)
        sys.exit()

    if len(sys.argv) == 2:
        return sys.argv[1], None
    return sys.argv[1], sys.argv[2]


def main():
    # Get file name and read the sequence
    test_file, sa_file = parse_args()
    test_sequence = utils.read_sequence(test_file)
    sa_sequence = utils.read_sequence(sa_file)

    # Read in the model
    json_model = utils.read_json()

    # Classify the test sequence
    predicted_rsa = DecisionTree.classify_sequence(test_sequence, json_model)

    utils.print_alignment(test_sequence, predicted_rsa, sa_sequence)


if __name__ == '__main__':
    main()
