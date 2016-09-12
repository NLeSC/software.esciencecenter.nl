---
competence:
- Optimized Data Handling
- Big Data Analytics
- Efficient Computing
contactPerson: /person/j.maassen
discipline:
- eScience Methodology
engineer:
- /person/j.maassen
- /person/b.vanwerkhoven
expertise:
- Distributed Computing
- Accelerated Computing
- High Performance Computing
endorsedBy:
- /organization/nlesc
involvedOrganization:
- /organization/nfi
- /organization/nlesc
- /organization/vua
logo: /images/project/a-jungle-computing-approach-to-large-scale-online-forensic-analysis.jpg
name: A Jungle Computing approach to large scale online Forensic Analysis
nlescWebsite: https://www.esciencecenter.nl/project/a-jungle-computing-approach-to-large-scale-online-forensic-analysis
tagLine: Programming tools that simplify application development and deployment
uses:
- /software/kernel_tuner
---
Computing devices (including mobile phones) feature in many of the day-to-day crimes. Computer forensics has emerged as a discipline to assist law enforcement agencies in addressing the increasing use of digital storage devices in criminal acts. Forensic examination of for example mobile phones and personal computers can reveal a wealth of evidence.

Increasingly, high profile criminal cases are benefitting from digital evidence gathered via a computer forensic examination. However, analyzing these large volume data sets of evidence can prove to be a very time consuming process due to the variety of the data and the quantity of potential evidence in a digital environment. For this reason, the Netherlands Forensic Institute (NFI) designed the HANSKEN platform - an important aid in modern police investigation, capable of micro level analysis of digital traces contained in digital devices such as hard disks and mobile phones, and generating macro level forensic views.

# A new computing paradigm

The HANSKEN platform requires a wide variety of computing hardware – all at once. The concurrent use of such variety of hardware has been applied in scientific and industrial applications, spawning a new computing paradigm: Jungle Computing. This variety of computing hardware used in Jungle Computing can take many forms – ranging from a single centralized machine consisting of heterogeneous hardware components (e.g., multicore CPUs, GPUs, and FPGAs) to large-scale distributed systems consisting of combinations of multiple clusters, grids, and cloud systems (each potentially being self-heterogeneous as well).

The complexity of Jungle Computing Systems has generated a need for programming tools that simplify application development and deployment. Above all, such tools must hide as much as possible the idiosyncrasies of the underlying hardware. Moreover, such tools must allow programmers to efficiently integrate multiple compute kernels each potentially implemented using different languages or models (e.g. C, MPI, Python, CUDA), to easily combine and integrate different types of data (potentially from different locations), and to easily deal with dynamic computing needs (software malleability and scalability) and ad-hoc hardware availability (hardware malleability and fault-tolerance). This project focuses on the development of a high quality set of technologies that adhere to all these requirements.

# A Jungle Computing version of the HANSKEN platform

The project aims to apply Jungle Computing to the above described extremely demanding domain of forensic analysis, in particular by extending and adapting the HANSKEN platform. Important requirements underlying the HANSKEN platform include: high-performance, full coverage of all available (possibly distributed) traces, ability to support a wide variety of trace analysis compute kernels, and direct access for various types of police investigators. Although the HANSKEN approach is proven successful (showing 80 times speed improvement over NFI’s current XIRAF system), the expected growth in data volumes, the need for multi-tenancy, and the need for deep analysis of multimedia traces in particular, put further demands on the HANSKEN platform. This proposal aims to realize a Jungle Computing enabled version of HANSKEN that adheres to all these requirements.

# Providing faster insights in forensic casework

Driven by the demands of the forensic analysis domain, expected outcomes of the proposed project include:  
 - High quality releases of core Jungle Computing technologies, based on the Ibis system of VU University.
 - Optimized GPU implementations for a set of performance-critical multimedia analysis kernels.
 - A generic and flexible interface to analysis tools, toolsets and/or libraries for specific forensic analysis domains.

Based on the collaboration between VU University, NFI and the Netherlands eScience Center, it is expected that forensic digital analysis will provide faster insights in forensic casework as well as new links between cases that would otherwise not have been found (for example cross-trace camera identification).
