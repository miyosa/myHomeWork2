import os
import sys
import  allure

import pytest
import yaml

sys.path.append('..')
print(sys.path)

def getData(name, type):
    with open('data.yml') as f:
        allDatas = yaml.safe_load(f)
    datas = allDatas[name][type]['datas']
    ids = allDatas[name][type]['ids']
    print(datas)
    print(ids)
    return (datas, ids)


class TestCalc:

    def test_add(self, get_add_int_data_with_fixture, get_instance):
        a = get_add_int_data_with_fixture
        assert a[2] == get_instance.add(a[0], a[1])

    def test_add_float(self, get_add_folat_data_with_fixture, get_instance):
        a = get_add_folat_data_with_fixture
        assert a[2] == round(get_instance.add(a[0], a[1]), 10)

    def test_div(self, get_div_int_data_with_fixture, get_instance):
        a = get_div_int_data_with_fixture
        assert a[2] == get_instance.div(a[0], a[1])

    def test_div_zero(self, get_div_zero_data_with_fixture, get_instance):
        a = get_div_zero_data_with_fixture
        with pytest.raises(ZeroDivisionError):
            assert a[2] == get_instance.div(a[0], a[1])

    def test_div_float(self, get_div_float_data_with_fixture, get_instance):
        a = get_div_float_data_with_fixture
        assert a[2] == round(get_instance.div(a[0], a[1]), 10)
