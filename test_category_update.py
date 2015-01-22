# coding=utf-8
import pytest
import os
from category_update import normalize, get_features, get_versions


@pytest.fixture
def set_fixture():
    features = get_features(os.path.realpath(__file__).rsplit('\\', 1)[0] + '/tests/category.xml')
    path = os.path.realpath(__file__).rsplit('\\', 1)[0] + '/tests/features/'
    return features, path


def test_normalize():
    assert normalize('test') == 'test'


def test_normalize_nonascii():
    assert normalize(u"testá") == 'test'


def test_get_features():
    assert get_features(os.path.realpath(__file__).rsplit('\\', 1)[0] + '/tests/category.xml') == [
        'com.fuzzmz_testfeature4.ext', 'com.fuzzmz.testfeature2', 'com.fuzzmz.testfeature3_ext', 'com.fuzzmz_testfeature1']


def test_get_versions(set_fixture):
    features, path = set_fixture
    assert get_versions(features, path) == [('com.fuzzmz_testfeature4.ext', '4.8.0.207352_201406-060126'),
                                            ('com.fuzzmz.testfeature2', '3.8.0.207352-201406060126'),
                                            ('com.fuzzmz.testfeature3_ext', '4.8.0.207352_201406060126'),
                                            ('com.fuzzmz_testfeature1', '2.8.0.207352-201406060126')]