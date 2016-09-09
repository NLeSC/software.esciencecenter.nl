---
name: PIDIlib
endorsedBy:
- /organization/nlesc
tagLine: A collection of scripts used in the PIDIMEHS project
codeRepository: https://bitbucket.org/egpbos/pidilib
nlescWebsite: 
website: 
documentationUrl:
logo:
programmingLanguage:
- Python
license:
- apache-2.0
competence:
- Big Data Analytics
discipline:
- Humanities & Social Sciences
expertise:
- Text Mining
- Information Retrieval
- Information Visualization
- Data Assimilation
supportLevel: advanced
contactPerson: /person/p.bos
owner:
- /organization/nlesc
contributingOrganization:
- /organization/nlesc
contributor:
- /person/p.bos
- /person/l.buitinck
user:
- /organization/university.of.groningen
involvedOrganization:
- /organization/nlesc
- /organization/university.of.groningen
- /organization/uva
- /organization/surfsara
usedIn:
- /project/pidimehs
startDate: 2014-08-01
status: inactive
dependency:
dependencyOf:
technologyTag:
- Elasticsearch
---
PIDIlib is a collection of scripts used in the PIDIMEHS project. It is mainly provided to showcase the possibilities of combining Elasticsearch, Pandas and Matplotlib in Python in the study of history of politics and media. PIDIlib's main contents are:

- Ways of querying the PIDIMEHS KB newspaper Elasticsearch instance
- Using Pandas to analyze the queried aggregations
- Visualization using Matplotlib
- Data used for 'indicators of pillarization' in the PIDIMEHS project
- Jupyter notebooks that were used to produce the results presented in the PIDIMEHS technical paper.

The KB newspaper data can be freely obtained from [Delpher](www.delpher.nl). It is not allowed to redistribute this data, so we cannot give access to our own instance. To use PIDIlib, one will have to set up their own Elasticsearch instance. Alternatively, one may contact the KB or SURFsara to request access to the SURFsara instance (which we used as well).
