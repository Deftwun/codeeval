'''
https://www.codeeval.com/open_challenges/158/
'''
import sys

test_cases = open(sys.argv[1], 'r');
for test in test_cases:
	if (test.strip() == ''): continue;
	test = test.split('|');
	inputs = test[0].split();
	iterations = int(test[1]);
	
	for i in range(0,iterations):
		isSorted = True;
		for j in range(0,len(inputs) - 1 - i):
			if int(inputs[j+1]) < int(inputs[j]):`
				isSorted = False;
				inputs[j],inputs[j+1] = inputs[j+1],inputs[j];
				
		if isSorted == True: break;
	print(' '.join(inputs));
test_cases.close()
