[![Build Status](https://travis-ci.org/fuzzmz/category-update.svg?branch=master)](https://travis-ci.org/fuzzmz/category-update)

The script updates a category.xml file with the correct versions of the features listed in said category.

The required arguments for the script are:

1. `-p /path/to/folder/containing/features`
2. `-c /path/to/category.xml`

The flow of the script is as follows:

1. parse `category.xml` and gather list of features to be updated with correct version
2. create feature-version mapping by mathing the feature name with the version listed in the feature.xml file (for both unpacked features and jars)
3. update `category.xml` with the new feature versions

The `category.xml` file is edited in place, so no new files are created by the script.

In case a feature isn't found, the category file isn't updated for that particular feature.

The script can be run multiple times pointing to different feature folders in case the features listed in the category file aren't grouped in the same folder.
