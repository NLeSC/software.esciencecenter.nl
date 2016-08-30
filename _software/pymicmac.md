---
codeRepository: https://github.com/ImproPhoto/pymicmac
competence:
- Optimized Data Handling
contactPerson: http://software.esciencecenter.nl/person/o.rubi
contributor:
- http://software.esciencecenter.nl/person/o.rubi
dependency:
- http://software.esciencecenter.nl/software/pycoeman
- http://software.esciencecenter.nl/software/noodles
dependencyOf:
discipline:
- eScience Methodology
downloadUrl: https://github.com/ImproPhoto/pymicmac
expertise:
- Distributed Computing
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
license:
- apache-2.0
name: pymicmac
owner:
- http://software.esciencecenter.nl/organization/nlesc
programmingLanguage:
- Python
startDate: 2016-05-03
status: active
supportLevel: specialized
tagLine: pymicmac provides a python interface for MicMac workflows execution and distributed computing tools for MicMac.
technologyTag:
- Distributed
- Workflow
- Library
- Point clouds
usedIn:
- http://software.esciencecenter.nl/project/improving-photogrammetry
user:
- http://software.esciencecenter.nl/person/o.rubi
---
pymicmac provides a python interface for MicMac workflows execution and distributed computing tools for MicMac. pymicmac uses pycoeman (Python Commands Execution Manager) (https://github.com/NLeSC/pycoeman) which also provides CPU/MEM/disk monitoring.

MicMac is a photogrammetric suite which contains many different tools to execute photogrammetric workflows. In short, a photogrammetric workflow contains at least:

(1) tie-point detection: extraction of key features in images and cross-match between different images to detect tie-points (points in the images that represent the same physical locations).

(2) Estimation of camera positions and orientations and of calibration parameters: mainly the bundle adjustment but may include some preparation and/or refinement steps.

(3) Dense-matching point cloud generation. 3D projection of image pixels to produce the dense point cloud.

pymicmac provides the tool micmac-run-workflow to run photogrammetric workflows with a sequence of MicMac commands. The tool uses the sequential commands execution tool of pycoeman which is configured with a XML configuration file that defines a chain of MicMac commands to be executed sequentially.