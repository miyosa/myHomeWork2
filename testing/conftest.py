import pytest
import yaml

import Calc
from test_Calc import getData


@pytest.fixture()
def get_instance():
    print('开始计算')
    calc: Calc = Calc.Calc()
    yield calc
    print('计算结束')


@pytest.fixture(params=getData('add', 'int')[0], ids=getData('add', 'int')[1])
def get_add_int_data_with_fixture(request):
    return request.param


@pytest.fixture(params=getData('add', 'float')[0], ids=getData('add', 'float')[1])
def get_add_folat_data_with_fixture(request):
    return request.param


@pytest.fixture(params=getData('div', 'int')[0], ids=getData('div', 'int')[1])
def get_div_int_data_with_fixture(request):
    return request.param


@pytest.fixture(params=getData('div', 'float')[0], ids=getData('div', 'float')[1])
def get_div_float_data_with_fixture(request):
    return request.param


@pytest.fixture(params=getData('div', 'zero')[0], ids=getData('div', 'zero')[1])
def get_div_zero_data_with_fixture(request):
    return request.param
