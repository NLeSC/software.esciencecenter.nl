---
competence:
- Optimized Data Handling
- Big Data Analytics
contactPerson: /person/r.goncalves
dataFormat:
- LAS/LAZ
- GML
dataMagnitude: TB
discipline:
- eScience Methodology
engineer:
- /person/r.goncalves
expertise:
- Information Visualization
- Information Integration
- Databases
endorsedBy:
- /organization/nlesc
involvedOrganization:
- /organization/cwi
- /organization/monetdb
- /organization/geodan
- /organization/tu-delft
- /organization/vua
- /organization/fugro
logo: /images/project/big-data-analytics-in-the-geo-spatial-domain.jpg
name: Big-Data-Analytics-in-the-Geo-Spatial-Domain
tagLine: 'Strategic partnership: Big Data Analytics in the Geo-Spatial Domain'
uses:
- /software/monetdb
- /software/datavaults
- /software/liblas
---
Digital 3D city models play a crucial role in research of urban phenomena; they form the basis of flow simulations (wind streams, water runoff and heat island effects), urban planning and analysis of underground formations. Urban scenes consist of large collections of complex objects which have rich semantic properties, such as materials and colors. Modeling and storing these properties indicating the relationships between them is best handled in a relational database.

Database management systems (DBMSs) are a well-established solution when it comes to archiving, filtering, analysis, and correlation of large data collections. Ability to perform analysis near data is one of the key requirements identified by the 4th Paradigm to handle the data deluge. A single spatial DBMS offers functionality for geo-spatial modeling and management of semantic properties in one place, thus avoiding the need for multiple software tools associated with high volume data transfer and format transformations.

The provision of spatial and geo-spatial features in database systems needs to be extended and brought to maturity to fulfill the requirements of real-world scientific applications. A class of DBMSs, called column-stores, has proven efficiency for analytical applications on extremely large datasets. In fact, all major DBMS vendors have extended their product spectrum with column-oriented solutions to address the needs of analytical applications. The aim of this project is to develop and mature the spatial features of the column-store open-source MonetDB. It has established a track record in high-performance analytical applications and demonstrated its ability to inject database technology successfully in several science domains, such as astronomy, remote sensing, seismology, and navigation.

The technology will be applied to a concrete use case of the Port of Rotterdam in which a 3D GIS is built to aid various multi-stakeholder construction projects where new structures are built in, on top of and around the existing port (underground) infrastructure. Extending and modifying the port is challenging as it is home to many different companies that often cover extensive areas and manage vast (underground) infrastructures such roads, pipes and cables. The port thus requires a 3D GIS that is able to store all harbor assets and analyze existing assets with future interventions and detect conflicts. The 3D GIS currently being built is aimed at collecting data from different sources and formats (BIM and GIS) and converting it to a common format to enable 3D operations and analyses such as 3D intersections, 3D buffers as well as simplification and generalization of GIS and (especially) BIM models for visualization purposes.

The goals of the strategic partnership and the expected project outcome is as follows: database extension for storage and indexing of 3D point clouds with properties that are suitable for and take advantage of column-oriented internal data organization; database extension for storage and indexing of 3Dvoxels with properties that are suitable for and take advantage of column-storage; the extensions will be evaluated with data and processing requirements of the use case of port of Rotterdam.

The development will rely as much as possible on existing open-source tools and libraries. The proposed (geo-) spatial data analytics tools will extend the eScience Technology Platform (eSTeP) and be offered as an associated technology available to the NLeSC projects and other eScience projects in national and international context.
