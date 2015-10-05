# In[1]:

import random


# In[4]:

A='A' #aleatorio
B='B' #sensing
def cea():
 phenotype = random.randint(1,3) 
 typeA = [A,phenotype,0]
 typeB = [B,phenotype,0]
 typelist = [typeA,typeB]
 return random.choice(typelist)


# In[5]:

n = 300
culture = [[[0 for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]

for k in xrange(n):
 for j in xrange(n):
  for i in xrange(n):
   culture[i][j][k] = cea()         


# In[6]:

def countcell():
 cellcount = []
 numA = 0
 numB = 0
 nump1 = 0
 nump2 = 0   
 for k in xrange(n):
  for j in xrange(n):
   for i in xrange(n):
    if culture[i][j][k][0] == 'A':
     numA +=1
    if culture[i][j][k][0] == 'B':
     numB +=1
    if culture[i][j][k][1] == 1:
     nump1 +=1
    else:
     nump2 +=1 
 cellcount.append(numA)  
 cellcount.append(numB)    
 cellcount.append(nump1)
 cellcount.append(nump2)           
 return cellcount
def column(matrix, i):
    return [row[i] for row in matrix]    


# In[11]:

Results = []
Ambiente = []
for t in range(50):
 ambiente = random.randint(1,3)
 Ambiente.append(ambiente)   
 for k in xrange(n):
  for j in xrange(n):
   for i in xrange(n):
    if culture[i][j][k][2] >= 1 and culture[i][j][k][0] == 'A':
     culture[i][j][k][0] ='B'  
    elif culture[i][j][k][2] >= 1 and culture[i][j][k][0] == 'B':
     culture[i][j][k][0] ='A'
    elif culture[i][j][k][0] == 'A' and culture[i][j][k][1] == 1 and ambiente == 1:
     culture[i][j][k][1] = random.randint(1,3)
    elif culture[i][j][k][0] == 'A' and culture[i][j][k][1] == 2 and ambiente == 2:
     culture[i][j][k][1] = random.randint(1,3)
    elif culture[i][j][k][0] == 'A' and culture[i][j][k][1] == 1 and ambiente == 2:
     culture[i][j][k][1] = random.randint(1,3)
     culture[i][j][k][2] += 1
    elif culture[i][j][k][0] == 'A' and culture[i][j][k][1] == 2 and ambiente == 1:
     culture[i][j][k][1] = random.randint(1,3)
     culture[i][j][k][2] += 1   
    elif culture[i][j][k][0] == 'B' and culture[i][j][k][1] == 1 and ambiente == 1:
     culture[i][j][k][1] = 1
    elif culture[i][j][k][0] == 'B' and culture[i][j][k][1] == 2 and ambiente == 2:
     culture[i][j][k][1] = 2
    elif culture[i][j][k][0] == 'B' and culture[i][j][k][1] == 2 and ambiente == 1:
     culture[i][j][k][1] = 1
     culture[i][j][k][2] += 1
    elif culture[i][j][k][0] == 'B' and culture[i][j][k][1] == 1 and ambiente == 2:
     culture[i][j][k][1] = 2
     culture[i][j][k][2] += 1      
 Results.append(countcell())    


# In[17]:

from pylab import *
figure(figsize=(20,20))
plot(linspace(0,500,50),column(Results,2),'k-',lw=2,label='Phenotype1')
plot(linspace(0,500,50),column(Results,3),'b-',lw=2,label='Phenotype2')
plot(linspace(0,500,50),column(Results,0),'g--',lw=2,label='GenotypeA')
plot(linspace(0,500,50),column(Results,1),'r--',lw=2,label='GenotypeB')
plot(linspace(0,500,50),Ambiente,'m^')
ylim([-1,27])
xlim([1,100])
legend(loc='upper left')
savefig("results.png")


# In[44]:

import numpy as np
np.savetxt("output.csv", Results , delimiter=",", fmt='%s')
