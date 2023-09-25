from programm import plusmal, unterschreiben, kubieren

def test_plusmal():
    assert plusmal(2, 3) == 10
    assert plusmal(0, 0) == 0
    assert plusmal(-1, 1) == 0

def test_unterschreiben():
    assert unterschreiben("test") == "test_unterschrieben"
    assert unterschreiben("hello") == "hello_unterschrieben"
    assert unterschreiben("") == "_unterschrieben"

def test_kubieren():
    assert kubieren(2) == 8
    assert kubieren(3) == 27
    assert kubieren(0) == 0
