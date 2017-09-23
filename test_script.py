File=open("data_set.txt","r")
data=File.read()
File.close()
Split=data.split(',')
z=''
New_data=[]
for i in Split:
     if len(i.split('\n'))==2:
         New_data.append(i.split('\n')[0])
         New_data.append(i.split('\n')[1])
     else:
         New_data.append(i)
modified=[]
feature=[]
label=[]
data_point=[]
counter=0
#print New_data
for i in range(0,len(New_data)):
     counter=counter+1
     if counter%5==0:
          counter=0
          feature.append(data_point)
          data_point=[]
          label.append(New_data[i])
     else:
          data_point.append(New_data[i])

#print feature[:5]
print label
'''-----------------------feature has all the features and Labels has all the data-------------------------------------'''
