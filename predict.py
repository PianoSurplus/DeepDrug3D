#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Predict the protein binds to ATP or Heme

@author: Limeng Pu
"""

import sys
import argparse

from voxelization import Vox3DBuilder

from keras.models import load_model

def myargs():
    parser = argparse.ArgumentParser()                                              
    parser.add_argument('--protein', required = True, help = 
                        'location of the protein pdb file path')
    parser.add_argument('--aux', required = True, help = 
                        'location of the auxilary input file')
    args = parser.parse_args()
    return args

def argdet():
    if len(sys.argv) < 5:
        print('Check number of input arguement!')
        exit()
    elif len(sys.argv) == 5:
        args = myargs()
        return args
    else:
        print('Cannot recognize the inputs!')
        exit()

def main(protein_path, aux_path):
    voxel = Vox3DBuilder.voxelization(protein_path, aux_path)
    mdl = load_model('deepdrug3d.h5')
    score = mdl.predict(voxel)
    print('The probability of biniding with ATP: ' + str(score[0]))
    print('The probability of biniding with Heme: ' + str(score[1]))
    
if __name__ == "__main__":
    args = argdet()
    main(args.protein, args.aux)
