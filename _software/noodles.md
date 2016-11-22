---
codeRepository: https://github.com/NLeSC/noodles
competence:
- Efficient Computing
contactPerson: /person/j.hidding
contributingOrganization:
- /organization/nlesc
contributor:
- /person/j.hidding
- /person/b.weel
- affiliation:
  - /organization/vua
  githubUrl: https://github.com/felipeZ
  name: Felipe Zapata
dependency:
- /software/xenon
- /software/pyxenon
dependencyOf:
- /pymicmac
- /software/pymicmac
discipline:
- Life Sciences & eHealth
- eScience Methodology
documentationUrl: http://nlesc.github.io/noodles/sphinxdoc/html/index.html
expertise:
- Orchestrated Computing
endorsedBy:
- /organization/nlesc
involvedOrganization:
- /organization/nlesc
- /organization/vua
license:
- lgpl-3.0
name: Noodles
nlescWebsite: https://www.esciencecenter.nl/technology/software/noodles
owner:
- /organization/nlesc
programmingLanguage:
- Python
startDate: 2015-10-11
status: active
supportLevel: specialized
tagLine: Programmable workflow engine for Python.
technologyTag:
- workflow
usedIn:
- /project/computational-chemistry-made-easy
- /project/improving-photogrammetry
user:
- /organization/nlesc
- /organization/vua
- /person/j.hidding
- /person/o.rubi
- /person/l.ridder
website: http://nlesc.github.io/noodles/
---
Noodles is a programmable workflow engine for Python. It can be used to parallelize your code with minimal effort.

# Why Noodles?

The primary goal of Noodles is to make it easy to run jobs on cluster supercomputers, in parallel, straight from a Python shell. The user enters a Python script that looks and feels like a serial program. The Noodles engine then converts this script into a call graph. This graph can be executed on a variety of machines using the different back-end runners that Noodles provides. This is not so much a design driven by technology but by social considerations. The end user may expect an elegant, easy to understand, interface to a computational library. This user experience we refer to as eating of noodles.

The computational library that is exposed to the user by means of Noodles needs to adhere to some design principles that are more strict than plain Python gives us. The library should follow a functional style of programming and is limited by the fact that function arguments need to pass through a layer where data is converted to and from a JSON format. The design of such a library is the cooking of noodles. As it is with ramen noodles, ofttimes the cook is also an avid consumer of noodles.

The complexity of running a workflow in parallel on a wide variety of architectures is taken care of by the Noodles engine. This is the production of noodles which is left as an exercise for the Noodles dev-team at the Netherlands eScience Center.
