# coding=utf-8
import pytest
import os
from category_update import normalize, get_features, get_versions


@pytest.fixture
def set_fixture():
    root, script = os.path.split(os.path.realpath(__file__))
    getfeaturesfunc = get_features(root + '/tests/category.xml')
    path = root + '/tests/features/'
    features = ['com.fuzzmz_testfeature1', 'com.fuzzmz.testfeature2', 'com.fuzzmz.testfeature3_ext',
                'com.fuzzmz_testfeature4.ext']
    featuremap = [('com.fuzzmz_testfeature4.ext', '4.8.0.207352_201406-060126'),
                  ('com.fuzzmz.testfeature2', '3.8.0.207352-201406060126'),
                  ('com.fuzzmz.testfeature3_ext', '4.8.0.207352_201406060126'),
                  ('com.fuzzmz_testfeature1', '2.8.0.207352-201406060126')]
    return getfeaturesfunc, path, root, features, featuremap


def test_normalize():
    assert normalize('test') == 'test'


def test_normalize_nonascii():
    assert normalize(u"testá") == 'test'


def test_get_features(set_fixture):
    getfeaturesfunc, path, root, features, featuremap = set_fixture
    assert get_features(root + '/tests/category.xml') == features


def test_get_versions(set_fixture):
    getfeaturesfunc, path, root, features, featuremap = set_fixture
    assert get_versions(getfeaturesfunc, path) == featuremap