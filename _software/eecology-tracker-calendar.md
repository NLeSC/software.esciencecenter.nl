---
codeRepository: https://github.com/NLeSC/eEcology-script-wrapper
competence:
- Optimized Data Handling
contactPerson: /person/s.verhoeven
contributingOrganization:
- /organization/nlesc
contributor:
- /person/s.verhoeven
discipline:
- Environment & Sustainability
expertise:
- Handling Sensor Data
- Information Retrieval
- Scientific Visualization
- Databases
involvedOrganization:
- /organization/nlesc
- /organization/uva
- /organization/surfsara
name: eEcology Tracker calendar
endorsedBy:
- /organization/nlesc
license:
- apache-2.0
owner:
- /organization/nlesc
- /organization/uva
- /person/s.verhoeven
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
- /project/eecology
user:
- /organization/uva
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
