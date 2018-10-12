# Split per chromosome/scaffolds/contigs 
# python chr_split.py <genome.fasta> 

import sys

# Get input reference fasta file 
file=open(sys.argv[1],'r')
fh=file.read()
fh=fh.strip()
file.close()
print 'Input processed...'

# Split by chromosomes
id=fh.split('>')
id=filter(None,id)
l=len(id)

# Output each chromosome
print 'your file is writing..'
i=0
while i<= (l-1):
 seq=id[i]
 sid=seq.split('\n')
 fid=sid[0]
 file2=open(fid+'.fasta','w')
 fn='>'
 fh1=file2.write(fn)  
 fh1=file2.write(seq)
 file2.close()
 i=i+1
print 'finished'

