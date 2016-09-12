---
codeRepository: https://github.com/NLeSC/DifferentialEvolution
competence:
- Big Data Analytics
contactPerson: /person/j.spaaks
contributingOrganization:
- /organization/nlesc
contributor:
- /person/j.spaaks
dependency:
- JFreeChart
- D3
discipline:
- eScience Methodology
documentationUrl:
expertise:
- Information Visualization
- Scientific Visualization
- Machine Learning
involvedOrganization:
- /organization/nlesc
license:
- apache-2.0
name: Differential Evolution
endorsedBy:
- /organization/nlesc
owner:
- /organization/nlesc
- /person/j.spaaks
programmingLanguage:
- Java
- JavaScript
startDate: 2013-06-18
status: inactive
supportLevel: specialized
tagLine: Differential Evolution global optimization algorithm, with Metropolis for uncertainty estimation
technologyTag:
- Visualization
- Global Optimization
- Uncertainty Estimation
- Parameter Estimation
- Calibration
usedIn:
user:
- /organization/nlesc
- /person/j.spaaks
website: https://github.com/NLeSC/DifferentialEvolution
---
Java implementation of the Differential Evolution algorithm by Storn & Price.

Additionally uses Metropolis algorithm to estimate the parameter uncertainty.

The software includes some simple
visualizations using JFreeChart (Java) as well as some simple D3.js (JavaScript).

Standard plotting routines include:

1. marginal parameter histograms;
2. matrix of 2-D parameter correlations (scatter);
3. matrix of 2-D parameter correlations (heatmap);
4. parameter evolution scatter;
5. objective score evolution scatter.

Currently, the Differential Evolution algorithm can be used to optimize any one of 6 models:



| index | Java model class name | number of parameters | description    |       
| ----- | --------------------- | -------------------- | ---------------|
| 1     | CubicModel            | 4                    | polynomial |
| 2     | DoubleNormalModel     | 1                    | two Gaussians, benchmark check on the accuracy of the Metropolis part |
| 3     | LinearDynamicModel    | 1                    | draining linear tank |
| 4     | RastriginModel        | 2                    | benchmark model with response surface containing many local minima |
| 5     | RosenbrockModel        | 2                    | benchmark model with response surface containing many local minima, large insensitive areas, and curved ridges |
| 6     | SingleNormalModel | 1                    | simpler version of the DoubleNormalModel |

