print "# writing your file ...#"

dir='formatted_cds_update.txt'
file=open(dir,'r')
fh=file.read()
file.close()


file1=open('candidate_unigenes_update.txt','w')
fh=fh.strip()
id=fh.split('\n')
l=len(id)

#print l


x=0

i=0
j=1
p=id[0]
cl=0

while x<(l-1):
 a=id[i]
 b=id[j]
 
 id1=a.split('\t')
 id2=b.split('\t')
 ac1=id1[0]
 ac2=id2[0]
 #print ac2
 
 if ac1!= ac2 :
  file1.write(p)
  file1.write('\n')
  cl=0
  p=b
  
 else:
  al1=float(id1[8])
  al2=float(id2[8])
  
  if al1>al2 and al1>cl:
   p=a
   cl=al1
  elif (al1>al2) and (al1<=cl):
   pass
  elif (al2>al1) and (al2>=cl):
   p=b
   cl=al2
  elif (al2>al1) and (al2<=cl):
   pass
  elif al1==al2:
   sl1=float(id1[7])
   sl2=float(id2[7])
   if sl1>sl2:
    p=a
   else:
    p=b
  else:
   p=b
   a=id[i]
 #
 x=x+1
 i=i+1
 if j!=l-1:
  j=j+1
 else :
  file1.write(p)
  file1.write('\n')
print "Done !!!"

