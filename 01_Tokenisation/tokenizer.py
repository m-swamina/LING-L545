#TOKENIZER FOR ROMANI LANGUAGE 

import sys, re

abbr = ['D.C.', 'P.T.', 'U.K.', 'W,', 'B.R. ', 'abr.', 'Jr.', 'St.', 'Anav.']


def tokenise(line, abbr):
	line = re.sub(r'([\(\)”?:!;])', r' \g<1> ', line)
	line = re.sub(r'([^0-9]),', r'\g<1> ,', line)
	line = re.sub(r',([^0-9])', r', \g<1>', line)
	line = re.sub(r'  +', ' ', line)
	output =[]
	for token in line.split(' '):
		if token == '':
			continue
		if token[-1] == '.' and token not in abbr:
			token = token[:-1] + '\n.'
		 
		output.append(token)
	return '\n'.join(output)

line = sys.stdin.readline()
while line != '':
	print(tokenise(line.strip('\n'), abbr))
	line = sys.stdin.readline()







