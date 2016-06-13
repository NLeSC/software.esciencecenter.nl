---
codeRepository: https://github.com/NLeSC/eEcology-script-wrapper
competence:
- Optimized Data Handling
contactPerson: http://software.esciencecenter.nl/person/s.verhoeven
contributor:
- http://software.esciencecenter.nl/person/s.verhoeven
discipline:
- Environment & Sustainability
expertise:
- Handling Sensor Data
- Information Retrieval
- Scientific Visualization
- Databases
involvedOrganization:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/uva
- http://software.esciencecenter.nl/organization/surfsara
name: eEcology Tracker calendar
inGroup:
- NLeSC
license:
- apache-2.0
owner:
- http://software.esciencecenter.nl/organization/nlesc
- http://software.esciencecenter.nl/organization/uva
- http://software.esciencecenter.nl/person/s.verhoeven
programmingLanguage:
- Python
startDate: 2013-02-15
status: active
supportLevel: specialized
tagLine: Calendar overview with daily statistics of GPS-tracker
technologyTag:
- GIS
- Website
usedIn:
- http://software.esciencecenter.nl/project/eecology
user:
- http://software.esciencecenter.nl/organization/uva
website: https://public.e-ecology.sara.nl/sw/tool/calendar/
---
The tracker calendar shows daily statistics or metrics of tracker as a calendar heatmap. It can be used to find days when something interesting happened or to find repeating patterns.

![Screenshot of tracker calendar](/images/eecology-tracker-calendar.png "Screenshot")

The following metrics of a tracker are calculated for each day:

* Nr. of GPS measurements
* Nr. of accelerometer measurements
* 2D distance travelled (km): Distance of line which consists of GPS measurements from midnight till midnight, altitude is ignored.
* Maximum altitude (m): Highest absolute altitude
* Average altitude (m): Average absolute altitude
* Minimum altitude (m): Lowest absolute altitude
* Maximum temperature (°C)
* Average temperature (°C)
* Minimum temperature (°C)
* Minimum voltage battery (V): Lowest battery voltage
* Maximum interval between GPS measurements (hh:mm:ss)
* Minimum interval between GPS measurements (hh:mm:ss)

The color range can be clipped to find outliers.
