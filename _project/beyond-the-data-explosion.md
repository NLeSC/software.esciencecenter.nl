---
competence:
- Optimized Data Handling
- Big Data Analytics
- Efficient Computing
contactPerson: /person/r.vannieuwpoort
coordinator: /person/r.vannieuwpoort
dataMagnitude: PB
discipline:
- Physics & Beyond
engineer:
- /person/r.vannieuwpoort
expertise:
- Handling Sensor Data
- High Performance Computing
- Accelerated Computing
- Low Power Computing
endorsedBy:
- /organization/nlesc
infrastructure: LOFAR
involvedOrganization:
- /organization/astron
- /organization/nlesc
logo: /images/project/beyond-the-data-explosion.jpg
name: An eScience infrastructure for huge interferometric datasets
nlescWebsite: https://www.esciencecenter.nl/project/beyond-the-data-explosion
principalInvestigator:
- affiliation:
  - /organization/astron
  name: Dr. Marco de Vos
  website: https://www.linkedin.com/in/devoscm
startDate: 2012-06-12
tagLine: Big Data for the Big Bang
uses:
- /software/eastroviz
---
People are used to the stunning visual images taken by telescopes like
the Hubble or the great telescopes in Hawaii and Chile, but maybe only
have heard of radio astronomy through movies like “Contact”. But radio
telescopes can “see” regions beyond the optical view of a galaxy. They
can uncover the mysteries as to how the early galaxies, in the
millions of years following the Big Bang, began to evolve: Where did
they get their material? What drives their rotation? What has shaped
them?

Since the 1930s astronomers have used radio telescopes to explore the
Universe by detecting radio waves emitted by a wide range of
objects. Our Sun, the nearest star to Earth is a powerful radio
emission source, mainly due to its proximity to our planet, but some
radio sources, which are millions of even billions of light years
away, are truly colossal in terms of their radio output.

Radio telescopes provide alternative views to optical telescopes. They
can detect invisible gas, and can reveal areas of space that may be
obscured with cosmic dust. And unlike optical telescopes, which can be
hampered by cloud or poor weather conditions on Earth, radio
telescopes, working with signals at a longer wavelength, can be used
even in cloudy skies.Radio telescopes can, for example, indirectly
measure the effects of gravity on objects in the Universe. Objects
like Pulsars, the fast spinning remnants of supernova explosions, and
their more exotic cousins, the Black Holes, which are the densest
objects in the Universe, exert huge gravitational effects on nearby
objects.

However, to discover these pulsars you need a high resolution radio
telescope; it would be kilometers across. For a single dish this is
clearly not possible or practical. To get around this limitation in
size radio astronomers use astronomical interferometers; an array of
radio telescopes linked together. In the Netherlands, the LOFAR radio
interferometric array is distributed over an area of about one hundred
kilometers in diameter.

The brute-force search for pulsars takes place over many parameter
combinations, because we do not know the position, distance and period
of the pulsars. Searching for pulsars is a Big Data problem: typical
observations produce hundreds of terabytes, and petabytes of
results. Moreover, the pulsar signal is faint and can be completely
covered by Radio Frequency Interference (RFI), which has to be
analyzed and removed from the signal. In this project we aim to
greatly speed up the search for new pulsars by using Graphics
Processing Units (GPUs) for the complex computations. We are
developing a complete real-time pulsar searching pipeline using a GPU
cluster, and are testing it with two Dutch radio telescopes: LOFAR and
Apertif. LOFAR currently is the largest radio telescope in the world.

Astronomical processing software requires expertise from a variety of
disciplines The results of this work will be extremely important in
developing the hardware and software for what will be the most
powerful radio telescope ever built, the Square Kilometer Array
(SKA). The SKA will be three to four orders of magnitude larger than
LOFAR; requiring exascale computing and networking, and the tools
developed in this project, to run efficiently.

This project explores a new development model for astronomical
processing software where expertise from a variety of disciplines is
combined. This includes for example mathematics for the foundations of
new algorithms, and computer science to optimize for high-performance
platforms. Optimized software and demonstrators will be developed that
can be re-used in a variety of contexts, not just for
radio/mm-astronomy, but also in other areas where large data-streams
are combined.
