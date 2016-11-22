---
name: Docker Couch Admin
endorsedBy:
- /organization/nlesc
tagLine: Configures a web service using angular-schema-form and CouchDB
codeRepository: https://github.com/NLeSC/docker-couch-admin
downloadUrl: https://hub.docker.com/r/nlesc/couch-admin/
doi: http://dx.doi.org/10.5281/zenodo.61301
programmingLanguage:
- JavaScript
- HTML
- Dockerfile
license:
- apache-2.0
competence:
- Efficient Computing
discipline:
- eScience Methodology
expertise:
- Information Integration
supportLevel: specialized
contactPerson: /person/j.borgdorff
owner:
- /organization/nlesc
contributingOrganization:
- /organization/nlesc
contributor:
- /person/j.borgdorff
user:
- /organization/nlesc
involvedOrganization:
- /organization/nlesc
usedIn:
- /project/simcity
startDate: 2016-01-07
status: inactive
dependency:
- /software/couchdb
dependencyOf:
technologyTag:
- Docker
- CouchDB
- AngularJS
- JSON Schema
---
A Docker image with a customisable CouchDB administration console, using
angular-schema-form. All configuration is readable from the CouchDB database.

This is specifically used to have dynamic but shared configuration in a set of
Docker containers. The configuration is accessible from a web interface.
