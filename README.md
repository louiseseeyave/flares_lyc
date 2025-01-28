# Ionising properties of galaxies in the First Light and Reionisation Epoch Simulations (FLARES)
This repository contains some of the FLARES data published in the paper: https://arxiv.org/abs/2305.18174.

Feel free to drop me an email at l.seeyave@sussex.ac.uk if the data you would like isn't here.

### Fig. 7
The file `flares_xiion_lum.txt` contains the 16th, 50th, and 84th percentile values of the ionising photon production efficiency (xiion) as a function of the dust-attenuated far-UV luminosity for $z=5-10$.

### Fig. 8
The files `flares_xiion_z_lum-2*` contain the 16th, 50th, and 84th percentile values of the ionising photon production efficiency (xiion) as a function of redshift, in bins of dust-attenuated far-UV luminosity:
* 28 < log<sub>10</sub>(L<sub>FUV,dust</sub>/erg s<sup>-1</sup>Hz<sup>-1</sup>) < 28.5, which corresponds to -19.7 < M<sub>FUV</sub> < -18.4
* 28.5 < log<sub>10</sub>(L<sub>FUV,dust</sub>/erg s<sup>-1</sup>Hz<sup>-1</sup>) < 29, which corresponds to -20.9 < M<sub>FUV</sub> < -19.7
* 29 < log<sub>10</sub>(L<sub>FUV,dust</sub>/erg s<sup>-1</sup>Hz<sup>-1</sup>) < 29.5, which corresponds to -22.2 < M<sub>FUV</sub> < -20.9
* log<sub>10</sub>(L<sub>FUV,dust</sub>/erg s<sup>-1</sup>Hz<sup>-1</sup>) > 29.5, which corresponds to M<sub>FUV</sub> < -22.2

The file `flares_xiion_z_lum-all.txt` contains the 2nd, 16th, 50th, 84th and 98th percentile values of the ionising photon production efficiency (xiion) as a function of redshift for all galaxies in FLARES.

### Fig. 9
The files `flares_xiion_beta_*` contain the 16th, 50th, and 84th percentile values of the ionising photon production efficiency (xiion) as a function of the UV-continuum slope $\beta$ for $z=5$ and 6:
* `beta_stellar` - pure stellar (first column of Figure 9)
* `beta_nebular` - stellar + nebular (second column of Figure 9)
* `beta_dust` - stellar + nebular + dust (third column of Figure 9)

### Fig. A1
The file `flares_xiion_mstar.txt` contains the 16th, 50th, and 84th percentile values of the ionising photon production efficiency (xiion) as a function of stellar mass for $z=5-10$.
