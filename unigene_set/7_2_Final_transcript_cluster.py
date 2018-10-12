print "# writing your file ...#"

file=open('Nr_mode_update.txt','r')
fh=file.read()
fh=fh.strip()
file.close()
print 'File 1 processed'

file1=open('final_updated_cluster.txt','r')
fh1=file1.read()
fh1=fh1.strip()
file1.close()
idx=fh1.split('\n')
l2=len(idx)

print 'File 2 processed'

file3=open('final_cds_update.txt','w')

id=fh.split('\n')
l1=len(id)


print 'your file is writing..'
i=0


while i<= (l1-1):
 whl=id[i]
 fst=whl.split('\t')
 fid=fst[0]
 fm=fst[1]
 
 
 
 k=0
 while k<= (l2-1):
  fidg=idx[k]
  fidgg=fidg.split('\t')
  fids=fidgg[0]
  fmm=fidgg[5]

  if fids == fid and fm==fmm:
   fh3=file3.write(fidg)
   fh3=file3.write('\n')
   
  else:
   pass
   
   
    
  k=k+1 
 i=i+1 
 #fh3=file3.write('\n')
print 'Finished' 
