---
name: WRFpy
endorsedBy:
- /organization/nlesc
tagLine: Python workflow application to set up/run WRF simulations (optionally including data assimilation).
codeRepository: https://github.com/rvanharen/wrfpy
downloadUrl: https://github.com/rvanharen/wrfpy/releases
programmingLanguage:
- Python
license:
- apache-2.0
competence:
- Big Data Analytics
- Efficient Computing
discipline:
- Environment & Sustainability
- eScience Methodology
expertise:
- 'Data Assimilation'
- 'Distributed Computing'
- 'High Performance Computing'
- 'Databases'
supportLevel: specialized
contactPerson: /person/r.vanharen
owner:
- /person/r.vanharen
contributingOrganization:
- /organization/nlesc
contributor:
- /person/r.vanharen
user:
- /person/r.vanharen
- /organization/wur
involvedOrganization:
- /organization/nlesc
usedIn:
- /project/era-urban
startDate: 2015-10-15
status: wip
dependency:
- /software/pyxenon
- f90nml
- WRF
- WRFDA
- UPP
- WPS
dependencyOf:
technologyTag:
- Simulation
- workflow

---
WRFpy is a python application that provides an easy way to set up, run,
and monitor (long) Weather Research and Forecasting (WRF) simulations. It
provides a simple user-editable JSON configuration file and an integration
with pyxenon to access distributes computing and storage resources.
Optionally, WRFpy allows for data assimilation using WRF data assimilation
system (WRFDA) and postprocessing of wrfinput files using the NCEP Unified
Post Processing System (UPP).
