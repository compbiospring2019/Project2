from amino_acids import amino_acids, get_amino_acid


def count_attribute(attr):
    count = 0
    for key in amino_acids.keys():
        if amino_acids[key][attr]:
            count += 1
    return count


def test_amino_acids_number():
    assert 20 == len(amino_acids)


def test_num_of_attributes():
    assert count_attribute('hydrophobic') == 12
    assert count_attribute('polar') == 10
    assert count_attribute('charged') == 5
    assert count_attribute('positive') == 3
    assert count_attribute('negative') == 2
    assert count_attribute('small') == 9
    assert count_attribute('tiny') == 3
    assert count_attribute('aliphatic') == 3
    assert count_attribute('aromatic') == 4
    assert count_attribute('proline') == 1


def test_get_amino_acid():
    aa_dict_1 = get_amino_acid('A')
    aa_dict_2 = get_amino_acid('A')
    aa_dict_1['polar'] = None

    assert aa_dict_2['polar'] is not None
