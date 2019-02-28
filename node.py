from amino_acids import options


class Node(object):
    parent = None           # Pointer to parent node
    children = {}           # Pointers to children nodes (key=attribute, value=child node)
    attributes_left = []    # List of attribute (strings) left
    molecules = []          # List of amino acids (dicts) that fit into this subtree
    attribute = ''          # The attribute choice that this node represents

    def __init__(self, parent_node=None):
        self.parent = parent_node

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

    def make_children(self, attribute):
        # Create & return the children nodes of this node based on the current attribute
        if attribute not in self.attributes_left:
            raise Exception('Attribute {} not in {}'.format(attribute, self.attributes_left))

        # Set this node's attribute
        self.attribute = attribute

        # Create the children
        children = []
        # For each value of the attribute, set parent attributes left, and molecules
        # Note: index in array of children is the attribute's value
        for attr_value in range(options[attribute]):
            child = Node(self)
            child.attributes_left = [attr for attr in self.attributes_left if attr != attribute]
            child.molecules = [mol for mol in self.molecules if mol[attribute] == attr_value]
            children.append(child)

        return children
