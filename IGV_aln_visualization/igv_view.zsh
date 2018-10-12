#!/bin/zsh

samtools='/opt/Bio/samtools/1.9/bin/samtools'

ref=$1
shift
base=$1
out=$base:t:r.cram

$samtools view -Ch -T $ref -@ 20 -o $out $base -L chr3h_parts.bed && $samtools index -c -@ 20 $out



