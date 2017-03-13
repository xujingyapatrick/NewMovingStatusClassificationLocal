'''
Created on 2016101

@author: Patric
'''

import pandas as pd
import numpy as np
import pickle

from ModingStatusClassification import RawDataProcessor, RandomForestGene, Verification

def processDataForStatus():
    dataProcessor= RawDataProcessor.RawDataProcessor()
    train= RandomForestGene.RandomForestGene()
    predictAnalyser=Verification.Verification()
    ##raw is in dictionaryy formate
    status=['running','walking','sitting']
    walkspeeds=[10,15,20,25,30,35]
    runspeeds=[25,30,35,40,45,50] 

    #dataProcessor.genefeaturesframe()
    
    pddata=dataProcessor.genefeaturesframe()
    
    m=status[0]
    for n in runspeeds:
        fullname=m+str(n)+'.txt'
        record=dataProcessor.parseRawdataFromEvaBoard(fullname, m)
        features=dataProcessor.genefeaturesFast(record,kpoints=1000)
        pddata=pddata.append(features, ignore_index=True)
        print(m+str(n)+' is parsed \n')
    
    m=status[1]
    for n in walkspeeds:
        fullname=m+str(n)+'.txt'
        record=dataProcessor.parseRawdataFromEvaBoard(fullname, m)
        features=dataProcessor.genefeaturesFast(record,kpoints=1000)
        pddata=pddata.append(features, ignore_index=True)
        print(m+str(n)+' is parsed \n')
    m=status[2]
    fullname=m+'.txt'
    record=dataProcessor.parseRawdataFromEvaBoard(fullname, m)
    features=dataProcessor.genefeaturesFast(record,kpoints=1000)
    pddata=pddata.append(features, ignore_index=True)
    print(m+str(n)+' is parsed \n')    
    
    f=open('alldata.data','w')
    i=0
    while i < len(pddata):
        m=str(pddata['accavgx'][i])+','+str(pddata['accavgy'][i])+','+str(pddata['accavgz'][i])
        m=m+','+str(pddata['accmaxx'][i])+','+str(pddata['accmaxy'][i])+','+str(pddata['accmaxz'][i])
        m=m+','+str(pddata['accminx'][i])+','+str(pddata['accminy'][i])+','+str(pddata['accminz'][i])
        m=m+','+str(pddata['accabsx'][i])+','+str(pddata['accabsy'][i])+','+str(pddata['accabsz'][i])
        m=m+','+str(pddata['accavgres'][i])+','+str(pddata['Dx'][i])+','+str(pddata['Dy'][i])
        m=m+','+str(pddata['Dz'][i])+','+str(pddata['Da1'][i])+','+str(pddata['Da2'][i])
        m=m+','+str(pddata['Da3'][i])+','+str(pddata['Db1'][i])+','+str(pddata['Db2'][i])
        m=m+','+str(pddata['Db3'][i])+','+str(pddata['D1'][i])+','+str(pddata['D2'][i])
        m=m+','+str(pddata['D3'][i])+','+str(pddata['frex'][i])+','+str(pddata['frey'][i])
        m=m+','+str(pddata['frez'][i])+','+str(pddata['types'][i])+'\n'
        f.write(m)
        i=i+1
    f.close()
    return pddata
    
def processDataForWalkingSpeed():
    dataProcessor= RawDataProcessor.RawDataProcessor()
    train= RandomForestGene.RandomForestGene()
    predictAnalyser=Verification.Verification()
    ##raw is in dictionaryy formate
    status=['walking']
    walkspeeds=[10,15,20,25,30,35]    
    #dataProcessor.genefeaturesframe()
    
    pddata=dataProcessor.genefeaturesframe()
    
    m=status[0]
    for n in walkspeeds:
        fullname=m+str(n)+'.txt'
        record=dataProcessor.parseRawdataFromEvaBoard(fullname, str(n))
        features=dataProcessor.genefeaturesFast(record,kpoints=1000)
        pddata=pddata.append(features, ignore_index=True)
        print(m+str(n)+' is parsed \n')
    
    f=open('walkdata.data','w')
    i=0
    while i < len(pddata):
        m=str(pddata['accavgx'][i])+','+str(pddata['accavgy'][i])+','+str(pddata['accavgz'][i])
        m=m+','+str(pddata['accmaxx'][i])+','+str(pddata['accmaxy'][i])+','+str(pddata['accmaxz'][i])
        m=m+','+str(pddata['accminx'][i])+','+str(pddata['accminy'][i])+','+str(pddata['accminz'][i])
        m=m+','+str(pddata['accabsx'][i])+','+str(pddata['accabsy'][i])+','+str(pddata['accabsz'][i])
        m=m+','+str(pddata['accavgres'][i])+','+str(pddata['Dx'][i])+','+str(pddata['Dy'][i])
        m=m+','+str(pddata['Dz'][i])+','+str(pddata['Da1'][i])+','+str(pddata['Da2'][i])
        m=m+','+str(pddata['Da3'][i])+','+str(pddata['Db1'][i])+','+str(pddata['Db2'][i])
        m=m+','+str(pddata['Db3'][i])+','+str(pddata['D1'][i])+','+str(pddata['D2'][i])
        m=m+','+str(pddata['D3'][i])+','+str(pddata['frex'][i])+','+str(pddata['frey'][i])
        m=m+','+str(pddata['frez'][i])+','+str(pddata['types'][i])+'\n'
        f.write(m)
        i=i+1
    f.close()
    return pddata
    
def processDataForRunningSpeed():
    dataProcessor= RawDataProcessor.RawDataProcessor()
    train= RandomForestGene.RandomForestGene()
    predictAnalyser=Verification.Verification()
    ##raw is in dictionaryy formate
    status=['running']
    runspeeds=[25,30,35,40,45,50] 
    
    #dataProcessor.genefeaturesframe()
    
    pddata=dataProcessor.genefeaturesframe()
    
    m=status[0]
    for n in runspeeds:
        fullname=m+str(n)+'.txt'
        record=dataProcessor.parseRawdataFromEvaBoard(fullname, str(n))
        features=dataProcessor.genefeaturesFast(record,kpoints=1000)
        pddata=pddata.append(features, ignore_index=True)
        print(m+str(n)+' is parsed \n')
    
    f=open('rundata.data','w')
    i=0
    while i < len(pddata):
        m=str(pddata['accavgx'][i])+','+str(pddata['accavgy'][i])+','+str(pddata['accavgz'][i])
        m=m+','+str(pddata['accmaxx'][i])+','+str(pddata['accmaxy'][i])+','+str(pddata['accmaxz'][i])
        m=m+','+str(pddata['accminx'][i])+','+str(pddata['accminy'][i])+','+str(pddata['accminz'][i])
        m=m+','+str(pddata['accabsx'][i])+','+str(pddata['accabsy'][i])+','+str(pddata['accabsz'][i])
        m=m+','+str(pddata['accavgres'][i])+','+str(pddata['Dx'][i])+','+str(pddata['Dy'][i])
        m=m+','+str(pddata['Dz'][i])+','+str(pddata['Da1'][i])+','+str(pddata['Da2'][i])
        m=m+','+str(pddata['Da3'][i])+','+str(pddata['Db1'][i])+','+str(pddata['Db2'][i])
        m=m+','+str(pddata['Db3'][i])+','+str(pddata['D1'][i])+','+str(pddata['D2'][i])
        m=m+','+str(pddata['D3'][i])+','+str(pddata['frex'][i])+','+str(pddata['frey'][i])
        m=m+','+str(pddata['frez'][i])+','+str(pddata['types'][i])+'\n'
        f.write(m)
        i=i+1
    f.close()
    return pddata   

def buildAndStoreForests():
    
    dataProcessor= RawDataProcessor.RawDataProcessor()
    train= RandomForestGene.RandomForestGene()
    predictAnalyser=Verification.Verification()
    pddata=processDataForStatus()

#print(iris.feature_names)
#    pddata = pd.DataFrame(iris.data, columns=iris.feature_names)
    
#    pddata["types"]=pd.Categorical.from_codes(iris.target,iris.target_names,ordered=True)
    traindata, testdata=train.dataspilit(pddata,0.8)
    forest=train.datatrain(traindata,numoftrees=200)

    with open('forestStatus.pkl', 'wb') as f:
        pickle.dump(forest, f)
    
    tablist, percentage=predictAnalyser.tableAnalysisForStatus(forest,testdata)
    print("status classification")
    print(tablist)

    
    pddata=processDataForWalkingSpeed()
    traindata, testdata=train.dataspilit(pddata,0.8)
    forest=train.datatrain(traindata,numoftrees=200)
    with open('forestWalking.pkl', 'wb') as f:
        pickle.dump(forest, f)
    
    
    tablist, percentage=predictAnalyser.tableAnalysisForWalkingSpeed(forest,testdata)
    print("walking speed classification")
    print(tablist)
    
    
    pddata=processDataForRunningSpeed()
    traindata, testdata=train.dataspilit(pddata,0.8)
    forest=train.datatrain(traindata,numoftrees=200)
    with open('forestRunning.pkl', 'wb') as f:
        pickle.dump(forest, f)
    
    tablist, percentage=predictAnalyser.tableAnalysisForRunningSpeed(forest,testdata)
    print("running speed classification")
    print(tablist)
    print("****************Forest Generation finished!*****************")

def buildAndStoreForestsFromExistingFeatures():
    
    dataProcessor= RawDataProcessor.RawDataProcessor()
    train= RandomForestGene.RandomForestGene()
    predictAnalyser=Verification.Verification()
#    pddata=processDataForStatus()
    pddata=dataProcessor.getClassificationFeaturePandasFromDataFile('alldataWithSpeedAndStatus.data')
#print(iris.feature_names)
#    pddata = pd.DataFrame(iris.data, columns=iris.feature_names)
    
#    pddata["types"]=pd.Categorical.from_codes(iris.target,iris.target_names,ordered=True)
    traindata, testdata=train.dataspilit(pddata,0.7)
    forest=train.datatrain(traindata,numoftrees=500)

    with open('forestStatus.pkl', 'wb') as f:
        pickle.dump(forest, f)
    
    tablist, percentage=predictAnalyser.tableAnalysisForStatus(forest,testdata)
    print("status classification")
    print(tablist)



    
#    pddata=processDataForWalkingSpeed()
    pddata=dataProcessor.getRegressionFeaturePandasFromDataFile('walkdataWithStatus.data')

    traindata, testdata=train.dataspilit(pddata,0.7)
    forest=train.datatrain(traindata,numoftrees=500)
    with open('forestWalking.pkl', 'wb') as f:
        pickle.dump(forest, f)
    
    
    tablist, percentage=predictAnalyser.tableAnalysisForWalkingSpeed(forest,testdata)
    print("walking speed classification")
    print(tablist)
    
    
    
    
#    pddata=proessDataForRunningSpeed()
    pddata=dataProcessor.getRegressionFeaturePandasFromDataFile('rundataWithStatus.data')

    traindata, testdata=train.dataspilit(pddata,0.7)
    forest=train.datatrain(traindata,numoftrees=500)
    with open('forestRunning.pkl', 'wb') as f:
        pickle.dump(forest, f)
    
    tablist, percentage=predictAnalyser.tableAnalysisForRunningSpeed(forest,testdata)
    print("running speed classification")
    print(tablist)
    print("****************Forest Generation finished!*****************")
def generateAllDataWithSpeedAndType():
    f=open("rundata.data",'r')
    line=f.readline()
    fr=open("rundataWithStatus.data",'a')
    while line:
        line=line[:-1]+",running\n"
        fr.write(line)
        line=f.readline()
    f.close()
    fr.close()
    print("running finished!")
    f=open("walkdata.data",'r')
    line=f.readline()
    fr=open("walkdataWithStatus.data",'a')
    while line:
        line=line[:-1]+",walking\n"
        fr.write(line)
        line=f.readline()
    f.close()
    fr.close()
    print("walking finished!")

    f=open("alldata.data",'r')
    line=f.readline()
    fr=open("sitdataWithStatus.data",'a')
    while line:
        if line[-8]=='s':
            line=line[:-8]+"0,sitting\n"
            fr.write(line)
        line=f.readline()
    f.close()
    fr.close()
    print("sitting finished!")
    
    fr=open("alldataWithSpeedAndStatus.data",'a')
    f=open("sitdataWithStatus.data",'r')
    line=f.readline()
    while line:
        fr.write(line)
        line=f.readline()
    f.close()
    f=open("walkdataWithStatus.data",'r')
    line=f.readline()
    while line:
        fr.write(line)
        line=f.readline()
    f.close()
    f=open("rundataWithStatus.data",'r')
    line=f.readline()
    while line:
        fr.write(line)
        line=f.readline()
    f.close()
    fr.close()
    print("all data has finished!")

if __name__=="__main__":
    
#     generateAllDataWithSpeedAndType()
#     predictAnalyser=Verification.Verification()

    buildAndStoreForestsFromExistingFeatures()    
#     #buildAndStoreForestsFromExistingFeatures()
#     predictAnalyser.plotAnalysisForWalkingSpeed()
#     predictAnalyser.plotAnalysisForRunningSpeed()
#     processDataForStatus()
#     processDataForRunningSpeed()
#     processDataForWalkingSpeed()
#     


    #===========================================================================
    # processDataForWalkingSpeed()
    # processDataForRunningSpeed()
    #===========================================================================



    
    
 