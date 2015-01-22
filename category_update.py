import os
import optparse
import xml.etree.ElementTree as ElemTree
from zipfile import ZipFile


def normalize(string):
    """Strip out non-ASCII characters from string
    :param string: the string to normalize
    :return: returns the string without non-ASCII characters
    """
    return "".join(filter(lambda x: ord(x) < 128, string))


def get_features(categoryfile):
    """Get a list of features in a category.xml file
    :param categoryfile: The path to the category.xml file
    :return: returns a vector of feature names
    """
    tree = ElemTree.parse(categoryfile)
    root = tree.getroot()
    features = []
    for feature in root.iter('feature'):
        features.append(feature.attrib['id'].lower())
    return features


def get_versions(features, path):
    """Creates a feature - version mapping based on the
    feature folder names
    :param features: The list of features in the feature.xml file
    :param path: Path to the folder containing the feature folders
    :return: returns an array of tuples containing the feature-version mapping
    """
    folders = os.walk(path).next()[1]
    files = os.walk(path).next()[2]
    versionmap = []
    contents = []
    for folder in folders:
        for feature in features:
            if feature in folder.lower():
                tree = ElemTree.parse(path + '/' + folder + '/feature.xml')
                root = tree.getroot()
                for feat in root.iter('feature'):
                    version = feat.attrib['version']
                    versionmap.append((feature, version))
    for element in files:
        name = str(element).rsplit('.', 1)[0]
        contents.append(name.lower())

    for name in contents:
        for feature in features:
            if feature in name:
                archive = ZipFile(path + '/' + name + '.jar')
                xml = archive.read('feature.xml')
                root = ElemTree.fromstring(xml)
                for feat in root.iter('feature'):
                    version = feat.attrib['version']
                    versionmap.append((feature, version))
    return versionmap


def update_versions(versionmap, categoryfile):
    """Update the category.xml file with correct feature versions
    and feature URLs
    :param versionmap: An array of tuples containing the feature-version mapping
    :param categoryfile: The path to the category.xml file
    """
    tree = ElemTree.parse(categoryfile)
    root = tree.getroot()
    for item in versionmap:
        for feature in root.iter('feature'):
            if feature.attrib['id'].lower() == item[0]:
                feature.set('version', item[1])
                feature.set('url', 'features/' + item[0] + '_' + item[1] + '.jar')
    tree.write(categoryfile)


def category_update():
    """Update the feature URLs and versions in a category file
    """
    parser = optparse.OptionParser()

    parser.add_option('-p', '--path',
                      dest='path',
                      action='store',
                      help='Path to folder containing features')

    parser.add_option('-c', '--cat',
                      dest='categoryFile',
                      action='store',
                      help='Path to the category.xml file')

    (opts, args) = parser.parse_args()
    path = normalize(opts.path)
    categoryfile = normalize(opts.categoryFile)

    features = get_features(categoryfile)
    versionmap = get_versions(features, path)
    update_versions(versionmap, categoryfile)


if __name__ == '__main__':
    category_update()