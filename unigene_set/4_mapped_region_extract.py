print "# writing your file ...#"

### Give your input file path ###

dir='new_top_hits_1e_5.txt'

####################################

file=open(dir,'r')
fh=file.read()
fh=fh.strip()
file.close()

print "### Reading your input file...."


### Give your output file name ###

file1=open('T_mapped_regions.txt','w')

tmp=open('tmp.txt','w')

#####################################################

print "### Writing your input file...."
fh=fh.strip()
id=fh.split('\n')
l=len(id)

x=0
i=0
j=1
exons=1



while x<(l-1):
 a=id[i]
 b=id[j]
 
 id1=a.split('\t')
 id2=b.split('\t')
 qid1=id1[0]
 qid2=id2[0]

 subj1=id1[1]
 subj2=id2[1]
 gr1=id1[8]
 gr2=id1[9]
 
 if qid1==qid2 and subj1==subj2:
  tmp.write(gr1)
  tmp.write("\n")
  tmp.write(gr2)
  tmp.write("\n")
  exons=exons+1

 else:
  
  tmp.write(gr1)
  tmp.write("\n")
  tmp.write(gr2)
  tmp.close()
  tmfile=open('tmp.txt','r')
  tmpf=tmfile.read()
  tmpf=tmpf.strip()
  tid=tmpf.split('\n')
  tid=map(int, tid)
  
  tlen=sorted(tid,key=int)
  
  lnth=len(tlen)
  p=str(qid1)+"\t"+str(subj1)+"\t"+str(tlen[0])+"\t"+str(tlen[lnth-1])+"\t"+ str(exons)
  file1.write(p)
  file1.write('\n')
  tmp=open('tmp.txt','w+')
  exons=1
  
 
 
 i=i+1
 j=j+1
 x=x+1

tmp.close()
tmfile=open('tmp.txt','r')
tmpf=tmfile.read()
tmpf=tmpf.strip()

if tmpf!='':
 tid=tmpf.split('\n')
 tid=map(int, tid)
 tlen=sorted(tid,key=int)
  
 lnth=len(tlen)
 p=str(qid1)+"\t"+str(subj1)+"\t"+str(tlen[0])+"\t"+str(tlen[lnth-1])+"\t"+ str(exons)
 file1.write(p)
 file1.write('\n')
 tmp=open('tmp.txt','w+')
 tmp.close()
else:
 if gr1>gr2:
  file1.write(str(qid2)+"\t"+str(subj2)+"\t"+str(gr1)+"\t"+str(gr2)+"\t"+ str(exons))
 else:
  file1.write(str(qid2)+"\t"+str(subj2)+"\t"+str(gr2)+"\t"+str(gr1)+"\t"+ str(exons))


print "Finished!!!!!"


















