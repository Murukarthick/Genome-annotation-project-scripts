print "# writing your file ...#"

file=open('final_cds_update.txt','r')
fh=file.read()
fh=fh.replace('\r','')
file.close()
print 'File 1 processed'

file1=open('seq_id_size.txt','r')
fh1=file1.read()
fh1=fh1.replace('\r','')
file1.close()
idx=fh1.split('\n')

l2=len(idx)

idm=fh1.split('\n')
#idm=idm[0].split('\t')
idm=str(idm)
idm = idm.replace ('\n', '')
#print idm
print 'File 2 processed'

file3=open('formatted_cds_update.txt','w')

id=fh.split('\n')
l1=len(id)


print 'your file is writing..'
i=0

#print id[0]
while i<= (l1-1):
 whl=id[i]
 fst=whl.split('\t')
 fid=fst[1]
 	 
 fh3=file3.write(whl)
 fh3=file3.write('\t')
 
 
 
 
 if fid in idm:
  k=0
  while k<= (l2-1):
   fidg=idx[k]
   fidgg=fidg.split('\t')
   fids=fidgg[0]
   #print fids
   
   if fids == fid:
    fh3=file3.write(fidg)
    fh3=file3.write('\t')
    print 'printed'
   else:
    pass
   #fh3=file3.write(fidg)
   
    
   k=k+1 
 i=i+1 
 fh3=file3.write('\n')
print 'Finished' 
 

