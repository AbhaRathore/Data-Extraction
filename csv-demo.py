import csv
interviewFile = open('interview_scent.csv')
interviewReader = csv.reader(interviewFile)
myFile_prediction = open('interview_scent_prediction.csv', 'w')
myFile_count = open('interview_scent_count.csv', 'w')

count=0
Prediction= [ ]
distinct_count={}
next (interviewReader)
for row in interviewReader:
     if row[4]!='None':
        count += 1
     if row[4] not in Prediction:
        Prediction.append(row[4])
     if row[4] not in distinct_count:
        distinct_count[row[4]]=1
     else:
        distinct_count[row[4]] +=1
unique_count= len(Prediction)

print ("\nTotal No. of Rows: %s\n " % (count))
print ("Distinct values of Prediction are:\n%s\n"%(Prediction))
print ("Count of distinct prediction values is:\n%s\n"% (distinct_count))

total= ['Total No. of Rows without None Prediction', count]
unique= ['Distinct values in Prediction', unique_count]
wrp = csv.writer(myFile_prediction, quoting=csv.QUOTE_ALL)
wrp.writerow(total)
wrp.writerow(unique)

wrc = csv.writer(myFile_count, quoting=csv.QUOTE_ALL)
wrc.writerow(['Predictions', 'Total_Count'])
for k,v in distinct_count.items():
      wrc.writerow([k,v])