# Extract gene/mRNA/up/down stream extract from a gff file
# python gffFeatures_to_seq.py <genome.gff> <gff file> <feature> <outputfile>
# Example: python gffFeatures_to_seq.py genome.fa annot.gff gene geneseq.fasta
import sys

Elmn=sys.argv[3]

# Read your input file
file=open(sys.argv[1],'r')
fh=file.read()
fh=fh.strip()
file.close()
print 'File 1 processed'

# Read your gff file
file1=open(sys.argv[2],'r')
fh1=file1.read()
fh1=fh1.strip()
file1.close()

# Process input files
idx=fh1.split('\n') 
idx=filter(None, idx)
l2=len(idx)

# write output file
file3=open(sys.argv[4],'w')
print 'File 2 processed'

id=fh.split('>')
id=filter(None, id)
l=len(id)

i=0
while i<=(l-1):
 whl=id[i]
 sid=whl.split('\n')
 fid=sid[0]
 seq=''.join(sid[1:])
 
 k=0
 while k<=(l2-1):
  fidg=idx[k]
  fidgg=fidg.split('\t')
  if fidgg[2] == Elmn :
   id2=fidgg[0]
   gid=fidgg[3]
   gid=gid.strip()
   s=int(fidgg[3])
   e=int(fidgg[4])
   seqID=fidgg[8]+"|"+Elmn
  
   if id2 == fid:
    s=s-1
    e=e
    se=seq[s:e]
    x=0
    y=70
    gid='>'+ seqID
    file3.write(gid)
    file3.write('\n')
    while x<=len(se):
     fseq=se[x:y] 
     file3.write(fseq)
     file3.write('\n')
     x=x+70
     y=y+70  
   else:
    pass
  k=k+1
 i=i+1

print 'Finished !!!'

