---
name: DataVaults
endorsedBy:
- /organization/nlesc
tagLine: Technology of Attachment to a DBMS of large file repositories.
codeRepository: https://github.com/MonetDB/data-vaults
website: https://github.com/MonetDB/data-vaults
website: https://www.monetdb.org/Documentation/Extensions/DataVaults
nlescWebsite: 
documentationUrl: https://www.monetdb.org/Documentation/Extensions/DataVaults
downloadUrl: https://www.monetdb.org/Downloads
doi: 
logo: 
programmingLanguage:
- C
license:
- mpl-2.0
competence:
- Optimized Data Handling
discipline:
- eScience Methodology
expertise:
- Databases
supportLevel: specialized
contactPerson: /person/r.goncalves
contributingOrganization:
- /organization/nlesc
contributor:
- /person/r.goncalves
user:
- /person/r.goncalves
involvedOrganization:
- /organization/cwi
- /organization/monetdb
- /organization/jhu
usedIn:
- /project/big-data-analytics-in-the-geo-spatial-domain
- /project/3d-geospatial-data-exploration-for-modern-risk-management-systems
- /project/massive-point-clouds-for-esciences
startDate: 2014-03-1
status: active
dependency:
dependencyOf:
- /software/monetdb
technologyTag:
- Scientific Databases
- In-situ data access
---
A data vault provides a symbiosis between a DBMS and existing file-based repositories.
It keeps data in its original format while scalable processing functionality is offered
through the DBMS. The concept was designed by the CWI Database group, currently the
Netherlands eScience center works closely with CWI Database group to improve it and
extend it.

# Why DataVaults?

DataVaults provides transparent access to all data kept in the file repository
through a tabular or array-based interface abstraction. The in-situ data access
is possible due to the large amounts of metadata (data of data) existent on file
formats such as NetCDF, LAS/LAZ, MSEEDS, HDF5, etc. Such metadata is used for
effective data skipping, but also to collect data insights, e.g. summaries and
samples, without having to process the entire data set.

Such an approach gives the user the opportunity to continue performing data
curation activities since the main data archive is the file-based repository,
i.e., the raw data is kept outside of the DBMS.
