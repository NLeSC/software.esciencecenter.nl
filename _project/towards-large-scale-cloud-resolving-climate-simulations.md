---
name: Towards Large-Scale Cloud-Resolving Climate Simulations
tagLine: 'Towards Large-Scale Cloud-Resolving Climate Simulations: A new 3d-super-parameterization approach'
nlescWebsite: https://www.esciencecenter.nl/project/primavera
website:
logo: https://www.esciencecenter.nl/img/projects/p56-large.jpg
competence:
- Big Data Analytics
- Efficient Computing
discipline:
- Environment & Sustainability
expertise:
- 'Data Assimilation'
- 'Scientific Visualization'
- 'Distributed Computing'
- 'High Performance Computing'
infrastructure: 'Supercomputer'
dataMagnitude: 'GB'
dataFormat:
- NetCDF
- Grib
- HDF5
- CSV
contactPerson: /person/g.vandenoord
coordinator: http://software.esciencecenter.nl/person/r.bakhshi
engineer:
- http://software.esciencecenter.nl/person/g.vandenoord
principalInvestigator:
- name: Prof. Daan Crommelin
  affiliation:
  - http://software.esciencecenter.nl/organization/cwi
  - http://software.esciencecenter.nl/organization/uva
  website: http://homepages.cwi.nl/~dtc/
  description: "Prof. Daan Crommelin is leader of the Scientific Computing research group at CWI Amsterdam, and professor at the KdV Institute for Mathematics, University of Amsterdam. His research interests include stochastic and computational methods for multiscale dynamical systems, rare event simulation, applications in atmosphere‐ocean-climate science and energy networks."

  photo: https://www.esciencecenter.nl/img/team/Daan-Crommelin-eScience.jpg
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/cwi
- http://software.esciencecenter.nl/organization/knmi
uses:

---
Clouds and convection processes are important for the climate system, yet they are not explicitly resolved in global climate models due to computational limitations. The approximate parameterized representation of these processes is the main source of model uncertainty in climate models and has hampered progress in our understanding of the interaction between clouds and the large-scale circulation for decades.

We will pursue a new 3d-super-parameterization (3d-SP) approach to overcome this conundrum. This approach builds further on super-parameterization (SP) approach, proposed 15 years ago. We will nest 3-dimensional Large Eddy Simulation (LES) models into the grid columns of a Global Circulation Model.

This way, the parameterized descriptions of clouds, convection and turbulence with all their shortcomings will be replaced by a realistic 3-dimensional simulation technique for these processes.

Although computationally more expensive than traditional parameterizations and conventional super-parameterization, this approach is ideally suited to take full advantage of present-day parallel computers because of the minimal communication between the LES models and will be much more efficient than a direct simulation on the large scale at the resolution of the nested LES model.


This project team will use state-of-the-art high performance computing (HPC) technologies to make this approach feasible and within reach of modern supercomputers. Furthermore, the team plans to employ recently developed algorithmic approaches to further speed up computations.

The overarching goal is to develop and explore a computational tool that is able to realistically resolve the interaction between the large-scale atmospheric circulation and the smaller scale cloud and convective processes.

Image source: [Perhaps the most impressive of cloud formations, cumulonimbus (from the Latin for “pile” and “rain cloud”) clouds form due to vigorous convection (rising and overturning) of warm, moist, and unstable air – by NASA](http://eol.jsc.nasa.gov/SearchPhotos/photo.pl?mission=ISS016&roll=E&frame=27426)
