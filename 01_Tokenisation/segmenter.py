
#SEGEMENTATION FOR ROMANI LANGUAGE

import sys


line = sys.stdin.readline()
while line != '':
	for token in line.split(' '):
		if token[-1] in '!?':
			sys.stdout.write(token + '\n')
		elif token[-1] == '.':
			if token in  ['D.C.', 'P.T.', 'U.K.', '6.6', '4.8', '1.9', '1.8', '0.6', '99.59', '0.28', '0.11', '3.10', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', 'W.', 'B.R.', 'abr.', 'Jr.', 'St.' 'Anav.', 'Ando J.', 'Ando Sud-J.', ' "']:
				sys.stdout.write(token + ' ')
			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()



