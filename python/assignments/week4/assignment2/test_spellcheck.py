import pytest
import spellcheck
# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    # Tests whether a string has fewer than 10 words and fewer than 50 chars.
    assert spellcheck.word_count(input_value) < 10

    assert spellcheck.char_count(input_value) < 50


def test_struc(input_value):
    # Tests whether a string begins with a capital letter and ends with a period.
    assert spellcheck.first_char(input_value).isalpha()

    assert spellcheck.last_char(input_value).endswith('.')

# Run these tests with `python3 -m pytest test_spellcheck.py`