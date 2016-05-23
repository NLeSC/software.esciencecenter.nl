---
name: Salient Region Detectors
tagLine: Software package for detecting salient regions in images.
codeRepository: https://github.com/NLeSC/LargeScaleImaging
website:
documentationUrl: https://github.com/NLeSC/SalientDetector-python/blob/master/README.md
logo:
programmingLanguage:
- MATLAB
- Python
license:
- apache-2.0
competence:
- Big Data Analytics
discipline:
- eScience Methodology
expertise:
- Computer Vision
supportLevel: specialized
contactPerson: http://software.esciencecenter.nl/person/e.ranguelova
owner:
- http://software.esciencecenter.nl/organization/nlesc
contributor:
- http://software.esciencecenter.nl/person/e.ranguelova
- http://software.esciencecenter.nl/person/d.vankuppevelt
user:
- http://software.esciencecenter.nl/organization/nlesc
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
usedIn:

startDate: 2015-04-01
status: wip
dependency:
dependencyOf:
technologyTag:
- OpenCV
---
This package provide functionality to detect salient regions in images. Salient regions, or features, are regions in the image that are 'interesting', such as corners, lines and blobs. The detectors in this package specifically find blob-like regions. The detected regions could be used, for example, to match photos of the same object, taken under different conditions. These salient regions are invariant under transformations such as blurring, light change and rotation.

The software is implemented both in MATLAB and Python.
