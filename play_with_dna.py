'''
Play With Dna
author: Jeff Wakeman
https://www.codeeval.com/open_challenges/126/


only partially correct at the moment....
'''

import sys

def getNumMatching(a,b):
	matches = 0;
	for i,x in enumerate(a):		
		if x == b[i]: matches += 1;
	return matches;

def getMatches(segment,n,string):
	s = len(segment);
	r = len(string) - s + 1;
	matchLists = []; 
	for i in range(0,s): matchLists.append([]);
	
	#list of all sub-strings were comparing the segment to
	subs = [string[i:i+s] for i in range(0,r)];
	for x in subs:
		m = getNumMatching(segment,x);
		print (segment,x,'needed='+str(s-n),'matches='+str(m),m>=s-n);
		if (m >= s-n): matchLists[m-1].append(x);
		else: continue;
		
	#sort by best match (duplicate matches in alphabetical)
	output = [];
	matchLists.reverse();
	for l in matchLists:
		l.sort();
		output += l;
	return output;

test_cases = open(sys.argv[1],'r');
for test in test_cases:
	input = test.strip().split(' ');
	a = input[0];
	b = int(input[1]);
	c = input[2];
	m = getMatches(a,b,c);

	if (len(m) > 0): print(' '.join(m));
	else: print ('No match');

test_cases.close();