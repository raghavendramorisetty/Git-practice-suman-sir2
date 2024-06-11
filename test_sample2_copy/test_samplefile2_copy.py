import pytest
@pytest.mark.registration
def test_fun():pass

@pytest.mark.login1
class TestA:
    @pytest.mark.login2  
    def test_method1(self):
        a=1
        b=2
        assert a.__eq__(b), "a is not equal to (b)" # Hard assertion

    @pytest.mark.login3
    def test_method2(self): 
        w=2
        x=3
        if w>x: # Soft Assertion
            print("w is greater")
        else:
            print("x is greater")
        print("method2")


    @pytest.mark.loginnn
    def test_method3(self): pass

    @pytest.mark.loginnn
    def test_method4(self): pass

    def test_method6(self):
        assert 1==2, "a is not equal to 2" # Hard assertion

    @pytest.mark.skip
    def test_method5(self): pass

    @pytest.mark.xfail
    def test_method7(self):
        assert 1==2

    

    