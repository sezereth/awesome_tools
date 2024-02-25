from awesome_tools.tools.string_utils import reverse_string, capitalize_string, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_capitalize_string():
    assert capitalize_string("python") == "Python"

def test_count_vowels():
    assert count_vowels("hello") == 2
