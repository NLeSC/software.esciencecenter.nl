---
codeRepository: https://github.com/NLeSC/pycoeman
competence:
- Efficient Computing
contactPerson: /person/o.rubi
contributingOrganization:
- /organization/nlesc
contributor:
- /person/o.rubi
dependency:
dependencyOf:
- /software/pymicmac
discipline:
- eScience Methodology
downloadUrl: https://github.com/NLeSC/pycoeman
expertise:
- Distributed Computing
involvedOrganization:
- /organization/nlesc
license:
- apache-2.0
name: pycoeman
owner:
- /organization/nlesc
programmingLanguage:
- Python
startDate: 2016-07-25
status: active
supportLevel: specialized
tagLine: pycoeman (Python Commands Execution Manager) is a Python toolkit for executing command-line commands.
technologyTag:
- Distributed
- workflow
- Library
usedIn:
- /project/improving-photogrammetry
user:
- /person/o.rubi
---
Python Commands Execution Manager

pycoeman is a Python toolkit for executing command-line commands. It allows the execution of:

- Sequential commands: this is a chain of command-line commands which will be executed one after the other. In other words, this is a set of commands that you would traditionally execute in a Bash script. Normally there are IO dependencies between commands (one command requires the output from one or previous ones).

- Parallel commands: this is a set of command-line commands which are executed in parallel. In other words, this is a set of commands that you would traditionally execute in a Bash script with all the commands as background jobs (with the & at the end). There cannot be IO dependencies between commands. This is can be useful for pleasingly parallel solutions, i.e. tools which are single-core at programming level but can be parallelized at data level and usually require some final merging process.

pycoeman adds CPU/MEM/disk monitoring during the execution of the commands and it allows to create clean execution environments for easier management of your executions (the commands will be executed in different folders separated from where the input data is). pycoeman has tools to run both sequential and parallel commands locally (in the local computer), and also to run parallel commands in a set of remote hosts accessible via SSH as well as in SGE clusters (computer clusters with Sun Grid Engine batch-queuing system). pycoeman is configured using XML files.
