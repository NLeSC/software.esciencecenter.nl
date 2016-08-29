---
codeRepository: https://github.com/NLeSC/python-pcl
competence:
- Big Data Analytics
contactPerson: http://software.esciencecenter.nl/person/j.attema
contributor:
- http://software.esciencecenter.nl/person/j.attema
- http://software.esciencecenter.nl/person/l.buitinck
- http://software.esciencecenter.nl/person/j.borgdorff
- http://software.esciencecenter.nl/person/c.martinez
discipline:
- eScience Methodology
expertise:
- Handling Sensor Data
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
license:
- apache-2.0
name: python-pcl
inGroup:
- NLeSC
programmingLanguage:
- Python
startDate: 2014-10-01
status: active
supportLevel: specialized
tagLine: Python bindings to Point Cloud Library (PCL)
user:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/person/o.rubi
usedIn:
- http://software.esciencecenter.nl/project/viaappia-patty
owner: 
- http://software.esciencecenter.nl/organization/nlesc
dependencyOf:
- http://software.esciencecenter.nl/software/pattyanalytics
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

