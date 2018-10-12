# Extract specific chromosomes/scaffolds/contigs
# python seqSize_finder.py <genome.fasta> <selected_ids.txt> <ouput_Selected_seq.fasta>
import sys

# Read and split input fasta file
file=open(sys.argv[1],'r')
fh=file.read()
fh=fh.strip()
file.close()

# Read input ids
file1=open(sys.argv[2],'r')
fh1=file1.read()
fh1=fh1.replace('\r','')
file1.close()
idm=fh1.splitlines()

# write output
file3=open(sys.argv[3],'w')

id=fh.split('>')
id=filter(None,id)
l=len(id)


i=0
while i<= (l-1):
 seq=id[i]
 sid=seq.split('\n')
 fid=sid[0]
 fn='>'
 
 if fid in idm :
  fh1=file3.write(fn)  
  fh1=file3.write(seq)
  
 else:
  pass
 i=i+1

### ----- ####
