---
name: Cross-perspective Topic Modeling
tagLine: A Gibbs sampler that implements Cross-Perspective Topic Modeling
codeRepository: https://github.com/NLeSC/cptm
nlescWebsite:
website:
documentationUrl:
logo:
doi: http://dx.doi.org/10.5281/zenodo.47756
programmingLanguage:
- Python
- Cython
license:
- apache-2.0
competence:
- Big Data Analytics
discipline:
- Humanities & Social Sciences
expertise:
- Text Mining
supportLevel: specialized
contactPerson: http://software.esciencecenter.nl/person/j.vanderzwaan
owner:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/uva
contributor:
- http://software.esciencecenter.nl/person/j.vanderzwaan
- http://software.esciencecenter.nl/person/l.buitinck
- http://software.esciencecenter.nl/person/p.bos
user:
- http://software.esciencecenter.nl/organization/nlesc
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/uva
usedIn:
- http://software.esciencecenter.nl/project/dilipad
startDate: 2016-03-17
status: inactive
dependency:
dependencyOf:
technologyTag:
- Topic Modeling
- Latent Dirichlet Allocation
- Gibbs Sampler
---
A Gibbs sampler that implements Cross-Perspective Topic Modeling, as described in

> Fang, Si, Somasundaram, & Yu (2012). Mining Contrastive Opinions on Political Texts using Cross-Perspective Topic Model. In proceedings of the fifth ACM international conference on Web Search and Data Mining. http://dl.acm.org/citation.cfm?id=2124306

The cross-perspective topic model is an extended form of Latent Dirichlet Allocation
(LDA). Topics are learned by doing LDA on the topic words (nouns) in
the corpus. Opinions are learned from a separate LDA process using opinion words
(adjectives, verbs, and adverbs). A topic is a probability distribution
over topic words. An opinion is a probability distribution over opinion words.
While the topics are shared among the entire corpus, opinions depend on the perspective
a document belongs to. A document can only belong to a single perspective, and the
division of the corpus in perspectives is fixed and must be known in advance.

The imaginary process for generating documents is: one first selects a topic,
based on the topic mixture of that document. Then a topic word is drawn from the
topic. This procedure is repeated until all topic words have been selected.
Next, one selects an opinion based on the frequency of topic words associated
with the topics in the document. The more words associated with a certain topic,
the higher the chance that the corresponding opinion will be selected. The
contents of the opinion (i.e., probabilities of opinion words) depend on the
generator's perspective. Next, an opinion word is drawn from the selected opinion.
This procedure is again repeated until all opinion words have been selected.
