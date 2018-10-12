print "# writing your file ...#"

### Give your input file path ###

dir='formatted_genome_hits.txt'

####################################

file=open(dir,'r')
fh=file.read()
fh=fh.strip()
file.close()

print "### Reading your input file...."


### Give your output file name ###

file1=open('new_top_hits_1e_5.txt','w')



#####################################################

print "### Writing your input file...."
fh=fh.strip()
id=fh.split('\n')
l=len(id)

x=0
i=0
j=1
exons=1

cl=0


while x<(l-1):
 a=id[i]
 b=id[j]
 
 id1=a.split('\t')
 id2=b.split('\t')
 qid1=id1[0]
 qid2=id2[0]
 
 subj1=id1[1]
 subj2=id2[1]
 
 itn1=float(id1[2])
 itn2=float(id2[2])
 scr2=float(id1[11])
 scr2=float(id2[11])
 
 if (qid1==qid2) and (subj1==subj2) and (cl==0):
  file1.write(a)
  file1.write('\n')
 elif (qid1==qid2) and (subj1!=subj2) and (cl==0):
  file1.write(a)
  file1.write('\n')
  cl=cl+1
  
 elif (qid1!=qid2) and (subj1==subj2) and (cl==0):
  file1.write(a)
  file1.write('\n')
  
 elif (qid1!=qid2) :
  #file1.write(b)
  #file1.write('\n')
  cl=0

 i=i+1
 j=j+1
 x=x+1
file1.write(b)
print "Finished"

 























