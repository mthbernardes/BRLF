import os
import sys
import fnmatch

def list_dirs():
	folder_log = sys.argv[1]
	search = sys.argv[2]

	for root, dir, files in os.walk(folder_log):
		print root
		print ""
		for file in fnmatch.filter(files, "*"):
				print "..." + file
				get_infos(root,file,search)
				print
		print ""

def get_infos(root,file,search):
	pathbase = root+'\\'+file
	file = open(pathbase,'r')
	for linha in file:
		linha = linha.strip()
		if search in linha:
			print linha
		
if len(sys.argv) < 3:
	print 'Informa o caminho da pasta de logs'
	exit()
else:
	list_dirs()
