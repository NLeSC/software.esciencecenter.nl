---
name: CollateX
tagLine: Software for Collating Textual Sources
endorsedBy:
- /organization/huygens
codeRepository: https://github.com/interedition/collatex/
programmingLanguage:
- JavaScript
- Python
- Java
license:
- gpl-3.0
competence:
- Big Data Analytics
discipline:
- Humanities & Social Sciences
expertise:
- Text Mining
involvedOrganization:
- /organization/huygens
status: active
---
CollateX is software that

* reads multiple (≥ 2) versions of a text, splitting each version into parts (tokens) to be compared,
* identifies similarities of and differences between the versions (including moved/transposed segments) by aligning tokens, and
* outputs the alignment results in a variety of formats for further processing, for instance
* to support the production of a critical apparatus or the stemmatical analysis of a text's genesis.

It resembles software used to compute differences between files (e.g. diff) or tools for sequence alignment which are commonly used in Bioinformatics. While CollateX shares some of the techniques and algorithms with those tools, it mainly aims for a flexible and configurable approach to the problem of finding similarities and differences in texts, sometimes trading computational soundness or complexity for the user's ability to influence results.

As such it is primarily designed for use cases in disciplines like Philology or – more specifically – the field of Textual Criticism where the assessment of findings is based on interpretation and therefore can be supported by computational means but is not necessarily computable.
