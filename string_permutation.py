'''
String Permutations solution
author: Jeff Wakeman
https://www.codeeval.com/open_challenges/14/
'''

import sys
	
def permute(input,start):
	output = set();
	for i in range(start,len(input)):
		for j in range(start,len(input)):
			chars = list(input);
			chars[i],chars[j] = chars[j],chars[i];
			s = ''.join(chars);
			output.add(s);
			perm = permute(s,i+1);
			for o in perm:
				output.add(o);
	return output;
	
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	input = test.strip();
	output = list(permute(input,0));
	output.sort();
	print(','.join(output));
	