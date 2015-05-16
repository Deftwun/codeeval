'''
https://www.codeeval.com/open_challenges/179/
'''

import sys

#0 - 9
bitStrings = ['11111100','01100000','11011010' ,'11110010' ,'01100110',
					'10110110',	'10111110','11100000', '11111110','11110110']

def codifyDecimal(s):
	decimalSet = False; codes = [];
	for c in s.strip():
		if c == '.' : 
			decimalSet = True; 
			codes[-1]  = addOne(codes[-1]);
		else: codes.append(bitStrings[int(c)]);
	if not decimalSet: codes[-1] = addOne(codes[-1]);
	return codes;		
	
def addOne(s):
	return '{0:03b}'.format(int(s,2) + 1);

def compareBits(bits,mask): 
	return int(bits,2) & int(mask,2) == int(bits,2);

def willDisplay(display,number):
	index = 0;
	success = False;
	for index in range(0,len(display)-len(number)+1):
		subrange = display[index:index + len(number)];
		for i in range(0,len(subrange)):
			success = compareBits(number[i],subrange[i]);
			if not success: break; 
		if success: break;
	return int(success);

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	input = test.split(';');
	displayBits = input[0].split(' ');
	numberBits = codifyDecimal(input[1]);
	print(willDisplay(displayBits,numberBits));
	