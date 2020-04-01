import json
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

mylist=[]

line = 0
with open('tinyTwitter.json',encoding='utf-8') as f:
    for jsonObj in f:
        i = jsonObj[::-1].find('}')
        if i >= 0:
            if line%size == rank:
                data = json.loads(jsonObj[0:-i])
                mylist.append(data)
                #print('From process [%d]:'%rank)
                #print(data['doc']['entities']['hashtags'])
            line+=1

print('From node [%d]:'%rank)
print(len(mylist))
