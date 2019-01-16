#!/usr/bin/bash
python 'Downloads/generate_Negatives.py' \
--fasta '../player_data/toTrain/data_shuffled.txt' \
--count_negatives 250 \
--out_prefix