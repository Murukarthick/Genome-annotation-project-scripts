# Report sequence sizes in a fasta file
# python seqSize_finder.py <genome.fasta> > result-size.txt
import sys

# Read and split input fasta file
file=open(sys.argv[1],'r')
fh=file.read()
fh=fh.strip()
file.close()
id=fh.split('>')
l=len(id)

# Loop to count all bases
i=0
hd='IDs'+'\t'+'Total size (bp)'+'\t'+'As'+'\t'+'Ts'+'\t'+'Gs'+'\t'+'Cs'+'\t'+'Ns'
print hd
while i<= (l-1):
 se=id[i]
 sid=se.split('\n')
 a=sid[0]
 seq=sid[1:]
 seq=''.join(seq)
 size=len(seq)
 if size != 0 :
  A=seq.count('A')
  T=seq.count('T')
  G=seq.count('G')
  C=seq.count('C')
  N=seq.count('N')
  f=a+'\t'+ str(size)+'\t'+str(A)+'\t'+str(T)+'\t'+str(G)+'\t'+str(C)+'\t'+str(N)
  print f
  
 i=i+1
print "---------"

