print "# writing your file ...#"

### Give your input file path ###

dir='Pg_genome_hits.txt'

####################################

file=open(dir,'r')
fh=file.read()
fh=fh.strip()
file.close()

print "### Reading your input file...."

file2=open('issue_hits.txt','r')
fh1=file2.read()
fh1=fh1.strip()
file2.close()
idm=fh1.split('\n')

### Give your output file name ###

file1=open('formatted_genome_hits.txt','w')



#####################################################

print "### Writing your input file...."
fh=fh.strip()
id=fh.split('\n')
l=len(id)

x=0
i=0



while x<(l-1):
 a=id[i]
 id1=a.split('\t')
 qid1=id1[0]
 subj1=id1[1]
 m=qid1+'\t'+subj1
 if m not in idm:
  file1.write(a)
  file1.write('\n')
 else:
  pass

 i=i+1
 x=x+1

print "Finished"
