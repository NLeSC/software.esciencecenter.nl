---
codeRepository: https://github.com/NLeSC/xtas
competence:
- Efficient Computing
- Big Data Analytics
contactPerson: /person/j.attema
contributingOrganization:
- /organization/nlesc
contributor:
- /person/l.veen
discipline:
- Humanities & Social Sciences
documentationUrl: http://nlesc.github.io/xtas/setup.html
expertise:
- Text Mining
- Distributed Computing
- Information Retrieval
involvedOrganization:
- /organization/nlesc
- /organization/uva
license:
- apache-2.0
name: xtas
endorsedBy:
- /organization/nlesc
nlescWebsite: https://www.esciencecenter.nl/technology/software/xtas
owner:
- /organization/nlesc
- /organization/uva
usedIn:
- /project/candygene
- /project/texcavator
programmingLanguage:
- Java
- Python
startDate: 2013-01-01
status: active
supportLevel: basic
tagLine: the eXtensible Text Analysis Suite
technologyTag:
- NER
- NLP
- Parsing
- Sentiment analysis
user:
- /organization/nlesc
- /organization/uva
- /person/p.bos
website: http://nlesc.github.io/xtas/
website: http://xtas.net/
---
xtas is a collection of natural language processing and text mining tools, brought together in a single software package with built-in distributed computing and support for the Elasticsearch document store.

xtas functionality consists partly of wrappers for existing packages, with automatic installation of software and data; and partly of custom-built modules coming out of research. Currently offered are various parsers for Dutch and English (Alpino, CoreNLP, Frog, Semafor), named entity recognizers (Frog, Stanford and custom-built ones), a temporal expression tagger (Heideltime) and a sentiment tagger based on SentiWords.

A basic installation of xtas works like a Python module. Built-in package management and a simple, uniform interface take away the hassle of installing, configuring and using many existing NLP tools.

xtas's open architecture makes it possible to include custom code, run this in a distributed fashion and have it communicate with Elasticsearch to provide document storage and retrieval.
