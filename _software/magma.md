---
codeRepository: https://github.com/NLeSC/Osmium
competence:
- Big Data Analytics
- Efficient Computing
contactPerson: /person/l.ridder
contributingOrganization:
- /organization/nlesc
contributor:
- /person/l.ridder
- /person/s.verhoeven
- /person/m.sanders
dependency:
- /software/osmium
- /software/rdkit
discipline:
- Life Sciences & eHealth
endorsedBy:
- /organization/nlesc
expertise:
- High Performance Computing
- Scientific Visualization
involvedOrganization:
- /organization/nlesc
- /organization/wur
license:
- apache-2.0
name: MAGMa
owner:
- /organization/nlesc
- /organization/wur
programmingLanguage:
- Python
- JavaScript
startDate: 2011-05-10
status: active
supportLevel: specialized
tagLine: MAGMa is an online application for the automatic chemical annotation of accurate
  multistage MSn spectral data.
technologyTag:
- Distributed
- Webservice
usedIn:
- /project/emetabolomics
user:
- /person/l.ridder
- /person/m.sanders
website: http://www.emetabolomics.org/magma
---
MAGMa is an online application for the automatic chemical annotation of accurate multistage MSn spectral data.

- MSn data can be uploaded as a hierarchical tree of fragment peaks, either based on m/z values or elemental formulas, or as an mzXML file of the raw data.
- Candidate molecules are automatically retrieved from PubChem, from a subset of PubChem compounds present in Kegg, or from the Human Metabolome Database.
- Candidate molecules can be predicted based on in silico reaction rules describing microbiotic and human biotransformations
- For each candidate molecule, substructures are generated and matched with the observed fragment peaks.
- The web browser enables efficient mining of the automatically annotated data.
- Open Source, source code available at [https://github.com/NLeSC/MAGMa](https://github.com/NLeSC/MAGMa)

![screenshot](https://github.com/NLeSC/MAGMa/raw/master/web/magmaweb/static/img/metabolites.png "Screenshot of web application").
