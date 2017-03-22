---
competence:
- Efficient Computing
contactPerson: /person/b.vanwerkhoven
coordinator: /person/w.vanhage
discipline:
- Physics & Beyond
engineer:
- /person/b.vanwerkhoven
expertise:
- Accelerated Computing
- High Performance Computing
endorsedBy:
- /organization/nlesc
involvedOrganization:
- /organization/tu-delft
- /organization/nlesc
logo: /images/project/p071-large.jpg
name: Parallelisation of multi point-cloud registration
nlescWebsite: https://www.esciencecenter.nl/project/parallelisation-of-multi-point-cloud-registration
tagLine: Studying subcellular structures and functions
uses:
- /software/kernel_tuner
---

Optical nanoscopy is a powerful technique used in biology to study 
subcellular structures and functions via specifically targeted 
fluorescent labels. Localization microscopy in particular offers a much 
better resolution (~10-50 nm) than conventional microscopy (~250 nm) 
while being relatively undemanding on the experimental setup and the 
subsequent image analysis.

The next revolution in imaging towards 1 nm resolution must realize a 
big increase of the labelling density. Only then can subcellular 
structures be imaged at the molecular level to study the molecular 
machinery of the cell. Relaxing the required labelling density using a 
priori information by data fusion of many identical entities is one of 
the challenges in the field.

This idea, taken from cryo-Electron Microscopy, has already lead to new 
insights in the structure of the Nuclear Pore Complex. However, due to 
the computational complexity this work is just starting. More so, 
algorithms and image processing from the field of electron microscopy 
cannot be translated into light microscopy due to the very different 
image formation. The data here consist out of localizations of 
fluorophores per particle which yields a list of x, y, z positions, a 
point cloud, with associated (anisotropic) measurement uncertainties sx, 
sy and sz, where sx= sy but sx≠ sz due to the imaging modality. These 
measurement uncertainties are different for each point in the cloud, due 
to the fluctuations in the detected photon signal and thus cannot be 
ignored in the registration for optimal performance.

The computational complexity arises (1) from the large number of 
particles ~103-104, (2) the large number of points per particle ~103 and 
(3) from the evaluation of the most suited cost function, the 
Bhattacharyya distance, for registration that takes the measurement 
uncertainty into account.

Typically computation times for a full tree would be months on a 
multi-core server where acquisition times are at most one afternoon. 
This project will be scientifically embedded into an ERC consolidator 
grant (to BR) on optical nanoscopy.

We want to develop an image processing framework that is multi-core and 
GPU capable for fast computation of the whole workflow including multi 
point-cloud registration. In order to do so, and disseminate the 
algorithm and the code, we want to implement the multi-point-cloud 
template-free registration based on our existing and well-used image 
analysis library DIPlib. However, first we need to invest in updating 
the core of the library, now 20 years old, to support multi-threading 
and GPU computing in a flexible, easy to access, and long term 
supportable way.
