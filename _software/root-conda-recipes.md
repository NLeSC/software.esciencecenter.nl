---
name: ROOT-conda-recipes
endorsedBy:
- /organization/nlesc
tagLine: Conda recipes for building CERN ROOT binaries and its dependencies, with Python 3 support. It provides a "pythonic" interface (pandas DataFrames) to the ROOT I/O format.

codeRepository: http://github.com/NLeSC/root-conda-recipes
nlescWebsite: http://www.gitbook.com/book/nlesc/cern-root-conda-recipes/details
website: http://www.gitbook.com/book/nlesc/cern-root-conda-recipes/details
codeRepository: http://github.com/NLeSC/root-conda-recipes
nlescWebsite: http://www.esciencecenter.nl/technology/software/root-conda-recipes
documentationUrl: http://www.gitbook.com/book/nlesc/cern-root-conda-recipes/details
downloadUrl: http://github.com/NLeSC/root-conda-recipes/archive/master.zip
doi: http://dx.doi.org/10.5281/zenodo.47512
programmingLanguage:
- Python
license:
- apache-2.0
competence:
- Efficient Computing
discipline:
- Physics & Beyond
expertise:
- Distributed Computing
supportLevel: specialized
contactPerson: /person/d.remenska
owner: 
- /person/d.remenska
contributingOrganization:
- /organization/nlesc
contributor:
- /person/d.remenska
- /person/s.verhoeven
user:
- /organization/nikhef
involvedOrganization:
- /organization/nikhef
usedIn:
- /project/pandas-root
status: active
dependency:
- ROOT
- root-numpy
- rootpy
dependencyOf:
technologyTag:
- Anaconda
- pandas DataFrame
- Computing model
badges:
- "[![Build Status](https://api.travis-ci.org/NLeSC/root-conda-recipes.svg)](https://travis-ci.org/NLeSC/root-conda-recipes/)"
- "[![DOI](https://zenodo.org/badge/20885/NLeSC/root-conda-recipes.svg)](https://zenodo.org/badge/latestdoi/20885/NLeSC/root-conda-recipes)"
- "[![Join the chat at https://gitter.im/NLeSC/root-conda-recipes](https://badges.gitter.im/NLeSC/root-conda-recipes.svg)](https://gitter.im/NLeSC/root-conda-recipes?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)"
---
This repository contains Conda recipes for building CERN [ROOT](https://root.cern.ch/) binaries and its dependencies. For the needs of the [XENON Dark Matter project](http://www.xenon1t.org/), the goal is to provide a "pythonic" interface to the ROOT I/O format, primarily for loading and saving Pandas dataframes in the ROOT format. For this purpose, there are also recipes for building conda binaries of [root-numpy](https://github.com/rootpy/root_numpy) and [rootpy](https://github.com/rootpy/rootpy), the community-driven initiative to provide a more pythonic interface with ROOT on top of the existing PyROOT bindings.

The most most important thing for making things work out of the box is the ABI (binary) compatibility between different gcc(libstdc++)/glibc library versions, on various linux distributions. Typically ROOT would even complain when the GCC headers are not of the same version as the one used for building it, so *shipping the full GCC and glibc as a run dependency* of ROOT, seemed like the best solution.

Combine this with the fact that ROOT 6 requires GCC>=4.8, while we want things to work on older platforms with no "sudo" required, **we decided to fix our GCC distribution to (a relatively recent one) 4.8.2, built against a rather old glibc version 2.12**, making it as cross platform as possible. 

Working ROOT has been tested on: Ubuntu 11.10, 12.04, 14.04, 15.04, SLC-6.7, SLC-7. Please try it out and let us know if you experience problems. 


