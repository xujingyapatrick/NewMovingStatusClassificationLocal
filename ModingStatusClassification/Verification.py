'''
Created 

@author: Patric
'''
from ModingStatusClassification import RandomForestGene
from sklearn.ensemble import RandomForestClassifier

import pylab as pl
import pandas as pd
import numpy as np
import pickle
from ModingStatusClassification.RawDataProcessor import RawDataProcessor
from _ast import Str
class Verification(object):
    
    
    def tableAnalysisForStatus(self, forest, testdata):
        rfg=RandomForestGene.RandomForestGene()
        testfeatures=rfg.getfeatures(testdata)
        testtypes=rfg.gettypes(testdata)
        preds = forest.predict(testfeatures)
        #preds = forest.predict_proba(testfeatures)
 #==============================================================================
 #        returns [[ 1.     0.     0.   ]
 # [ 1.     0.     0.   ]
 # [ 1.     0.     0.   ]
 # ..., 
 # [ 0.     1.     0.   ]
 # [ 0.     1.     0.   ]
 # [ 0.     0.995  0.005]]
 #        we can use preds[m][n] to fet values
 #==============================================================================
        #print(testtypes)
        #print(preds)
        tablist=pd.crosstab(testtypes, preds, rownames=['actual'], colnames=['preds'])
        
        tablistpercentage=pd.crosstab(testtypes, preds, rownames=['actual'], colnames=['preds']).apply(lambda r: r/r.sum(), axis=1)
        
        percent=(tablist['running']['running']+tablist['walking']['walking']+tablist['sitting']['sitting'])/(1.0*np.sum(np.sum(tablist)))
        print('correct rate = '+str(percent))
        return tablist,tablistpercentage
    
    def tableAnalysisForWalkingSpeed(self, forest, testdata):
        rfg=RandomForestGene.RandomForestGene()
        testfeatures=rfg.getfeatures(testdata)
        testtypes=rfg.gettypes(testdata)
        preds = forest.predict(testfeatures)
        #print(testtypes)
        #print(preds)
        tablist=pd.crosstab(testtypes, preds, rownames=['actual'], colnames=['preds'])
        
        tablistpercentage=pd.crosstab(testtypes, preds, rownames=['actual'], colnames=['preds']).apply(lambda r: r/r.sum(), axis=1)
        
        #percent=(tablist['running']['running']+tablist['walking']['walking']+tablist['sitting']['sitting'])/(1.0*np.sum(np.sum(tablist)))
        #print('correct rate = '+str(percent))
        return tablist,tablistpercentage
    
    def tableAnalysisForRunningSpeed(self, forest, testdata):
        rfg=RandomForestGene.RandomForestGene()
        testfeatures=rfg.getfeatures(testdata)
        testtypes=rfg.gettypes(testdata)
        preds = forest.predict(testfeatures)
        #print(testtypes)
        #print(preds)
        tablist=pd.crosstab(testtypes, preds, rownames=['actual'], colnames=['preds'])
        
        tablistpercentage=pd.crosstab(testtypes, preds, rownames=['actual'], colnames=['preds']).apply(lambda r: r/r.sum(), axis=1)
        
        #percent=(tablist['running']['running']+tablist['walking']['walking']+tablist['sitting']['sitting'])/(1.0*np.sum(np.sum(tablist)))
        #print('correct rate = '+str(percent))
        return tablist,tablistpercentage
    def plotAnalysisForWalkingSpeed(self):
        walkspeeds=[10,15,20,25,30,35]
       
        dataProcessor= RawDataProcessor()
        train= RandomForestGene.RandomForestGene()

    
    
        
    #    pddata=processDataForWalkingSpeed()
        pddata=dataProcessor.getFeaturePandasFromDataFile('walkdata.data')
    
        traindata, testdata=train.dataspilit(pddata,0.8)
        forest=train.datatrain(traindata,numoftrees=200)
        #with open('forestWalking.pkl', 'wb') as f:
        #    pickle.dump(forest, f)
        testfeatures=train.getfeatures(testdata)
        testtypes=train.gettypes(testdata)
        testtypes=testtypes.tolist()
        probArray=forest.predict_proba(testfeatures)
        predictAndRealSpeed=np.zeros((len(testtypes),2), dtype=float)
        difAverage=0.0
        difAbsAverage=0.0
        i=0;
        #print(testtypes)
        #print(testtypes[0])
        
        while i<len(testtypes):
            predictAndRealSpeed[i,0]=int(testtypes[i])/10.0
            for j in range(0,len(walkspeeds)):
                predictAndRealSpeed[i,1]=predictAndRealSpeed[i,1]+walkspeeds[j]*probArray[i][j]
            predictAndRealSpeed[i,1]=predictAndRealSpeed[i,1]/10.0
            difAverage=difAverage+(predictAndRealSpeed[i,1]-predictAndRealSpeed[i,0])
            difAbsAverage=difAbsAverage+np.abs(predictAndRealSpeed[i,1]-predictAndRealSpeed[i,0])
            i=i+1
        difAverage=difAverage/len(testtypes)
        difAbsAverage=difAbsAverage/len(testtypes)
        print("walking speed prediction")
        
        print("average differences between prediction and real speed: "+str(difAverage))
        print("abs average differences between prediction and real speed: "+str(difAbsAverage))
        pl.figure(1,figsize=(8,8))
        pl.plot(predictAndRealSpeed[:,0], predictAndRealSpeed[:,1],'.')
        pl.xlabel(u"real speed(mile/h)")
        pl.ylabel(u"predict speed(mile/h)")
        pl.title('Walking speed prediction verification')
        
        pl.show()
        print('end plot')
        
        
    def plotAnalysisForRunningSpeed(self):
        runspeeds=[25,30,35,40,45,50]
       
        dataProcessor= RawDataProcessor()
        train= RandomForestGene.RandomForestGene()

    
    
        
    #    pddata=processDataForWalkingSpeed()
        pddata=dataProcessor.getFeaturePandasFromDataFile('rundata.data')
    
        traindata, testdata=train.dataspilit(pddata,0.8)
        forest=train.datatrain(traindata,numoftrees=200)
        #with open('forestWalking.pkl', 'wb') as f:
        #    pickle.dump(forest, f)
        testfeatures=train.getfeatures(testdata)
        testtypes=train.gettypes(testdata)
        testtypes=testtypes.tolist()
        probArray=forest.predict_proba(testfeatures)
        predictAndRealSpeed=np.zeros((len(testtypes),2), dtype=float)
        difAverage=0.0
        difAbsAverage=0.0
        i=0;
        #print(testtypes)
        #print(testtypes[0])
        while i<len(testtypes):
            predictAndRealSpeed[i,0]=int(testtypes[i])/10.0
            for j in range(0,len(runspeeds)):
                predictAndRealSpeed[i,1]=predictAndRealSpeed[i,1]+runspeeds[j]*probArray[i][j]
            predictAndRealSpeed[i,1]=predictAndRealSpeed[i,1]/10.0   
            difAverage=difAverage+(predictAndRealSpeed[i,1]-predictAndRealSpeed[i,0]) 
            difAbsAverage=difAbsAverage+np.abs(predictAndRealSpeed[i,1]-predictAndRealSpeed[i,0])
            i=i+1
        difAverage=difAverage/len(testtypes)
        difAbsAverage=difAbsAverage/len(testtypes)
        print("running speed prediction")
        print("average differences between prediction and real speed: "+str(difAverage))
        print("average abs differences between prediction and real speed: "+str(difAbsAverage))
        
        
        
        pl.figure(2,figsize=(8,8))
        pl.plot(predictAndRealSpeed[:,0], predictAndRealSpeed[:,1],'.')
        pl.xlabel(u"real speed(mile/h)")
        pl.ylabel(u"predict speed(mile/h)")
        pl.title('Running speed prediction verification')
        
        pl.show()
        print('end plot')


