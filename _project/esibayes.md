---
competence:
- Big Data Analytics
- Efficient Computing
contactPerson:
- /person/j.spaaks
- /person/s.branchett
coordinator: /person/s.branchett
dataFormat:
- MATLAB
dataMagnitude: GB
discipline:
- eScience Methodology
engineer:
- /person/j.spaaks
expertise:
- Machine Learning
- Data Assimilation
- Distributed Computing
- High Performance Computing
endorsedBy:
- /organization/nlesc
infrastructure: surfSARA's LISA cluster
involvedOrganization:
- /organization/uva
- /organization/surfsara
- /organization/nlesc
logo: /images/project/esibayes.jpg
name: esibayes
nlescWebsite: https://www.esciencecenter.nl/project/esibayes
principalInvestigator:
- affiliation:
  - /organization/uva
  name: Willem Bouten
  photo: https://www.esciencecenter.nl/img/team/willem-bouten-bw.jpg
  website: http://www.uva.nl/over-de-uva/organisatie/medewerkers/content/b/o/w.bouten/w.bouten.html
tagLine: An eScience infrastructure for Bayesian inverse modeling
uses:
- /software/mmsoda-toolbox-for-matlab
---
An eScience infrastructure for Bayesian inverse modeling

We have developed a parallel MATLAB version of SODA (Vrugt et al., 2005) that makes use of MPI. The software package is called 'The MMSODA Toolbox for MATLAB', or MMSODA for short (MMSODA stands for MATLAB-MPI-SODA).

MMSODA offers the functionality of a number of previously separate softwares, namely SCEM-UA (Vrugt _et al_., 2003b), SODA (Vrugt _et al._, 2005a,b; Clark and Vrugt, 2006), MOSCEM-UA (Vrugt _et al._, 2003a), multi-objective SODA (Vrugt _et al._, 2008), the MPITB-parallel version of SCEM-UA implemented in Octave (Vrugt _et al._, 2006b), and the MPITB-parallel version of SODA implemented in Octave (Vrugt _et al._, 2006a). Additionally, MMSODA offers a parallel version of multi-objective SCEM-UA, and a parallel version of multi-objective SODA, both of which did not exist previously. Moreover, MMSODA does not use Octave when running in parallel, because Octave does not evaluate code as quickly as does MATLAB. MMSODA circumvents (in a legal fashion) the license requirements that are often an impediment to parallel computation by compiling the MATLAB code into a binary which can be run without any license. Compiling the binary, however, does require a license, both for the MATLAB program itself, as well as for the MATLAB Compiler Runtime Toolbox. Fortunately, the required licenses are available on most cluster environments targeting a scientific and engineering audience.

In short, the acronyms mentioned above mean that: MMSODA can do parameter tuning with or without intermediate state updating by an ensemble Kalman Filter; that MMSODA supports both single-objective and multi-objective optimization; and that the optimization can be run either sequentially on a local machine, or in parallel on a cluster computer.

The serial/parallel capability is particularly attractive, since it allows the users to set up their optimizations locally on their own machines, thus ensuring a familiar development environment without the need to make the code compatible with Octave syntax. When the user finishes setting up the optimization, running it on a cluster computer is simply a matter of copying the relevant directory to the cluster storage using standard tools (e.g. WinSCP) and compiling the software by executing a script that comes with the software. Furthermore, MMSODA is fully documented with HTML documentation which can be accessed in the same way as MATLAB's built-in commands, namely through the ``doc`` command.

_References_

- J. A. Vrugt, H. V. Gupta, L. A. Bastidas, W. Bouten, and S. Sorooshian. Effective and efficient algorithm for multi-objective optimization of hydrologic models. Water Resources Research, 39(8):1214, 2003a. doi: 10.1029/2002WR001746.
- J. A. Vrugt, H. V. Gupta, W. Bouten, and S. Sorooshian. A Shuffled Complex Evolution Metropolis algorithm for optimization and uncertainty assessment of hydrologic model parameters. Water Resources Research, 39(8):1201, 2003b. doi: 10.1029/2002WR001642.
- Jasper A. Vrugt, Cees G. H. Diks, Hoshin V. Gupta, Willem Bouten, and Jacobus M. Verstraten. Improved treatment of uncertainty in hydrologic modeling: Combining the strengths of global optimization and data assimilation. Water Resources Research, 41:W01017, 2005a. doi: 10.1029/2004WR003059.
- Jasper A. Vrugt, Bruce A. Robinson, and Velimir V. Vesselinov. Improved inverse modeling for flow and transport in subsurface media: Combined parameter and state estimation. Geophysical Research Letters, 32:L18408, 2005b. doi: 10.1029/2005GL023940.
- Jasper A. Vrugt, Hoshin V. Gupta, Breand&aacute;nn &Oacute; Nuall&aacute;in, and Willem Bouten. Real-time data assimilation for operational ensemble streamflow forecasting. Journal of Hydrometeorology, 7(3):548–575, 2006a. doi: 10.1175/JHM504.1.
- Jasper A. Vrugt, Breand&aacute;nn &Oacute; Nuall&aacute;in, Bruce A. Robinson, Willem Bouten, Stefan C. Dekker, and Peter M. A. Sloot. Application of parallel computing to stochastic parameter estimation in environmental models. Computers & Geosciences, 32:1139–1155, 2006b. doi:10.1016/j.cageo.2005.10.015.
- Jasper A. Vrugt, Philip H. Stauffer, Th. W&ouml;hling, Bruce A. Robinson, and Velimir V. Vesselinov. Inverse modeling of subsurface flow and transport properties: A review with new developments. Vadose Zone Journal, 7(2):843–864, 2008. doi: 10.2136/vzj2007.0078.
