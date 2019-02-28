from amino_acids import get_amino_acid


class DecisionTree(object):
    root = None
    feature_matrix = None
    fasta = None
    sa = None

    def __init__(self, fasta, sa):
        self.fasta = fasta
        self.sa = sa

    def build_feature_matrix(self):
        for index in range(len(self.fasta)):
            # Create the AA object
            acid = get_amino_acid(self.fasta[index].upper())

            # Add the RSA label
            acid['rsa-label'] = self.sa[index]

            # Add the acid to the matrix
            self.matrix.append([])
