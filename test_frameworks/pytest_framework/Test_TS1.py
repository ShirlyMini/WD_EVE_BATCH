import pytest

@pytest.mark.sanity
def test_tc1():
    print("this is tc1 from TS1")
    #assert False
@pytest.mark.sanity
def test_tc2():
    print("this is tc2 from TS1")
@pytest.mark.functionality
def test_tc3():
    print("this is tc3 from TS1")