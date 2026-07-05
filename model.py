NAME=[]
TAMIL=[]
ENGLISH=[]
MATHS=[]
SCIENCE=[]
SOCIAL=[]
SUBJECT=[TAMIL,ENGLISH,MATHS,SCIENCE,SOCIAL]
lang=["TAMIL","ENGLISH","MATHS","SCIENCE","SOCIAL"]
for i in range(5):
    x=input("ENTER YOUR NAME:")
    NAME.append(x)
    for k in range(5):
       y=int(input("ENTER YOUR %s MARK:" %lang[k]))  
       for j in range(5):
          if lang[j]==lang[k]:
              SUBJECT[j].append(y)
maxy=[]
index=[]
for l in range(5):
    maxy.append(max(SUBJECT[l]))
    index.append(SUBJECT[l].index(max(SUBJECT[l])))
sub_name=input("ENTER THE SUBJECT YOU WANT TO CHECK:")
sub_name=sub_name.upper()
for m in range(5):
    if lang[m]==sub_name:
       print("THE HIGHEST MARK IN ",sub_name," IS ",maxy[m],"BY",NAME[index[m]])
            
            
