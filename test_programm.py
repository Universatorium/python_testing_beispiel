from programm import *

def test_plusmal():
    assert plusmal(2,3)*3 == 15

def test_unterschreiben():
    assert unterschreiben("unterschrieben") == "unterschrieben"

def test_url():
    assert url("https://github.com/Universatorium/python_testing_beispiel") == "https://github.com/Universatorium/python_testing_beispiel"

def test_kubieren():
    assert kubieren(4) == 64