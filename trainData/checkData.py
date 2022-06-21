#!/usr/bin/env python3
import sys
import os 
import csv    

errorfile="Errorfile.txt"
def writeErrors(message,errors):
    print(message)
    errors.write(message+os.linesep)

def countFastaLength(f):
    line=f.readline()
    while(line=="" or line[0]==">" or line[0]==";"): #'>',';' coments in fasta
        line=f.readline()
    return len(line)

def getFastaSegLength(name, fastaFiles,errors):

    fileName = fastaFiles+"/"+name+".fasta"  
    try:
      if not os.path.isfile(fileName):return -1

      f=open(fileName, "r")
      return countFastaLength(f)
    except IOError:
      writeErrors("Error: {0} can not be opened".format(fileName),errors)
      return 0

def checkLengthInCsv(datasetName, fasta,pathCsv,errors): 
    correct =True
    try:
      with open(pathCsv, 'r') as f:     
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for i, line in enumerate(reader):
           fastaSegLen =getFastaSegLength(line[0], fasta +"/"+ datasetName,errors)
           csvLen=len(line[1].replace(' ',''))  #return -1 if file does not exist
           if not (fastaSegLen==csvLen):
               writeErrors("ERROR line: {0} name: {1} in: {2}".format(i+2,line[0],pathCsv),errors)
               if(fastaSegLen==-1):
                   writeErrors("File does not exist ".format(),errors)
               else:
                   writeErrors("Length in Csv is: {0} but length of fasta is: {1}".format(csvLen,fastaSegLen),errors)
               correct=False
      return correct
    except IOError as e:

        writeErrors(("I/O error({0}): {1}".format(e.errno, e.strerror)),errors)
        writeErrors("{0} can not be opened".format(pathCsv),errors)


def checkLength(labels, fasta ,errors ): #check if labeling is the same length as fasta 
    # Iterate directory
    if not(os.path.isdir(labels)):
        writeErrors("{0} is not a directory".fotmat(labels),errors)
    for path in os.listdir(labels):
    # check if current path is a file
        if os.path.isfile(os.path.join(labels, path)):
            datasetName=os.path.basename(path).rpartition('.')
            correct=checkLengthInCsv(datasetName[0],fasta,labels +"/"+ path,errors)
            print(path)
            if correct:
               print(path," is correct.")
            else:
               print(path," is incorrect.")
        else:
            writeErrors("{0} isn`t a file".format(os.path.join(labels, path)),errors)
def main():   #arg[1]...bindings_labeled, arg[2]...fasta
    args=sys.argv  
    if (len(args)==1):
        args.append("../trainData/bindings_labeled")
        args.append("../trainData/fasta")
    errors = open(errorfile, "w") 
    checkLength(args[1],args[2],errors)
    errors.close()
    

if __name__ == "__main__":
    main()
