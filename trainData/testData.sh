#!/bin/bash
bindings="trainData/bindings_labeled"
residues="trainData/residues"

python checkData.py $bindings $fasta
