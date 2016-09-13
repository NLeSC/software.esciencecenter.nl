---
competence:
- Optimized Data Handling
- Big Data Analytics
contactPerson: /person/v.hees
dataFormat:
- NetCDF
dataMagnitude: GB
discipline:
- eScience Methodology
engineer:
- /person/v.hees
expertise:
- Databases
endorsedBy:
- /organization/nlesc
involvedOrganization:
- /organization/cwi
logo: /images/project/compressing-the-sky-into-a-large-collection-of-statistical-models.jpg
name: Compressing the Sky Into a Large Collection of Statistical Models
tagLine: 'PathFinder project: Compressing the sky into a large collection of statistical
  models'
uses:
- /software/monetdb
---
Time-domain astronomy opens up a new era of observational astronomy, covering the spectrum from radio and millimeter to optical wavelengths. The data avalanches from their instruments forces us to overhaul contemporary data storage, data management, and data analytics techniques. 

Rather than endlessly piling observations onto fleets of hard drives, raw observations could be replaced with more compact model-based representations founded in astrophysics. A well-fitting model has the potential of reducing the storage footprint by several orders of magnitude. The result should, however, be still easy to query and amendable for further analysis within a priori known statistical bounds.

The scientific challenge is to find efficient algorithms to fit many statistical models in millions of seemingly independent observations. Their representation should provide the means to control the information loss that may result from statistical compression, as added noise could destroy effects to be discovered at a later stage in the data analytics pipeline.

In the LOFAR Transients Key Science project a database management infrastructure is in place to take the output of the image production pipeline to populate the LOFAR catalog. This database is expected to grow at a rate of 50TB per year. One of the key limitations of such sizeable databases in the context of data exploration is the time to scan the data for events of interest. The scientist needs to learn what to ask.

One way to improve the exploration phase is to exploit the statistical properties of the growing collection of observations and semantically compress them into parameterized formulae. An astrophysical object with a stable light curve can be replaced by its average flux and a Gaussian error dispersion model. Periodicallly varying objects can be classified and represented by deterministic components of their signal wave models.

The eScience technology addressed is primarily aimed at Optimized Data Handling with a drive to cut down the cost of Big Data Analytics through proper (continuous) preprocessing of the observational data. The existing open-source database system MonetDB, supporting the LOFAR transient database, is extended.

The particular approach towards semantic driven database compression, in combination with the Blaeu visual data exploration tool developed at CWI, is likely to open a vista of hitherto unseen approaches to understand and explain the characteristics of the astrophysical objects. The strong embedding in LOFAR, BlackGem and emerging SKA infrastructures secure a direct route towards scientific discoveries by the astronomers engaged.
