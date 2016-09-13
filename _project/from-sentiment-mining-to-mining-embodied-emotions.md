---
competence:
- Big Data Analytics
contactPerson: /person/j.vanderzwaan
dataFormat:
- XML
- KAF
dataMagnitude: MB
discipline:
- Humanities & Social Sciences
endDate: 2015-06-30
engineer:
- /person/j.vanderzwaan
expertise:
- Text Mining
- Machine Learning
- Information Visualization
endorsedBy:
- /organization/nlesc
involvedOrganization:
- /organization/nlesc
- /organization/vua
- /organization/meertens
logo: /images/project/from-sentiment-mining-to-mining-embodied-emotions.jpg
name: Emotional styles on the Dutch stage between 1600-1800
nlescWebsite: https://www.esciencecenter.nl/project/from-sentiment-mining-to-mining-embodied-emotions
principalInvestigator:
- affiliation:
  - /organization/vua
  name: Prof. Inger Leemans
  website: http://www.fgw.vu.nl/nl/over-de-faculteit/medewerkers/medewerkers-i-l/prof-dr-i-leemans/index.aspx
publication:
- http://dx.doi.org/10.1109/eScience.2015.18
startDate: 2015-03-01
tagLine: Tracing emotion styles in theater texts
uses:
- /software/heem-dataset
---
The goals of the project were to develop a methodology to identify changes
over time in the relationship between emotional expressions and body parts in
(historical) texts and  to apply this methodology to 17th and 18th century
Dutch theatre texts.

The most important contribution (eScience-wise) is that we demonstrate that
a multi-label text classification approach to learning complex emotion models
on historical data is feasible. There are two parts to this contribution: 1)
in contrast to related work on emotion mining, our emotion model is more complex
(i.e., contains many more labels (42 instead of 6 or 8)), and 2) related work on
emotion/sentiment mining uses modern and mostly web-based texts. The historical
texts used in the embodied emotions project pose specific challenges (spelling
variation and the lack of NLP tools that work on historical text).
These results were published in IEEE eScience 2015.

## Approach

1. Select (and prepare) corpus
2. Create annotation schema
3. Annotate texts
4. Compare manual annotation to existing sentiment mining techniques
4. Do machine learning with annotated texts and analyze the results

A lot of time was spend on data selection and curation. The annotation schema
was created by the domain experts. It consists of 42 labels
on two layers (emotion labels and concept types). Existing work on emotion mining
uses much simpler emotion models (6 to 8 labels). Details about the emotion model
can be found in the IEEE eScience paper and the domain papers.

The annotation corpus was annotated by domain experts. To check the consistency
and reliability of the annotations, an inter-annotator study was carried out.
The results of this study show that annotating texts using our annotation scheme
was quite difficult. See the IEEE eScience paper for details.

The manual annotations were compared to existing sentiment mining techniques,
including Linguistic Inquiry and Word Count (LIWC)
a dictionary method that counts the occurences of words in different
(psychological) categories, including postive and negative emotions.

For the machine learning part of the project, we followed the approach used in
the SpuDisc project; the problem of predicting labels from our emotion model was
treated as a multi-label text classification task. We experimented with two
algorithms for multi-label classification: Binary Relevance (BR) and
Random k-Labelsets (RAkEL). Linear Support Vector Machines (SVM) using
standard bag-of-words features with tf-idf weighting and stop
word removal were trained for both classification algorithms.
We also experimented with spelling normalization. More details about our method
and results can be found in the IEEE eScience paper.

The text classifiers trained were applied to a corpus of 250 texts. The results
were analysed to gain insight on how emotions and the embodiment of emotions
change over time.
