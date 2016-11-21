---
codeRepository: https://github.com/NLeSC/ahn-pointcloud-viewer
website: http://ahn2.pointclouds.nl/
competence:
- Big Data Analytics
contactPerson: /person/m.vanmeersbergen
contributingOrganization:
- /organization/nlesc
contributor:
- /person/m.vanmeersbergen
- /person/o.rubi
- /person/s.verhoeven
discipline:
- eScience Methodology
expertise:
- Scientific Visualization
involvedOrganization:
- /organization/nlesc
license:
- apache-2.0
dependency:
- /software/potree
- /software/potreeconverter
- /software/massivepotreeconverter
name: AHN2 pointcloud viewer
endorsedBy:
- /organization/nlesc
programmingLanguage:
- JavaScript
startDate: 2014-04-01
status: active
supportLevel: specialized
tagLine: WebGL point cloud visualization of AHN2
user:
- /organization/nlesc
- /person/o.rubi
usedIn:
- /project/massive-point-clouds-for-esciences
owner: 
- /organization/nlesc
technologyTag:
- Point clouds
- WebGL
- Website
- 3D
---
WebGL point cloud visualization of the Actuele Hoogtekaart Nederland 2. 
This renderer is based on http://potree.org

In order to visualize such a massive data set, the AHN2 has to be reorganized in a multi-resolution octree. This processing can be done with the Massive-PotreeConverter (</software/massivepotreeconverter>) which is a extension of the PotreeConverter (</software/potreeconverter>) to distribute the processing into multiple machines/cores.
