import pydicom 
import numpy as np 
import csv 
import sys

def __init__():     
	print()  

def crop_center(img, cropx, cropy):     
	y, x = img.shape     
	startx = x // 2 - (cropx // 2)     
	starty = y // 2 - (cropy // 2)     
	return img[starty:starty + cropy, startx:startx + cropx]  

def convert(file, output):     
	with open(file, "r") as f:         
		reader = csv.reader(f, delimiter=",")         
		count = 1         
		npLists = []         
		for row in reader:             
			print(count, ". ", row[0])             
			ds = pydicom.read_file(row[0]) 
			ycrop = input("Enter number of columns (pixel height): ")
			xcrop = input("Enter number of rows (pixel length): ")
			croppedArray = crop_center(ds.pixel_array, xcrop, ycrop)             
			# print(croppedArray)             
			npLists.append(croppedArray)                   
			count += 1      
	np.savez(output, *npLists)      
	print("Numpy arrays saved!")               

	####### TO LOAD AND PRINT NUMPY ARRAYS FROM FILE  #######   
	loaded = np.load('brainNpArrays.npz' ) 
	i = 0     
	for val in data:             
		index = 'arr_' + str(i)         
		print(loaded[index]) # print arrays         
		i = i + 1  

def main():     
	args1 = sys.argv[1]     
	args2 = sys.argv[2] 
	if args1 and args2:         
		print("input file: ", sys.argv[1])         
		print("destination: ", sys.argv[2])         
		file = sys.argv[1]         
		output = sys.argv[2]         
		convert(file, output)     
	else:         
		print("Input and destination files missing/incorrect.")  

if __name__ == "__main__":     
	main()


