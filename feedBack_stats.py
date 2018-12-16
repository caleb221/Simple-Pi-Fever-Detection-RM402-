#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:21:02 2018

I NEED TO DO STATISTICS ON THE RESULTS

@author: caleb
"""

import numpy as np
import json
import os
import glob
import matplotlib.pyplot as plt
import scipy.stats as st


# extract all 8 questions
#/home/caleb/Desktop/notes/researchMethods/betterNode/feedBack/

folder_path= '/home/caleb/Desktop/notes/researchMethods/betterNode/feedBack/'
data=[]
for filename in glob.glob(os.path.join(folder_path, '*.json')):
  with open(filename, 'r') as f:
    currentdata = json.load(f)
    data.append(currentdata)
    #print (filename)

dataPoints=len(data)
ir_res=[]
interLevel=[]
reliability=[]
sickness=[]
hospUse=[]
thermoUse=[]
learnability=[]

for i in range(dataPoints):
    #print(data[i]['name'])
    ir_res.append(data[i]['IR_resp'])
    interLevel.append(data[i]['interaction'])
    reliability.append(data[i]['reliable'])
    sickness.append(data[i]['sick_level'])
    hospUse.append(data[i]['useInHopsital'])
    thermoUse.append(data[i]['thermometerComp'])
    learnability.append(data[i]['learnable'])

# put nominals go to numpy
npRel=np.array(reliability).astype(np.float)
npInteraction=np.array(interLevel).astype(np.float)
npSick=np.array(sickness).astype(np.float)
npLearn=np.array(learnability).astype(np.float)
npLearn=npLearn
#this is time based 0-60
# take a little longer than needed
# scale factor  factor while preserving value..
# 
#AVERAGES
relAvg=np.average(npRel)
interAvg=np.average(npInteraction)
sickAvg=np.average(npSick)
learnAvg=np.average(npLearn)

#MEDIANS
relMed=np.median(npRel)
interMed=np.median(npInteraction)
sickMed=np.median(npSick)
learnMed=np.median(npLearn)

#STANDARD DERIVATIONS
relStd=np.std(npRel)
interStd=np.std(npInteraction)
sickStd=np.std(npSick)
learnStd=np.std(npLearn)

outplot='/home/caleb/Desktop/notes/researchMethods/RM/'

"""
fig, (p1,p2) = plt.subplots(2,2)

bin=[x for x in range(12)]
plt.subplot(221)
plt.title("User's Reliability")
plt.xlabel("Reliability scale")
plt.ylabel("submission Frequency")
plt.hist(npRel,bin,histtype='bar',rwidth=.5,color='orange')
#plt.show()


plt.subplot(222)
plt.title("UI Interaction")
plt.xlabel("Ease of access scale")
plt.ylabel("submission Frequency")
plt.hist(npInteraction,bin,histtype='bar',rwidth=.5,color='green')
#plt.show()

plt.subplot(223)
plt.title("User's reported Sickness")
plt.xlabel("Rated sickness during interaction")
plt.ylabel("Users rated health")
plt.hist(npSick,bin,histtype='bar',rwidth=.5)
#plt.show()

bin=[x for x in range(61)]
plt.subplot(224)
plt.title("Time spent using device")
plt.xlabel("Time (s)")
plt.ylabel("submission Frequency")

plt.hist(npLearn,bin,histtype='bar',rwidth=1,color='red')

left  = 0.125  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.5   # the bottom of the subplots of the figure
top = 2      # the top of the subplots of the figure
wspace = .4   # the amount of width reserved for space between subplots,
               # expressed as a fraction of the average axis width
hspace = 0.3   # the amount of height reserved for space between subplots,
               # expressed as a fraction of the average axis height
               

fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
#plt.show()
plt.savefig(outplot+'DEMSTATS.png', bbox_inches='tight',dpi=400)

print("\n")
print("Reliability avg",relAvg)
print("Reliability median",relMed)
print("Reliability stdev ",relStd)
print("\n")
print("interaction avg",interAvg)
print("interaction median ",interMed)
print("interaction stdev ",interStd)
print("\n")
print("sickness avg",sickAvg)
print("sickness median ",sickMed)
print("sickness stdev ",sickStd)
print("\n")
print("learnability avg ",learnAvg)
print("learnability median ",learnMed)
print("learnability stdev ",learnStd)
"""
#==========================================
# compare reported sickness and IR response
#==========================================

npRel=np.sort(npRel)
npLearn=np.sort(npLearn)
npInteraction=np.sort(npInteraction)
fig, (p1,p2) = plt.subplots(1,2)

fit = np.polyfit(npRel,npInteraction,1)
fit_fn = np.poly1d(fit) 
# fit_fn is now a function which takes in x and returns an estimate for y

#regression line between reliability and interactivity
plt.subplot(121)

plt.plot(npRel,npInteraction, 'bo', npRel, fit_fn(npRel), '--k')
plt.xlim(min(npRel)-.2, max(npRel)+.2)
plt.ylim(min(npInteraction), max(npInteraction)+1)
plt.title("Reliability and Interaction Regression")
plt.xlabel("Interaction")
plt.ylabel("reliability")

# and then interaction between reliablity and learnability
#now we can say based
# users feel that the easier it is to learn a device, the more reliable it is precieved??
#
plt.subplot(122)
fit = np.polyfit(npRel,npLearn,1)
fit_fn = np.poly1d(fit) 

plt.plot(npRel,npLearn, 'ro', npRel, fit_fn(npRel), '--k')
plt.xlim(min(npRel)-.2, max(npRel)+.2)
plt.ylim(min(npLearn), max(npLearn)+.5)
plt.title("Reliability and Learnability Regression")
plt.xlabel("Learnability")
plt.ylabel("reliability")

left =0
bottom =0
right =1
top =1
wspace = .25
hspace =.5

fig.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
#plt.savefig(outplot+'learn_fitLines.png', bbox_inches='tight')
plt.show()

#============================================================
fig,myplt=plt.subplots(2,2)
plt.subplot(211)
plt.title("Algorithm Diagnosis")
plt.ylabel("User Frequency")

plt.hist(ir_res,'auto',color='darkred')
plt.tick_params(axis='x',labelsize=16)

plt.subplot(212)
plt.title("Users reported Sickness")
plt.ylabel("User Frequency")
plt.xlabel("health scale (10=Healthy)")
plt.hist(npSick,bins=[1,2,3,4,5,6,7,8,10,11],rwidth=.5)
plt.tick_params(axis='x',labelsize=8)

fig.subplots_adjust(top=1.5,left=.5, wspace=wspace, hspace=hspace)

plt.savefig(outplot+'AlgorithmTest.png', bbox_inches='tight',dpi=200)
plt.show()


fig, myplt=plt.subplots(2,2)

plt.subplot(211)
plt.title("Usage in Hospital")
plt.hist(hospUse,'auto',color='green')
plt.tick_params(axis='x',labelsize=14)
plt.ylabel("User Frequency")

#plt.savefig(outplot+'HospUse.png', bbox_inches='tight')
#plt.show()

plt.subplot(212)
plt.title("Thermometer comparison")
plt.hist(thermoUse,'auto')
plt.tick_params(axis='x',labelsize=14)
plt.ylabel("User Frequency")
#plt.savefig(outplot+'thermResp.png',bbox_inches='tight')

fig.subplots_adjust(top=1.5,left=.5, wspace=wspace, hspace=hspace)
plt.savefig(outplot+'hospitalBinary.png',bbox_inches='tight',dpi=200)
plt.show()
#================================================================


relInt_pearCoef, twotailpRI=st.pearsonr(npRel,npInteraction)
relLearn_pearCoef, twotailpRL=st.pearsonr(npRel,npLearn)
lrnInt_pearCoef,twotailLI=st.pearsonr(npInteraction,npLearn)

print("REL INTERACT PEARSON:  ",relInt_pearCoef)
print("REL LEARN PEARSON: ",relLearn_pearCoef)
print("LEARN INTERACT PEARSON:  ",lrnInt_pearCoef)

ir_num=[]
binSick=[]
total_perf=[]
for i in range(len(ir_res)):
    
    if('fine' in ir_res[i]):
        ir_num.append(1)
    else:
        ir_num.append(0)
    
    if(npSick[i]<5):
        binSick.append(0)
    elif(npSick[i]==5):
        binSick.append(np.nan)
    elif(npSick[i]>5):
        binSick.append(1)
        
    if(ir_num[i] == binSick[i]):
        total_perf.append(1)
        
algorithm_perf=(np.sum(total_perf)/dataPoints) *100
print("reported Algorithm Performance: ",algorithm_perf)
#
# T^2
# chi^2
# no citations in abstract       
# inferrential statistics
# attach code in appendices (optional)
# RE-WRITE ANYTHING YOU USE FROM PROPOSAL
# 4-8 pages
# 
# background section is like lit review
# discussion is important
"""
A One Sample T-Test is a statistical test used to evaluate the null hypothesis
that the mean m of a 1D sample dataset of independant 
observations is equal to the true mean μ of the 
population from which the data is sampled. In other words, 
"""