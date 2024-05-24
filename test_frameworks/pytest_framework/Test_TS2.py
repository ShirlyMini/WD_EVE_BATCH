import pytest


class Test_Tsuite2:
    @pytest.mark.sanity
    def test_tc1(self,setup1, setup_class, setup_module):
        print("\nthis is tc1 from Test_Tsuite2")

    @pytest.mark.sanity
    def test_tc2(self,setup1):
        print("\nthis is tc2 from Test_Tsuite2")

    @pytest.mark.functionality
    @pytest.mark.regression
    @pytest.mark.parametrize("name",["john", "scott", "pooja", "nike"])
    def test_tc3(self,setup1, name):
        print("\nthis is tc3 from Test_Tsuite2")
        print(name)

    @pytest.mark.functionality
    @pytest.mark.regression
    @pytest.mark.parametrize("name,age,qual",[("john", 25, "BE"), ("Pooja", "23", "BCOM"), ("nike", "27", "MS")])
    def test_tc4(self,setup1, name, age, qual):
        print("\nthis is tc3 from Test_Tsuite2")
        print(f"{name} {age} {qual}")