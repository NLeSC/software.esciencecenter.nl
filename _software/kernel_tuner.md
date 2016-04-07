---
name: Kernel Tuner
tagLine: A simple CUDA/OpenCL kernel tuner in Python.
codeRepository: https://github.com/benvanwerkhoven/kernel_tuner
website: http://benvanwerkhoven.github.io/kernel_tuner/
documentationUrl: http://benvanwerkhoven.github.io/kernel_tuner/sphinxdoc/html/index.html
logo:
programmingLanguage:
- Python
- CUDA
- OpenCL
license:
- apache-2.0
competence:
- Efficient Computing
discipline:
- eScience Methodology
expertise:
- High Performance Computing
- Accelerated Computing
supportLevel: specialized
contactPerson: http://software.esciencecenter.nl/person/b.vanwerkhoven
owner:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/person/b.vanwerkhoven
contributor:
- http://software.esciencecenter.nl/person/b.vanwerkhoven
user:
involvedOrganization:
usedIn:
startDate: 2016-03-27
status: active
dependency:
dependencyOf:
technologyTag:
- GPU Computing
---
The goal of this project is to provide a - as simple as possible - tool for tuning CUDA and OpenCL kernels.

# Kernel Tuning

A very common problem in GPU programming is that some combination of thread block dimensions and other kernel parameters, like tiling or unrolling factors, results in dramatically better performance than other kernel configurations. The goal of auto-tuning is to automate the process of finding the best performing configuration for a given device.

This kernel tuner aims that you can directly use the tuned kernel without introducing any new dependencies. The tuned kernels can afterwards be used independently of the programming environment, whether that is using C/C++/Java/Fortran or Python doesn't matter.

The kernel_tuner module currently only contains one function which is called tune_kernel to which you pass at least the kernel name, a string containing the kernel code, the problem size, a list of kernel function arguments, and a dictionary of tunable parameters. There are also a lot of optional parameters, for a full list see the full documentation.
