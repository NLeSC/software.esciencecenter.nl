---
codeRepository: https://github.com/nlesc-sherlock/Rig
competence:
- Big Data Analytics
contactPerson: http://software.esciencecenter.nl/person/j.vanderzwaan
contributor:
- http://software.esciencecenter.nl/person/j.vanderzwaan
- http://software.esciencecenter.nl/person/w.vanhage
- http://software.esciencecenter.nl/person/o.rubi
- http://software.esciencecenter.nl/person/l.buitinck
discipline:
- eScience Methodology
expertise:
- Text Mining
- Information Visualization
- Databases
- Distributed Computing
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
license:
- apache-2.0
logo: /images/software/rig.png
name: Rig
owner:
- http://software.esciencecenter.nl/organization/nlesc
programmingLanguage:
- Python
- JavaScript
startDate: 2016-02-16
status: active
supportLevel: specialized
tagLine: Big data cleaning toolkit
technologyTag:
- Spark
usedIn:
- http://software.esciencecenter.nl/project/sherlock
user:
- http://software.esciencecenter.nl/organization/nlesc
---
Every data analysis project starts with exploring and cleaning data. For tabular data, there are some tools available that facilitate data pre-processing, such as OpenRefine and Trifacta Wrangler. However, these tools one big disadvantage; they don't scale to really big data sets. Also, Trifacta Wrangler is not open source. For full text data, no tools for data cleanup exist.

The goal of the data cleaning toolkit subproject is to create a data cleaning toolkit that is open source, supports both tabular data and full text pre-processing, and scales to big data sets. The frontend is a web interface that supports loading the data and creating workflows. Based on user input, it generates scripts that are send to the backend for execution. The backend relies on spark to ensure scalability.

Because building a complete toolkit is is rather ambitious, we focus on the use case of vocabulary cleanup for full text data. When working with full text data, pre-processing often consists of tokenizing texts (i.e., splitting them into words), lematizing or stemming the tokens, and performing some kind of filtering to remove typo's and other unwanted tokens. The data cleaning toolkit should support customizing these tasks, and provide visualizations that facilitate vocabulary cleanup.
