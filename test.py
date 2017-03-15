#!/usr/bin/env python
#from os.path import basename,exists,dirname
#from random import randint,random
#import os
import glob
#import sys
#import commands
import time
#import numpy as np
#import matplotlib.pyplot as plt
#import collections
#import pickle
#import cPickle as pickle
import shelve
from message import send_message

all_feature_keys=['pdb', 'label', 'set_nr', 'model1', 'model2', 'old_features', 'clash', 'Sc', 'nBSA', 'Fintres', 'Ld', 'rGb', 'INTCOMP', 'INTPAIR']
feature_keys=['pdb', 'label', 'set_nr', 'old_features', 'clash', 'Sc', 'nBSA', 'Fintres', 'Ld', 'rGb', 'INTCOMP', 'INTPAIR']

def replace_missing(key,value):
    if value=='None' or value==[] or value=='NaN': # empty clash or missing dict
        print key,value
        if key=="INTCOMP":
            zeros='0 '*20
        elif key=="INTPAIR":
            zeros='0 '*210
        else:
            zeros='0 '
        return zeros
    if type(value) is list:
        m='' # multiple values
        for v in value:
            m= m + v + ' '
        return m
    else:
        return value + ' '
        
def featureString(ordered_dict):
    string=''
    for key,value in ordered_dict.iteritems():
        if key in feature_keys: # just give feature values back that we want
            feature=replace_missing(key,value)
            string=string + feature
    string= string + '\n' 
    return string


def list_keys():
    # This function lists pdb keys from NEW.all_data.dat2 file  
    key_list=[]
    for line in file("/home/x_amisi/proj/RandomForest/NEW.all_data.dat2"):
        col=line.split()
        key_list.append(col[0])
    return key_list 

def main():
    pdbs=list_keys()
    d=shelve.open('/home/x_amisi/proj/RandomForest/tmp/shelve')
    "test"
    #t=d['Q95604_0_Q53H82_0_3cx5_F_3cx5_I.pdb']
    #print t
    #print featureString(t)
    
    for pdb in pdbs[:10000]:
        ofd=d[pdb] #Ordered feature dictionary
        print featureString(ofd)
               
    d.close()

if __name__ =='__main__':
    main()
