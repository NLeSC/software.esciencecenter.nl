---
name: "Digging into Parliamentary Data (DiLiPaD)"
tagLine: A new approach to the history of parliamentary communication and discourse
nlescWebsite: https://www.esciencecenter.nl/project/dilipad
competence:
  - Big Data Analytics
discipline:
  - Humanities & Social Sciences
expertise:
  - Text Mining
infrastructure:
dataMagnitude: GB
dataFormat:
- XML
contactPerson: http://software.esciencecenter.nl/person/j.vanderzwaan
engineer:
- http://software.esciencecenter.nl/person/j.vanderzwaan
principalInvestigator:
  - name: Dr. Maarten Marx
    affiliation:
    - http://software.esciencecenter.nl/organization/uva
    website: http://mashup2.science.uva.nl/marx/
  - name: Dr. Jaap Kamps
    affiliation:
    - http://software.esciencecenter.nl/organization/uva
    website: http://humanities.uva.nl/~kamps/
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/uva
uses:
- http://software.esciencecenter.nl/software/cptm
startDate: 2014-12-18
endDate: 2016-04-01
---

The goals of the DiLiPad project were to:

1. Implement cross-perspective topic modeling (cptm)
2. Adapt cptm in order to be able to track changes in opinions over time
3. Validate the results on Dutch parliamentary proceeding

Cross-perspective topic modeling is an existing topic modeling technique to
extract viewpoints (opinions) from text data. The first step was to implement
the algorithm. This resulted in a Python module to do cross-perspective topic.

Cross-perspective topic modeling requires the corpus to be divided in
perspectives (in case of the Dilipad project, a perspective is a political party).
To take into account the time parameter, we decided to further divide the data
(instead of having a perspective for a political party, we now have a perspective
for a political party during a government term).

For the validation study, cross-perspective topic modeling was applied to an existing
dataset of Dutch parliamentary proceedings. The results show that the
method yields valid topics (content and criterion validity). While opinions
were found to be representative of the political parties' positions as expressed
in party manifestos (content validity), we were unable to find correlation
between opinions and positions on the left/right political spectrum (criterion validity).
Further work is required to determine whether differences between opinions
correlate with other politically meaningful dimensions. We also propose to
investigate the effect of improving topic and opinion quality on the validation
results.
