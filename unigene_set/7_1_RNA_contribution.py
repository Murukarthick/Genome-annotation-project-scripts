print "# writing your file ...#"

file=open('CP_unigenes_seq.fa','r')
fh=file.read()
fh=fh.strip()
file.close()
print 'File 1 processed'

file1=open('seq_id_size.txt','w')
print 'File 2 processed'
id=fh.split('>')
l=len(id)

print 'your file is writing..'
#fh
i=0
hd='IDs'+'\t'+'size (bp)'+'\t'+'RNA-seq'+'\t'+'Genome'
fh1=file1.write(hd)
while i<= (l-1):
 se=id[i]
 sid=se.split('\n')
 aid=sid[0]
 
 seq=sid[1:]
 seq=''.join(seq)
 size=len(seq)
 
 A=seq.count('A')
 T=seq.count('T')
 G=seq.count('G')
 C=seq.count('C')
 N=seq.count('N')
 tr=int(A)+int(T)+int(G)+int(C)

 a=seq.count('a')
 t=seq.count('t')
 g=seq.count('g')
 c=seq.count('c')
 n=seq.count('n')
 gn=a+t+g+c
 f=str(aid)+'\t'+ str(size)+'\t'+ str(tr)+"\t"+str(gn)
 #f=a+'\t'+ str(size)+'\t'+str(tr)+'\t'+str(gn)
 fh1=file1.write(f)
 fh1=file1.write('\n')
 i=i+1
print "finished"
