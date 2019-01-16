#!/usr/bin/env python

import os 
import sys
import random
import argparse
import numpy as np 

################################################################################
# generate_Negatives.py
#
# Input FASTA file, output FASTA file with scrambled negative cases
#
################################################################################

def toy_example(fasta, count_negatives, out_prefix):
    # input fasta 
    fasta_in = open(fasta,'r')

    # output txt file
    txt_out = open('%s.txt' % out_prefix,'w')

    sequences = []
    for line in fasta_in:
        _, format_string, reverse_string = line.split('\t')
        sequences.append(format_string)
        cols = format_string + '\t' + str(1) + '\n'
        txt_out.writelines(cols)

    fasta_in.close()

    for ii in range(count_negatives):
        newline = random.choice(sequences)
        newseq = [newline[jj:jj+2] for jj in np.arange(0,len(newline),2)]
        scrambled = ''.join(random.sample(newseq,len(newseq)))
        cols = scrambled + '\t' + str(0) + '\n'
        txt_out.writelines(cols)

    txt_out.close()

################################################################################
# Args
################################################################################

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--fasta',
      type=str,
      help='Input fasta.'
  )
  parser.add_argument(
      '--count_negatives',
      type=int,
      default=5000,
      help="Number of negative cases to generate."
  )
  parser.add_argument(
    '--out_prefix',
    type=str,
    default='out',
    help="Name for file."
  )

  FLAGS, _ = parser.parse_known_args()
  toy_example(FLAGS.fasta, FLAGS.count_negatives, FLAGS.out_prefix)















