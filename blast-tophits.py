# Blast top hits extract
# Blast result should be in table format
# python blast-tophits.py blastoutput.txt output_tophits.txt
import sys

print "# writing your file ...#"

### Give your input file path ###
####################################

file=open(sys.argv[1],'r')
fh=file.read()
file.close()

print "### Reading your input file...."


### Give your output file name ###

file1=open(sys.argv[2],'w')

#####################################################

print "### Writing your input file...."
fh=fh.strip()
id=fh.split('\n')
l=len(id)


x=0
i=0
j=1
p='p'

cl=0

while x<(l-1):
 a=id[i]
 b=id[j]

 id1=a.split('\t')
 id2=b.split('\t')
 ac1=id1[0]
 ac2=id2[0]

 if (ac1==ac2) and (cl==0) :
  p=a
  cl=1

 elif (ac1==ac2) and (cl!=0) :
  pass

 elif (ac1!=ac2):

  file1.write(p)
  file1.write('\n')
  cl=0
  p=b


 i=i+1
 j=j+1
 x=x+1
 if j>(l-1):
  #print p
  file1.write(p)
  file1.write('\n')

print '### your file is ready now...';
