import pytest
@pytest.mark.parametrize('name',['张三','李四'])
def test_encode(name):
    print(name)