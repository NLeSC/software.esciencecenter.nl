---
name: ReciPy
endorsedBy:
- /organization/nlesc
tagLine: Effortless provenance in Python
codeRepository: https://github.com/recipy/recipy
programmingLanguage:
- Python
license:
- apache-2.0
competence:
- Big Data Analytics
discipline:
- eScience Methodology
expertise:
- Reproducible Research
supportLevel: advanced
contactPerson: /person/j.vanderzwaan
owner:
- name: Robin Wilson
  affiliation:
  - /organization/university.of.southampton
  website: http://www.rtwilson.com
- /organization/nlesc
contributingOrganization:
- /organization/nlesc
contributor:
- name: Robin Wilson
  affiliation:
  - /organization/university.of.southampton
  website: http://www.rtwilson.com
- /person/j.vanderzwaan
user:
- /organization/nlesc
involvedOrganization:
- /organization/nlesc
startDate: 2015-03-27
status: active
technologyTag:
- Provenance
---
Imagine the situation: You've written some wonderful Python code which produces a beautiful graph as an output. You save that graph, naturally enough, as "graph.png". You run the code a couple of times, each time making minor modifications. You come back to it the next week/month/year. Do you know how you created that graph? What input data? What version of your code? If you're anything like me then the answer will often, frustratingly, be “no”. Of course, you then waste lots of time trying to work out how you created it, or even give up and never use it in that journal paper that will win you a Nobel Prize…

ReciPy (from *recipe* and *python*) is a Python module that will save you from this situation! (Although it can't guarantee that your resulting paper will win a Nobel Prize!) With the addition of a single line of code to the top of your Python files, ReciPy will log each run of your code to a database, keeping track of the input files, output files and the version of your code, and then let you query this database to find out how you actually did create "graph.png".

When you import recipy it adds a number of classes to "sys.meta_path". These are then used by Python as part of the importing procedure for modules. The classes that we add are classes derived from "PatchImporter", often using the easier interface provided by "PatchSimple", which allow us to wrap functions that do input/output in a function that calls recipy first to log the information.

Currently, ReciPy provides patches for:

* numpy
* pandas
* matplotlib.pyplot
* gdal
* sklearn
* nibabel
