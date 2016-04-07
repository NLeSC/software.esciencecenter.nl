---
name: MAGMa
tagLine: MAGMa is an online application for the automatic chemical annotation of accurate multistage MSn spectral data.
codeRepository: https://github.com/NLeSC/MAGMa
website: http://www.emetabolomics.org/magma
codeRepository: https://github.com/NLeSC/Osmium
programmingLanguage:
- Python
license:
- apache-2.0
competence:
- Efficient Computing
discipline:
- Life Sciences & eHealth
expertise:
- High Performance Computing
- Scientific Visualization
supportLevel: specialized
contactPerson: http://software.esciencecenter.nl/person/l.ridder
owner:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/wur
contributor:
- http://software.esciencecenter.nl/person/l.ridder
- http://software.esciencecenter.nl/person/s.verhoeven
user:
- http://software.esciencecenter.nl/person/l.ridder
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/wur
usedIn:
- http://software.esciencecenter.nl/project/emetabolomics
startDate: 2011-05-10
status: active
dependency:
- http://software.esciencecenter.nl/software/osmium
technologyTag:
- Distributed
- Webservice
---
MAGMa is an online application for the automatic chemical annotation of accurate multistage MSn spectral data.

- MSn data can be uploaded as a hierarchical tree of fragment peaks, either based on m/z values or elemental formulas, or as an mzXML file of the raw data.
- Candidate molecules are automatically retrieved from PubChem, from a subset of PubChem compounds present in Kegg, or from the Human Metabolome Database.
- Candidate molecules can be predicted based on in silico reaction rules describing microbiotic and human biotransformations
- For each candidate molecule, substructures are generated and matched with the observed fragment peaks.
- The web browser enables efficient mining of the automatically annotated data.
- Open Source, source code available at [https://github.com/NLeSC/MAGMa](https://github.com/NLeSC/MAGMa)

![screenshot](https://github.com/NLeSC/MAGMa/raw/master/web/magmaweb/static/img/metabolites.png "Screenshot of web application").
