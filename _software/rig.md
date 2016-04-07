---
name: Rig
tagLine: Big data cleaning toolkit
codeRepository: https://github.com/nlesc-sherlock/Rig
nlescWebsite:
website:
documentationUrl:
logo: https://raw.githubusercontent.com/nlesc-sherlock/Rig/develop/app/images/noun_95045_cc.png
programmingLanguage:
- Python
- JavaScript
license:
- apache-2.0
competence:
- Big Data Analytics
discipline:
- eScience Methodology
expertise:
- Text Mining
- Information Visualization
- Databases
- Distributed Computing
supportLevel: specialized
contactPerson: http://software.esciencecenter.nl/person/j.vanderzwaan
owner:
- http://software.esciencecenter.nl/organization/nlesc
contributor:
- http://software.esciencecenter.nl/person/j.vanderzwaan
- http://software.esciencecenter.nl/person/w.vanhage
- http://software.esciencecenter.nl/person/o.rubi
- http://software.esciencecenter.nl/person/l.buitinck

user:
- http://software.esciencecenter.nl/organization/nlesc
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc

usedIn:

startDate: 2016-02-16
status: active
dependency:
dependencyOf:
technologyTag:
- Spark
---
Every data analysis project starts with exploring and cleaning data. For tabular data, there are some tools available that facilitate data pre-processing, such as OpenRefine and Trifacta Wrangler. However, these tools one big disadvantage; they don't scale to really big data sets. Also, Trifacta Wrangler is not open source. For full text data, no tools for data cleanup exist.

The goal of the data cleaning toolkit subproject is to create a data cleaning toolkit that is open source, supports both tabular data and full text pre-processing, and scales to big data sets. The frontend is a web interface that supports loading the data and creating workflows. Based on user input, it generates scripts that are send to the backend for execution. The backend relies on spark to ensure scalability.

Because building a complete toolkit is is rather ambitious, we focus on the use case of vocabulary cleanup for full text data. When working with full text data, pre-processing often consists of tokenizing texts (i.e., splitting them into words), lematizing or stemming the tokens, and performing some kind of filtering to remove typo's and other unwanted tokens. The data cleaning toolkit should support customizing these tasks, and provide visualizations that facilitate vocabulary cleanup.
