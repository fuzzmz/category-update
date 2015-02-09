# coding=utf-8
import pytest
import os
from category_update import normalize, get_features, get_versions


@pytest.fixture
def set_fixture():
    root, script = os.path.split(os.path.realpath(__file__))
    categoryfile = root + '/tests/category.xml'
    getfeaturesfunc = get_features(categoryfile)
    path = root + '/tests/features/'
    features = ['com.fuzzmz_testfeature1', 'com.fuzzmz.testfeature2', 'com.fuzzmz.testfeature3_ext',
                'com.fuzzmz_testfeature4.ext']
    featuremap = [('com.fuzzmz_testfeature4.ext', '4.8.0.207352_201406-060126', False),
                  ('com.fuzzmz.testfeature2', '3.8.0.207352-201406060126', True),
                  ('com.fuzzmz.testfeature3_ext', '4.8.0.207352_201406060126', True),
                  ('com.fuzzmz_testfeature1', '2.8.0.207352-201406060126', True)]
    return getfeaturesfunc, path, root, features, featuremap, categoryfile


def test_normalize():
    assert normalize('test') == 'test'


def test_normalize_nonascii():
    assert normalize(u"testá") == 'test'


def test_get_features(set_fixture):
    getfeaturesfunc, path, root, features, featuremap, categoryfile = set_fixture
    assert get_features(categoryfile) == features


def test_get_versions(set_fixture):
    getfeaturesfunc, path, root, features, featuremap, categoryfile = set_fixture
    test_mapping = get_versions(getfeaturesfunc, path)
    assert len(test_mapping) == len(featuremap)
    for i in range(len(test_mapping)):
        assert featuremap[i] in test_mapping