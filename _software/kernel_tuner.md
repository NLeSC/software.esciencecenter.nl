---
codeRepository: https://github.com/benvanwerkhoven/kernel_tuner
competence:
- Efficient Computing
contactPerson: http://software.esciencecenter.nl/person/b.vanwerkhoven
contributor:
- http://software.esciencecenter.nl/person/b.vanwerkhoven
discipline:
- eScience Methodology
documentationUrl: http://benvanwerkhoven.github.io/kernel_tuner/sphinxdoc/html/index.html
expertise:
- High Performance Computing
- Accelerated Computing
license:
- apache-2.0
name: Kernel Tuner
owner:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/person/b.vanwerkhoven
programmingLanguage:
- Python
- CUDA
- OpenCL
startDate: 2016-03-27
status: active
supportLevel: specialized
tagLine: A simple CUDA/OpenCL kernel tuner in Python.
technologyTag:
- GPU Computing
user:
- http://software.esciencecenter.nl/person/b.vanwerkhoven
website: http://benvanwerkhoven.github.io/kernel_tuner/
---
The goal of this project is to provide a - as simple as possible - tool for tuning CUDA and OpenCL kernels.

# Kernel Tuning

A very common problem in GPU programming is that some combination of thread block dimensions and other kernel parameters, like tiling or unrolling factors, results in dramatically better performance than other kernel configurations. The goal of auto-tuning is to automate the process of finding the best performing configuration for a given device.

This kernel tuner aims that you can directly use the tuned kernel without introducing any new dependencies. The tuned kernels can afterwards be used independently of the programming environment, whether that is using C/C++/Java/Fortran or Python doesn't matter.

The kernel_tuner module currently only contains one function which is called tune_kernel to which you pass at least the kernel name, a string containing the kernel code, the problem size, a list of kernel function arguments, and a dictionary of tunable parameters. There are also a lot of optional parameters, for a full list see the full documentation.