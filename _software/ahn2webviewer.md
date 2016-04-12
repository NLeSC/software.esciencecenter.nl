---
codeRepository: https://github.com/NLeSC/ahn-pointcloud-viewer
competence:
- Big Data Analytics
contributor:
- http://software.esciencecenter.nl/person/m.vanmeersbergen
- http://software.esciencecenter.nl/person/o.rubi
- http://software.esciencecenter.nl/person/s.verhoeven
discipline:
- eScience Methodology
expertise:
- Scientific Visualization
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
license:
- apache-2.0
dependency:
- http://software.esciencecenter.nl/software/potree
- http://software.esciencecenter.nl/software/potreeconverter
- http://software.esciencecenter.nl/software/massivepotreeconverter
name: AHN2 pointcloud viewer
programmingLanguage:
- JavaScript
startDate: 2014-04-01
status: active
supportLevel: specialized
tagLine: WebGL point cloud visualization of AHN2
user:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/person/o.rubi
usedIn:
- http://software.esciencecenter.nl/project/massive-point-clouds-for-esciences
owner: 
- http://software.esciencecenter.nl/organization/nlesc
technologyTag:
- Point clouds
- WebGL
---
WebGL point cloud visualization of the Actuele Hoogtekaart Nederland 2. 
This renderer is based on http://potree.org

In order to visualize such a massive data set, the AHN2 has to be reorganized in a multi-resolution octree. This processing can be done with the Massive-PotreeConverter (<http://software.esciencecenter.nl/software/massivepotreeconverter>) which is a extension of the PotreeConverter (<http://software.esciencecenter.nl/software/potreeconverter>) to distribute the processing into multiple machines/cores.