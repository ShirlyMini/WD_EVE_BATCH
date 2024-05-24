import pytest

class Test_Tsuite3:
    @pytest.mark.regression
    @pytest.mark.skip
    def test_tc1(self, setup1,setup_class, setup_module):
        print("\nthis is tc1 from Test_Tsuite3")

    @pytest.mark.skipif(5>3, reason="condition is true so skipping this test case")
    @pytest.mark.functionality
    def test_tc2(self, setup1):
        print("\nthis is tc2 from Test_Tsuite3")

    @pytest.mark.regression
    @pytest.mark.xfail
    def test_tc3(self, setup1):
        print("\nthis is tc3 from Test_Tsuite3")