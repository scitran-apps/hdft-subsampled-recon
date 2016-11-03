#! /usr/bin/env python
# Parse the config json and return a string that can be passed to the MSE.


# Parse a config file 
def parse_config(json_file, output_config_file, input_dir, output_dir, nifti_dir, bvec_dir, bval_dir, subsampling_vec_dir):
    import os
    import json
    import glob
    import shutil

    # Read the config json file
    with open(json_file, 'r') as jsonfile:
        config = json.load(jsonfile)

    # Rename the config key to params
    config['params'] = config.pop('config')

    # Set config to include the input files
    config['bval_file'] = glob.glob(os.path.join(bval_dir, '*bval*'))[0]
    config['bvec_file'] = glob.glob(os.path.join(bvec_dir, '*bvec*'))[0]
    config['dwi_file'] = glob.glob(os.path.join(nifti_dir, '*.nii*'))[0]
    config['subsampling_vec'] = glob.glob(os.path.join(subsampling_vec_dir, '*.csv*'))[0]

    # Set the sh_filename
    config['sh_filename'] = os.path.join(output_dir, config['params']['sh_filename'])

    # Print out the arguments for the MSE
    input_arguments = [config['dwi_file'],
                        config['subsampling_vec'],
                        config['bval_file'],
                        config['bvec_file'],
                        str(config['params']['spherical_harmonics_order']),
                        str(config['params']['mean_diffusion_length']),
                        config['sh_filename']]
    print " ".join(input_arguments)


    # Write out the modified configuration
    with open(output_config_file, 'w') as config_json:
        json.dump(config, config_json)

if __name__ == '__main__':

    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--json_file', type=str, dest="json_file", default='/flywheel/v0/config.json', help='Full path to the input json config file.')
    ap.add_argument('--output_config_file', type=str, dest="output_config_file", default='/flywheel/v0/output/subsampled_recon_params.json', help='Full path to the output file.')
    ap.add_argument('--input_dir', type=str, dest="input_dir", default='/flywheel/v0/input', help='Full path to the input directory.')
    ap.add_argument('--output_dir', type=str, dest="output_dir", default='/flywheel/v0/output', help='Full path to the output directory.')
    ap.add_argument('--bvec_dir', type=str, dest="bvec_dir", default='/flywheel/v0/input/bvecs_file', help='Full path to the bvec directory.')
    ap.add_argument('--bval_dir', type=str, dest="bval_dir", default='/flywheel/v0/input/bvals_file', help='Full path to the bval directory.')
    ap.add_argument('--nifti_dir', type=str, dest="nifti_dir", default='/flywheel/v0/input/dwi_file', help='Full path to the nifti directory.')
    ap.add_argument('--subsampling_vec_dir', type=str, dest="subsampling_vec_dir", default='/flywheel/v0/input/subsampling_vec', help='Full path to the subsampling_vec directory.')
    args = ap.parse_args()

    parse_config(args.json_file, args.output_config_file, args.input_dir, args.output_dir, args.nifti_dir, args.bvec_dir, args.bval_dir, args.subsampling_vec_dir)
