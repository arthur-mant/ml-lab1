## script para extrair Dummy Features da base de digitos manuscritos
## As imagens sao normalizadas no tamanho indicado nas variavies X e Y
## Aprendizagem de Maquina, Prof. Luiz Eduardo S. Oliveira
##
##

import sys
import cv2
import os
import numpy as np
import random

def load_images(path_images, fout, x, y):
	print ('Loading images...')
	archives = os.listdir(path_images)
	images = []
	arq = open('digits/files.txt')
	lines = arq.readlines()
	print ('Extracting dummy features')
	for line in lines:
		aux = line.split('/')[1]
		image_name = aux.split(' ')[0]
		label = line.split(' ')[1]
		label = label.split('\n')
		
		for archive in archives:
			if archive == image_name:
				image = cv2.imread(path_images +'/'+ archive, 0)
				rawpixel(image, label[0], fout, x, y)
				
				#images.append((image, label))

	print ('Done. Take a look into features.txt')
	return images

#########################################################
# Usa o valor dos pixels como caracteristica
#
#########################################################
	
def rawpixel(image, label, fout, X, Y):
	
	## novas dimensoes
	
	image = cv2.resize(image, (X,Y) )
	#cv2.imshow("image", image )
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	
	fout.write(str(label) +  " ")
	
	indice = 0
	for i in range(Y):
		#vet= []
		for j in range(X):
			if( image[i][j] > 128):
				v = 0
			else:
				v = 1	
			#vet.append(v)		
	
			fout.write(str(indice)+":"+str(v)+" ")
			indice = indice+1

	fout.write("\n")
			

if __name__ == "__main__":


	fout = open("features.txt","w")
	
	if len(sys.argv) < 3:
		print("inform X and Y")
		exit()

	x = int(sys.argv[1])
	y = int(sys.argv[2])

	images = load_images('digits/data', fout, x, y)

	fout.close
	
		



