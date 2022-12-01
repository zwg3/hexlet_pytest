from hexlet_pytest import example

def test_reverse():
    assert example.reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert example.reverse('') == ''
