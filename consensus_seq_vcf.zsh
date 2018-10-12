# Consensus sequence extraction
# Programs
samtools='/opt/Bio/samtools/1.9/bin/samtools'
bcftools='/opt/Bio/bcftools/1.9/bin/bcftools'
ref='/filer-dg/agruppen/seq_shared/mascher/wheat_psmol_v2_160618/161010_CS_v1.0_pseudomolecules.fasta'

# Extract for specific regions
# Use -H opiton when you have multiple alt allel

$samtools faidx $ref chr7B:5059617-50604264 | $bcftools consensus -s TRI-10703-13 -o TRI-10703-13.fa AE_5310-10703_WGS_samtools.vcf.gz
