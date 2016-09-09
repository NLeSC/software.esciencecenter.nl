---
name: Chemical Analytics Virtual Machine
endorsedBy:
- /organization/nlesc
tagLine: Packer template to create Vagrant box with Knime inside
codeRepository: https://github.com/NLeSC/Chemical-Analytics-Platform
website: https://github.com/NLeSC/Chemical-Analytics-Platform
downloadUrl: https://atlas.hashicorp.com/nlesc/boxes/chemical-analytics-platform
documentationUrl: https://github.com/NLeSC/Chemical-Analytics-Platform/wiki
programmingLanguage:
- YAML
license:
- apache-2.0
competence:
- Optimized Data Handling
discipline:
- eScience Methodology
expertise:
- Reproducible Research
supportLevel: specialized
contactPerson: /person/s.verhoeven
owner:
- /organization/nlesc
- /organization/radboud.university.nijmegen
- /organization/vua
contributingOrganization:
- /organization/nlesc
contributor:
- /person/s.verhoeven
- name: Ross McGuire
  affiliation:
  - /organization/radboud.university.nijmegen
  linkedInUrl: https://nl.linkedin.com/in/ross-mcguire-71457523
involvedOrganization:
- /organization/nlesc
- /organization/radboud.university.nijmegen
- /organization/vua
usedIn:
- /project/3d-e-chem
startDate: 2015-08-05
status: active
technologyTag:
- Knime
- Vagrant
- Packer
dependencyOf:
- /software/3d-e-chem-vm
---
Scripts to create a Vagrant box using packer and ansible.

Vagrant box is a Virtual Machine in Virtualbox format.

Start virtual machine with

```
vagrant init nlesc/chemical-analytics-platform
vagrant up
```
