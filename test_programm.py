from programm import *

def test_plusmal():
    assert plusmal(3,3) == 12
def test_plusmal():
    assert plusmal(14,-3)*11 == 121

def test_unterschreiben():
    assert unterschreiben("Test") == "Test unterschrieben"

def test_url():
    assert url("https://github.com/Universatorium/python_testing_beispiel") == "https://github.com/Universatorium/python_testing_beispiel GitHub url"

def test_kubieren():
    assert kubieren(4) == 64