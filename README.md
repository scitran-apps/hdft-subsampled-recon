[![Docker Pulls](https://img.shields.io/docker/pulls/scitran/hdft-subsampled-recon.svg)](https://hub.docker.com/r/scitran/hdft-subsampled-recon/)
[![Docker Stars](https://img.shields.io/docker/stars/scitran/hdft-subsampled-recon.svg)](https://hub.docker.com/r/scitran/hdft-subsampled-recon/)

## hdft-subsampled-recon

Build context for a [Flywheel compatible Gear](https://github.com/flywheel-io/gears/tree/master/spec) for the HDFT Subsampled Recon algorithm from Schneider Lab, University of Pittsburgh.

This **sample** code computes a transformation of multi-shell diffusion weighted data to a set of Spherical Harmonic coefficients. Outputs 4D Spherical Harmonic coefficient data. This is a first step in the Schneider Lab HDFT diffusion reconstruction process.

### Inputs

* `dwi_filename`: input filename of 4D DWI data
* `subsampling_vec`: input vector to select volumes from `dwi_filename` (can be a text file or CSV)
* `bvals_filename`: input file of Nx1 b values
* `bvecs_filename`: input file of Nx3 b vectors

### Parameters
* `spherical_harmonics_order`: The maximum order of spherical harmonics. Defaulted to `8`.
* `mean_diffusion_length`: The mean diffusion length for reconstruction of GQI matrix. Defaulted to `1.2`.

### Output
* `sh_filename`: 4D Spherical Harmonic coefficient data.

### Reference
Pathak, S. K., Fissell, C., Krishnaswamy, D., Aggarwal, S., Hachey, R., Schneider, W. (2015).
Diffusion reconstruction by combining spherical harmonics and generalized q-sampling imaging.
ISMRM, Toronto, Canada.

### License
All code is copyright University of Pittsburgh unless alternate authorship noted.
This code is not for public distribution, please contact Schneider Lab re distribution.
http://www.lrdc.pitt.edu/schneiderlab/
