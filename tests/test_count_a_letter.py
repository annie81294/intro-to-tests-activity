# Co-contributer: Valerie, Porselvi, Annie

from main import count_a_letter
import pytest

def test_demo_one():
    sentence = "We are a great team!"
    letter = "a"
    count = count_a_letter(sentence, letter)

    assert count == 4

def test_demo_two():
    sentence = "We are a great team!"
    letter = "x"
    count = count_a_letter(sentence, letter)

    assert count == 0

def test_demo_three():
    sentence = "We are a great team!"
    letter = "10"
    count = count_a_letter(sentence, letter)

    assert count is None

def test_demo_four():
    sentence = "a"
    letter = "We are family!"
    count = count_a_letter(sentence, letter)

    assert count is None

def test_demo_five():
    sentence = "We are a big family!"
    letter = "**"
    count = count_a_letter(sentence, letter)

    assert count is None

def test_demo_five():
    sentence = "WE ARE A BIG FAMILY!"
    letter = "a"
    count = count_a_letter(sentence, letter)

    assert count == 0

# Delete the demo tests and add your tests here 