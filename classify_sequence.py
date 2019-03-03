import sys
import utils
from train_and_evaluate import err_msg
from decision_tree import DecisionTree


def parse_args():
    if len(sys.argv) < 2:
        print(err_msg)
        sys.exit()

    return sys.argv[1]


def main():
    # Get file name and read the sequence
    test_file = parse_args()
    test_sequence = utils.read_sequence(test_file)

    # Read in the model
    json_model = utils.read_json()

    # Classify the test sequence
    predicted_rsa = DecisionTree.classify_sequence(test_sequence, json_model)

    print(predicted_rsa)


if __name__ == '__main__':
    main()
