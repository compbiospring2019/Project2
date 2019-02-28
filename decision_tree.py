from amino_acids import get_amino_acid, options
from node import Node
import math


class DecisionTree(object):
    root = None
    feature_matrix = []
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
            self.feature_matrix.append(acid)

    def build_tree(self, current_node=None):
        # Recursive 'build the tree' funct starting with root node
        if current_node is None:
            self.root.attributes_left = [key for key in options.keys() if key not in ['name', 'rsa-label']]
            self.root.molecules = self.feature_matrix
            current_node = self.root

        # Choose best attribute
        best_attribute = self.compute_best_attribute(current_node)
        if best_attribute is None:
            # Data is perfectly classified
            print('Perfectly classified')
            return

        # Create children nodes based on that attribute
        children = current_node.make_children(best_attribute)

        print('current_node.attribute: {}'.format(current_node.attribute))

        # Recursive calls to those children nodes
        for child in children:
            self.build_tree(child)

    def compute_best_attribute(self, current_node):
        # Based on current node, select the best attribute from the leftover attributes
        total_outcomes = [mol['rsa-label'] for mol in current_node.molecules]
        total_entropy = self.compute_entropy(total_outcomes)

        print('Current node attrs left: {}'.format(current_node.attributes_left))

        if total_entropy == 0:
            # Data is perfectly classified
            return None

        attribute_gain = {}
        max_gain_attr = None
        for attr in current_node.attributes_left:
            attribute_gain[attr] = total_entropy
            for attr_val in range(options[attr]):
                # Calculate the portion of the weighted average
                # So, (Probability of attr=attr_val) * (Entropy(attr=attr_val))
                relevant_molecules = [mol for mol in current_node.molecules if mol[attr] == attr_val]
                probability = float(len(relevant_molecules)) / len(current_node.molecules)
                relevant_rsas = [mol['rsa-label'] for mol in relevant_molecules]
                entropy = self.compute_entropy(relevant_rsas)
                attribute_gain[attr] -= probability * entropy
            if not max_gain_attr:
                max_gain_attr = attr
            elif attribute_gain[max_gain_attr] < attribute_gain[attr]:
                max_gain_attr = attr

        return max_gain_attr

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
