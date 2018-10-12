# Consensus sequence extraction
# Programs
# Provide absolute path
samtools='/source/samtools/1.9/bin/samtools'
bcftools='/source/bcftools/1.9/bin/bcftools'
ref='pseudomolecules.fasta'

# Extract consensus sequence for specific regions
# Use -H opiton when you have multiple alt allel

$samtools faidx $ref chr7B:5059617-50604264 | $bcftools consensus -s TRI-10703-13 -o TRI-10703-13.fa WGS_samtools.vcf.gz
