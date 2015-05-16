''' 
 https://www.codeeval.com/open_challenges/1/ 
 '''

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test.strip() != '': 
	
		inputs = test.split();
		x = int(inputs[0]);
		y = int(inputs[1]);
		n = int(inputs[2]);
		outputs = [];
		
		for i in range(n):
			out = '';
			if (i + 1)  % x == 0: out = 'F';
			if (i + 1) % y ==0: out += 'B';
			if out == '': out = (i+1);
			outputs.append(str(out));
		
		print ' '.join(outputs);
		
test_cases.close()