with open('test.log') as f:
    lines = f.readlines()
    
giveNumber = int(input("Enter ur number: "))


my_values = []

dist_li=[]
for i in lines:
    k = i.split(" ")  
    dis = k[3]
    u = dis.replace("-", " ")
    if u == "list": 
        continue
    dist_li.append(float(u))
    
print(f'number of elemetns in list is {len(dist_li)}')
c=[i for i in dist_li if float(i)<=giveNumber]
total_percent=(len(c)/len(dist_li))*100
print(c)
print(f'Found: {len(c)} of {len(dist_li)}' )
print(f'Total percentage: {total_percent}')
if len(c) == 0:
    print( f"The minimum distance is: {min(dist_li)} ")


