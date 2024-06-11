import pytest

@pytest.mark.parametrize("userid,pswd",[("user1","pswd1"),("user2","pswd2"),("user3","pswd3")])
def test_f1(userid,pswd):
    print("user id is:",userid)
    print("password is:",pswd)