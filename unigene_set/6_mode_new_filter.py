import nltk
print "# writing your file ...#"

### Give your input file path ###

dir='final_updated_cluster.txt'

####################################

file=open(dir,'r')
fh=file.read()
fh=fh.strip()
file.close()

print "### Reading your input file...."


### Give your output file name ###

file1=open('Nr_mode_update.txt','w')

tmp=open('tmp.txt','w')

#####################################################

print "### Writing your input file...."
fh=fh.strip()
id=fh.split('\n')
l=len(id)

x=0
i=0
j=1




while x<(l-1):
 a=id[i]
 b=id[j]
 
 id1=a.split('\t')
 id2=b.split('\t')
 qid1=str(id1[0])
 qid2=str(id2[0])
 
 gr1=id1[5]
 
 
 if qid1==qid2:
  tmp.write(gr1)
  tmp.write("\n")
  
 else:
  tmp.write(gr1)
  tmp.close()
  tmfile=open('tmp.txt','r')
  tmpf=tmfile.read()
  tmpf=tmpf.strip()
  tid=tmpf.split('\n')
  print tid
  tid=map(int, tid)
  
  fd=nltk.FreqDist(tid)
  m=fd.max()
  print str(tid)+"selected"+str(m) 
  p=str(qid1)+"\t"+str(m)
  file1.write(p)
  file1.write('\n')
  tmp=open('tmp.txt','w+')
  
 
 i=i+1
 j=j+1
 x=x+1
if j==l:
 a=id[l-1]
 gr=a.split('\t')
 tmp.write(gr[5])
tmp.close()
tmfile=open('tmp.txt','r')
tmpf=tmfile.read()
tmpf=tmpf.strip()

if tmpf!='':
 tid=tmpf.split('\n')
 fd=nltk.FreqDist(tid)
 m=fd.max()
   
 p=str(qid1)+"\t"+str(m)
 file1.write(p)
 file1.write('\n')
 tmp=open('tmp.txt','w+')
 tmp.close()
else:
 p=str(qid2)+"\t"+str(m)
 file1.write(p)


print "Finished!!!!!"

