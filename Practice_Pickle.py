import pickle

list1=[]
list2=[]


with open('C:/practice.txt','r') as f1:
    list1 = f1.readlines()
    f1.close()
with open('c:/data.pickledata','wb') as picklefile:
    pickle.dump(list1,picklefile)
    picklefile.close()

with open('c:/data.pickledata','rb') as picklefile:
    list2 = pickle.load(picklefile)
print(list2)
