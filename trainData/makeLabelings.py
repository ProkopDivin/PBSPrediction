#! /usr/bin/env python3
import sys
import os 
import csv  
def makeName(fileName):
     name=""
     for item in fileName.split('.'):
         if len(item)>=2 and (item[:3]=="pdb"):
             
             break
         if not name=="":
            name=name+'.'+item
         else:name=name+item
     return name
def saveToCsv(name,lastChain,labeling,labelsCsv):
    name2=name+'_'+lastChain
    labelingString="".join(labeling)
    labelsCsv.write('{0},{1}\n'.format(name2,labelingString))

def processFile(labelsCsv, residues):
    try:
      with open(residues, 'r') as f:     
        reader = csv.reader(f, delimiter=',')
        name=os.path.basename(residues)
        if(name[-4:]==".csv"):            
            lastChain=""
            labeling=[]
            for line in reader:
                if (len(line[0])>1): #skip head
                    line=next(reader) 
                    chain=line[0]
                    lastChain=chain
                chain=line[0]
                if not(lastChain==chain):    #devide sequece to a chains
                    saveToCsv(makeName(name),lastChain,labeling,labelsCsv)
                    lastChain=chain
                    labeling=[]
                labeling.append(line[7])
            saveToCsv(makeName(name),lastChain,labeling,labelsCsv)               
    except IOError as e:
       print("{0} can not be open, error ({1}): {2}".format(residues,e.errno, e.strerror))

def makeLabels(labels, residuesDir): #stream to csv file , directory with residuis
    for file in os.listdir(residuesDir):
    # check if current path is a file
        if os.path.isfile(os.path.join(residuesDir, file)):
            filePath=residuesDir+"/"+file
            processFile(labels,filePath)

    
def main(): #args[1]...bindings_labeled, args[2]...residues 
    args=sys.argv  
    if (len(args)==1):
       args.append("trainData/residues")
       args.append("trainData/bindings_labeled")
   
    if not (len(args)==3):print("need 2 arguments")
    for name in os.listdir(args[1]):
    # check if current path is a file
        if os.path.isdir(os.path.join(args[1], name)):
           labelsCsv=args[2]+"/"+name+".csv"
           try:
             labels=open(labelsCsv,"w")
             makeLabels(labels,args[1]+"/"+name)
             labels.close()
           except IOError as e:
             print("{0} can not be open, error ({1}): {2}".format(labelsCsv,e.errno, e.strerror))
           print("Working with",name)
        else:
            print("{0} isn`t a file".format(os.path.join(labels, name)))
    

if __name__=='__main__':

    main()



