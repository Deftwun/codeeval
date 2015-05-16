'''
https://www.codeeval.com/open_challenges/122/
'''

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.strip();
	hidden = 'abcdefghij';
	for c in test:
		if c in hidden: test = test.replace(c,str(hidden.find(c)));
		elif not c.isdigit(): test = test.replace(c,'');
	if (test == ''): test = 'NONE';
	print(test);
	
test_cases.close()
