#!/bin/bash
errors="trainData/errors.txt"
p2rank="p2rank_2.4"
fasta="trainData/fasta"
bindings="trainData/bindings_labeled"
residues="trainData/residues"

main()
{
mkdir -p $fasta
mkdir -p $bindings
mkdir -p $residues

for f in "$@"  
   do  
      name1=${f##*/}
      name=${name1%.*} 
      $p2rank/prank analyze fasta-masked $f -o $fasta/$name
      $p2rank/prank analyze residues $f -o $residues/$name
       
   done  
echo "extracting labeling"
echo ""
python makeLabelings.py $residues $bindings
echo ""
echo "checking data"
python checkData.py $bindings $fasta
}

main $@
