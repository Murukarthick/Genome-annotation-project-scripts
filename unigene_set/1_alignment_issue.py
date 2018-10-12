print "# writing your file ...#"

### Give your input file path ###

dir='Pg_genome_hits.txt'

####################################

file=open(dir,'r')
fh=file.read()
fh=fh.strip()
file.close()

print "### Reading your input file...."


### Give your output file name ###

file1=open('issue_hits.txt','w')



#####################################################

print "### Writing your input file...."
fh=fh.strip()
id=fh.split('\n')
l=len(id)

x=0
i=0
j=1
k=2
exons=1

cl=0


while x<(l-1):
 a=id[i]
 b=id[j]
 c=id[k]
 
 id1=a.split('\t')
 id2=b.split('\t')
 id3=c.split('\t')

 qid1=id1[0]
 qid2=id2[0]
 qid3=id3[0]
 
 subj1=id1[1]
 subj2=id2[1]
 subj3=id3[1]

 idn1=float(id1[2])
 idn2=float(id2[2])
 idn3=float(id3[2])
 
 if (qid1==qid2) and (subj1!=subj2) and (idn1<=idn2) and (cl==0) and subj2==subj3 and qid2==qid3 and idn3>=99:
  file1.write(qid1)
  file1.write('\t')
  file1.write(subj1)
  file1.write('\n')
  cl=cl+1 
 elif (qid1==qid2) and (subj1==subj2) and (cl==0):
  cl=cl+1
 elif (qid1==qid2) and (subj1!=subj2) and (idn1!=idn2)and (cl==0):
  cl=cl+1
 elif (qid1!=qid2):
  cl=0
  a=b
 else:
  pass

 i=i+1
 j=j+1
 x=x+1
 k=k+1
print "Finished"
