---
name: Texcavator
endorsedBy:
- /organization/nlesc
tagLine: Texcavator is a text mining application used for historical research
codeRepository: https://github.com/UUDigitalHumanitieslab/texcavator
nlescWebsite:
website: http://texcavator.surfsaralabs.nl/
documentationUrl:
logo:
programmingLanguage:
- Python
- JavaScript
license:
- apache-2.0
competence:
- Big Data Analytics
discipline:
- Humanities & Social Sciences
expertise:
- Information Retrieval
- Text Mining
- Distributed Computing
- Information Visualization
supportLevel: advanced
contactPerson: /person/j.vanderzwaan
owner:
- /organization/nlesc
- /organization/uva
- /organization/uu
contributingOrganization:
- /organization/nlesc
contributor:
- /person/j.vanderzwaan
- name: Martijn van der Klis
  affiliation:
  - /organization/uu
  website: http://www.uu.nl/staff/MHvanderKlis/
user:
- /organization/uu
involvedOrganization:
- /organization/nlesc
- /organization/uva
- /organization/uu
usedIn:
- /project/texcavator
- /project/shico
startDate: 2013-12-04
status: inactive
dependency:
dependencyOf:
technologyTag:
- Elasticsearch
- Django
- Dojo Toolkit
---
Texcavator is a text mining application used for historical research using newspaper data (the KB newspaper archive).
The newspaper articles are stored in an Elasticsearch index.
Django is used for user management and other functionality that requires storing information in a relational database (as opposed to storing documents in Elasticsearch). Because the KB data is not public, every user has their own login. Also, users can save queries (currently, a saved query is required to be able to generate word clouds and time lines). User data is stored in a (MySQL) database; Django provides a convenient interface to the database and provides standard functionality for manipulating database records. A disadvantage of Django is that the front end (user interface) and back end are somewhat intertwined. On top of that, the user interface (implemented in Dojo version 1.8.6) directly retrieved and updated information in the database in some cases.
