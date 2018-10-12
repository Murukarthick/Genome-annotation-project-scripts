# Create upstream, downstream and intergenic boundary from gff file
# This script create user defined upstream and downstream gff features along with intergenic regions
# 
# python make_gene_features.py <genome.gff> <upstream> <downstream> <outputfile>
# Example: python make_gene_features.py IPGA_gene_1.1.gff.txt 1000 200 updated.gff
import sys

# input arguments
up=sys.argv[2]
down=sys.argv[3]

# open gff file
file=open(sys.argv[1],'r')
fh=file.read()
fh=fh.strip()
file.close()
m=fh.split("\n")
l=len(m)

# output all features gff file
file2=open(sys.argv[4],'w')
x=0
y=1
while x<= (l-1) :
 m1=m[x]
 ml=m1.split('\t')
 ml1=ml[2]

 u1000=int(ml[3])-int(up)
 intrn=int(ml[4])+1
 d200=int(ml[4])+int(down)
 
 ml3=int(ml[3]) 
 ml4=ml3+300
 chr=ml[1]
 m2=m[y]
 my=m2.split('\t')
 my1=my[2]
 e=int(my[3])-1
 s=int(ml[4])+1
# Block of conditions carry out the requested process 
 if ml1 == 'gene' :
  file2.write(m1)
  file2.write("\n")
 elif ml1 =='CDS' and my1=='CDS':
  file2.write(m1)
  file2.write("\n")
  c=ml[0]+"\t"+ml[1]+"\t"+"Intron"+"\t"+str(intrn)+"\t"+str(e)+"\t"+"."+"\t"+"-"+"\t"+"."+"\t"+ml[8]
  file2.write(c)
  file2.write("\n")
 elif (ml1 =='mRNA' or ml1 =='exon') and my1=='CDS':
  file2.write(m1)
  file2.write("\n")
  c=ml[0]+"\t"+ml[1]+"\t"+"Upstream"+"\t"+str(u1000)+"\t"+str(e)+"\t"+"."+"\t"+ml[6]+"\t"+"."+"\t"+ml[8]
  file2.write(c)
  file2.write("\n")
 elif ml1=='CDS' and (my1 =='exon' or my1 =='gene') :
  file2.write(m1)
  file2.write("\n")
  c=ml[0]+"\t"+ml[1]+"\t"+"downstream"+"\t"+str(s)+"\t"+str(d200)+"\t"+"."+"\t"+ml[6]+"\t"+"."+"\t"+ml[8]
  file2.write(c)
  file2.write("\n")
 else:
  file2.write(m1)
  file2.write("\n")
 x=x+1
 if y!= l-1:
  y=y+1
print '## finished ##'
