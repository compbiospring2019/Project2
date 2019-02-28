class Node(object):
    parent = None           # Pointer to parent node
    children = {}           # Pointers to children nodes (key=attribute, value=child node)
    attributes_left = []    # List of attribute (strings) left
    molecules = []          # List of amino acids (dicts) that fit into this subtree
    attribute = ''          # The attribute choice that this node represents

    def get_outcomes(self, attribute, attr_value):
        if attribute not in self.attributes_left:
            raise Exception('Attribute {} not in {}'.format(attribute, self.attributes_left))

        # Go through molecules and get the rsa-label for that
        # value of the attribute
        outcomes = []
        for molecule in self.molecules:
            if molecule[attribute] == attr_value:
                outcomes.append(molecule['rsa-label'])
        return outcomes
