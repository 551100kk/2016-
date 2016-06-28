arr=[]
class staff:
    def __init__(self,id,firstname,lastname,jobid,age):
        self.id=id
        self.firstname=firstname
        self.lastname=lastname
        self.jobid=jobid
        self.age=age
    def pt(self):
        print(self.id+" "+self.firstname+" "+self.lastname+" "+self.jobid+" "+self.age)
    def sort_by_jobid(self):
        return self.jobid
    def sort_by_id(self):
        return self.id
    def sort_by_id_jobid(self):
        return (self.id,self.jobid)
def que_add(id,firstname,lastname,jobid,age):
    newstaff=staff(id,firstname,lastname,jobid,age)
    arr.append(newstaff)
def que_id(id):
    ans=[]
    for i in range(len(arr)):
        if arr[i].id==id:
            ans.append(arr[i])
    ans.sort(key=staff.sort_by_jobid)
    for i in range(len(ans)):
        ans[i].pt()
def que_jobid(jobid):
    ans=[]
    for i in range(len(arr)):
        if arr[i].jobid==jobid:
            ans.append(arr[i])
    ans.sort(key=staff.sort_by_id)
    for i in range(len(ans)):
        ans[i].pt()
def que_name(firstname,lastname):
    ans=[]
    for i in range(len(arr)):
        if arr[i].firstname==firstname and arr[i].lastname==lastname:
            ans.append(arr[i])
    ans.sort(key=staff.sort_by_jobid)
    for i in range(len(ans)):
        ans[i].pt()
def que_print():
	arr.sort(key=staff.sort_by_id_jobid)
	for i in range(len(arr)):
	    arr[i].pt()
num = int(input())
while num:
    num-=1
    query = input().split(' ')
    if query[0]=="ADD":
        que_add(query[1],query[2],query[3],query[4],query[5])
        continue
    if query[0]=="ID":
        que_id(query[1])
    if query[0]=="JOBID":
        que_jobid(query[1])
    if query[0]=="NAME":
        que_name(query[1],query[2])
    if query[0]=="PRINT":
        que_print()
    print() 
        
