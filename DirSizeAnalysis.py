import os
import sys
import getopt
from enum import Enum

class ByteSize(Enum):
	B = 1
	KB = 1024
	MB = 1024**2
	GB = 1024**3

def GetSize(inputSize):
	whiteSpace = " "
	if inputSize < ByteSize.B.value*1024:
		return inputSize
	elif inputSize < ByteSize.KB.value*1024:
		return repr(round(inputSize / ByteSize.KB.value, 2)) + whiteSpace + ByteSize.KB.name
	elif inputSize < ByteSize.MB.value*1024:
		return repr(round(inputSize / ByteSize.MB.value, 2)) + whiteSpace + ByteSize.MB.name
	elif inputSize < ByteSize.GB.value*1024:
		return repr(round(inputSize / ByteSize.GB.value, 2)) + whiteSpace + ByteSize.GB.name

def GetDirTotalSize(inputPath = '.'):
	calcDirSize = 0
	maxNumberOfLargestFiles = 10
	for dirPath, dirName, fileNames in os.walk(inputPath):
		for fileName in fileNames:
			filePath = os.path.join(dirPath, fileName)
			fileSize = os.path.getsize(filePath)
			calcDirSize += fileSize
	return calcDirSize

def GetLargestFiles(maxNumber):
	for i in range(maxNumber):
		biggestFileList.append(filePath, fileSize)
	return biggestFileList

def Main(argv):
	inputFileName = ''
	outputFileName = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('DirSizeAnalysis.py -i <inputFileName> -o <outputFileName>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('DirSizeAnalysis.py -i <inputFileName> -o <outputFileName>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputFileName = arg
		elif opt in ("-o", "--ofile"):
			outputFileName = arg
	
	with open(inputFileName, "r") as inputFile:
		dirNames = inputFile.readlines()

	dirNames = { "c:/gry", "c:/users/barto" }
	
	for dirName in dirNames:
		with open(outputFileName, "w") as outputFile:
			outputFile.write(dirName)
		print(dirName)
		print("Directory size: " + GetSize(GetDirTotalSize("%s" % dirName)))

if __name__ == "__main__":Main(sys.argv[1:])