---
contactPerson: /person/o.rubi
engineer:
- /person/o.rubi
- /person/r.goncalves
- /person/m.vanmeersbergen
- /person/s.verhoeven
endorsedBy:
- /organization/nlesc
involvedOrganization:
- /organization/tu-delft
- /organization/cwi
- /organization/fugro
- /organization/oracle
- /organization/rijkswaterstaat
- /organization/potree
logo: /images/project/massive-point-clouds-for-esciences.jpg
name: Massive Point Clouds for eSciences
publication:
- http://dx.doi.org/10.14778/2824032.2824110
- http://dx.doi.org/10.1016/j.cag.2015.01.007
tagLine: Massive Point-Clouds for eSciences
uses:
- /software/monetdb
- /software/datavaults
- /software/pdal
- /software/potreeconverter
- /software/massivepotreeconverter
- /software/ahn2webviewer
- /software/potree
- /software/liblas
---
We are witnessing an increased significance of point clouds for societal and scientific applications, such as in smart cities, 3D urban modeling, flood modeling, dike monitoring, forest mapping, and digital object preservation in history and art. Modern Big Data acquisition technologies, such as laser scanning from airborne, mobile, or static platforms, dense image matching from photos, or multi-beam echo-sounding, have the potential to generate point clouds with billions (or even trillions) of elevation/depth points. One example is the height map of the Netherlands (the  AHN2 dataset), which consists of no less than 640.000.000.000 height values.

The main problem with these point clouds is that they are simply too big (several terabytes) to be handled efficiently by common ICT infrastructures. At this moment researchers are unable to use this point cloud Big Data to its full potential because of a lack of tools for data management, dissemination, processing, and visualization.

The goal is a scalable (more data and users without architectural change) and generic solution: keep all current standard object-relational database management system (DBMS) and integrate with existing spatial vector and raster data functionality. Core support for point cloud data types in the DBMS is needed, besides the existing vector and raster data types. Furthermore, a new and specific web-services protocol for point cloud data is investigated, supporting progressive transfer based on multi-resolution. Based on user requirements analysis a point cloud benchmark is specified. Oracle, PostgreSQL, MonetDB and file based solutions are analyzed and compared. After identifying weaknesses in existing DBMSs, R&D activities will be conducted in order to realize improved solutions, in close cooperation with the various DBMS developers. The non-academic partners in this project (Rijkswaterstaat, Fugro and Oracle) will deliver their services and expertise and provide access to data and software (development).
