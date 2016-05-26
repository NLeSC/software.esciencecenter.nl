---
name: "Texcavator"
tagLine: Facilitating and supporting large-scale text mining in the field of digital humanities
nlescWebsite: https://www.esciencecenter.nl/project/texcavator
logo: http://www.esciencecenter.nl/img/projects/1.P023-large.jpg
competence:
  - Big Data Analytics
discipline:
  - Humanities & Social Sciences
expertise:
  - Information Retrieval
  - Text Mining
  - Distributed Computing
  - Information Visualization
infrastructure: Elasticsearch for indexing and searching newspaper data
dataMagnitude: GB
dataFormat:
- XML
contactPerson: http://software.esciencecenter.nl/person/j.vanderzwaan
engineer:
- http://software.esciencecenter.nl/person/j.vanderzwaan
principalInvestigator:
  - name: Prof. Joris van Eijnatten
    affiliation:
    - http://software.esciencecenter.nl/organization/uu
    website: http://www.uu.nl/medewerkers/JvanEijnatten/
  - name: Prof. Toine Pieters
    affiliation:
    - http://software.esciencecenter.nl/organization/uu
    website: http://www.uu.nl/staff/AHLMPieters/
  - name: Dr. Jaap Verheul
    affiliation:
    - http://software.esciencecenter.nl/organization/uu
    website: http://www.uu.nl/staff/JVerheul/
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/uva
- http://software.esciencecenter.nl/organization/uu
- http://software.esciencecenter.nl/organization/surfsara
uses:
- http://software.esciencecenter.nl/software/texcavator
- http://software.esciencecenter.nl/software/xtas
startDate: 2013-12-04
endDate: 2015-03-20
---

Texcavator is a text mining application used for historical research. It is an
interface to an Elasticsearch index (specifically, an ES index containing the
KB newspaper archive from 1850 - 1990) that allows users to perform full text
searches and to visualize the results (in word clouds and/or time lines).
Texcavator was build on top of previous applications (WAHSP and Biland).
The goals of this project were:

1. Improvement of the overall stability and maintainability of the software
2. Analysis and improvement of scalability  

Most time was spend on refactoring the back end. The quality of the original
Texcavator software was very low; it was clearly organically grown (instead of
engineered) and documentation and unit tests were lacking.

One of the main problems was scalability of word cloud generation.
In the old version of Texcavator, this could take hours (even though the
maximum number of documents was limited to 10000 documents) and often failed
without giving an error message.
We wanted to use standard Elasticsearch functionality to generate the word
clouds (i.e., terms aggregations). However, this proved to be infeasible,
because of the large amount of words in the data set (the number of unique
words in the corpus is too big (mostly due to OCR mistakes) to keep in memory,
which is required to be able to use terms aggregations). We came up with two
alternative approaches: term vector word clouds and tag word clouds and
implemented the term vector word clouds. Word cloud generation is now faster
(minutes instead of hours).

After the test version of Texcavator was put online, a user session was
organized to test the performance of Texcavator when multiple users use the
application at the same time and to identify other problems with the
application. The session was a success in the sense that multiple users
(~10) were able to use the application at the same time without noticable
effects on performance (Texcavator remained responsive).
