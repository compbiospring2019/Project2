from amino_acids import get_amino_acid
from node import Node
import math


class DecisionTree(object):
    root = None
    feature_matrix = None
    fasta = None
    sa = None

    def __init__(self, fasta, sa):
        # TODO: Training data vs. test data
        self.fasta = fasta
        self.sa = sa
        self.root = Node()

    def build_feature_matrix(self):
        for index in range(len(self.fasta)):
            # Create the AA object
            acid = get_amino_acid(self.fasta[index].upper())

            # Add the RSA label
            acid['rsa-label'] = self.sa[index]

            # Add the acid to the matrix
            self.matrix.append([])

    def build_tree(self, current_node=None):
        # Recursive 'build the tree' funct starting with root node
        if current_node is None:
            current_node = self.root

        # Choose best attribute
        # Create children nodes based on that attribute
        # Recursive calls to those children nodes

        pass

    def compute_best_attribute(self, current_node):
        # Based on current node, select
        pass

    def compute_entropy(self, outcome_list):
        # Outcome list: the list of outcomes (y/n) for a given data set
        # or attribute

        # Calc number of each outcome
        outcome_count = {}
        for outcome in outcome_list:
            if outcome not in outcome_count:
                outcome_count[outcome] = 0
            outcome_count[outcome] += 1

        # Calculate the entropy (sum of p*log(p))
        sum = 0
        for outcome in outcome_count.keys():
            probability = float(outcome_count[outcome]) / len(outcome_list)
            sum -= probability * math.log(probability, 2)

        return sum

    def evaluate_model(self):
        pass

    def calculate_eval_metrics(self):
        pass


options = {
    'hydrophobic': 2,
    'polar': 2,
    'charged': 2,
    'positive': 2,
    'negative': 2,
    'small': 2,
    'tiny': 2,
    'aliphatic': 2,
    'aromatic': 2,
    'proline': 2,
    'rsa-label': 2
}
