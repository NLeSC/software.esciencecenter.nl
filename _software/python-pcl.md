---
codeRepository: https://github.com/NLeSC/python-pcl
competence:
- Big Data Analytics
contactPerson: /person/j.attema
contributingOrganization:
- /organization/nlesc
contributor:
- /person/j.attema
- /person/l.buitinck
- /person/j.borgdorff
- /person/c.martinez
discipline:
- eScience Methodology
expertise:
- Handling Sensor Data
involvedOrganization:
- /organization/nlesc
license:
- apache-2.0
name: python-pcl
endorsedBy:
- /organization/nlesc
programmingLanguage:
- Python
startDate: 2014-10-01
status: active
supportLevel: specialized
tagLine: Python bindings to Point Cloud Library (PCL)
user:
- /organization/nlesc
- /person/o.rubi
usedIn:
- /project/viaappia-patty
owner: 
- /organization/nlesc
dependencyOf:
- /software/pattyanalytics
technologyTag:
- Point clouds
---
This is a small python binding to the pointcloud library. Currently, the following parts of the API are wrapped (all methods operate on PointXYZRGB) point types

- I/O and integration; saving and loading PCD files
- segmentation
- SAC
- smoothing
- filtering

The code tries to follow the Point Cloud API, and also provides helper function for interacting with NumPy.

