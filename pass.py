#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Define the Ukrainian alphabet in order
ukrainian_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
alphabet_mapping = {char: i+1 for i, char in enumerate(ukrainian_alphabet)}

# ASCII printable characters (character code 32-126)
# Codes 32-127 are common for all the different variations of the ASCII table, they are called printable characters, 
# represent letters, digits, punctuation marks, and a few miscellaneous symbols. 
# You will find almost every character on your keyboard. 
# Character 127 represents the command DEL.

# DEC   HEX Symbol  DEC HEX Symbol  DEC HEX Symbol  DEC HEX Symbol  DEC HEX Symbol  DEC HEX Symbol
# 32	20	space   48  30	0       64  40	@       80	50	P       96	60	`       112	70	p
# 33	21	!       49  31	1       65	41	A       81	51	Q       97	61	a       113	71	q
# 34	22	"       50	32	2       66	42	B       82	52	R       98	62	b       114	72	r
# 35	23	#       51	33	3       67	43	C       83	53	S       99	63	c       115	73	s
# 36	24	$       52	34	4       68	44	D       84	54	T       100	64	d       116	74	t
# 37	25	%       53	35	5       69	45	E       85	55	U       101	65	e       117	75	u
# 38	26	&       54	36	6       70	46	F       86	56	V       102	66	f       118	76	v
# 39	27	'       55	37	7       71	47	G       87	57	W       103	67	g       119	77	w
# 40	28	(       56	38	8       72	48	H       88	58	X       104	68	h       120	78	x
# 41	29	)       57	39	9       73	49	I       89	59	Y       105	69	i       121	79	y
# 42	2A	*       58	3A	:       74	4A	J       90	5A	Z       106	6A	j       122	7A	z
# 43	2B	+       59	3B	;       75	4B	K       91	5B	[       107	6B	k       123	7B	{
# 44	2C	,       60	3C	<       76	4C	L       92	5C	\       108	6C	l       124	7C	|
# 45	2D	-       61	3D	=       77	4D	M       93	5D	]       109	6D	m       125	7D	}
# 46	2E	.       62	3E	>       78	4E	N       94	5E	^       110	6E	n       126	7E	~
# 47	2F	/       63	3F	?       79	4F	O       95	5F	_       111	6F	o       127	7F	DEL

MIN_PRINTABLE_ASCII = 32    #" " — whitespace
MAX_PRINTABLE_ASCII = 126   #"~" — tilda

def process_text(input_text):

    max_code = MAX_PRINTABLE_ASCII-MIN_PRINTABLE_ASCII

    # Process the text to replace letters with ASCII symbols, applying overflow first
    lines = input_text.split('\n')
    processed_lines = []
    p=0
    for line in lines:
        processed_line = []
        for i, char in enumerate(line):
            if char.upper() in alphabet_mapping:
                p=p+1
                # Calculate the position score with overflow
                a = alphabet_mapping[char.upper()]
                position_score = (a * (p)) % max_code
                # Adjust the score by adding START_CODE
                final_score = position_score + MIN_PRINTABLE_ASCII
                # Convert the final score to its ASCII symbol
                ascii_symbol = chr(final_score)
                processed_line.append(ascii_symbol)

                # Print calculated values for debuging:
                #print(char+"="+ str(a)+"*"+str(p)+"%"+ str(max_code) +"="+str(position_score)+ " +"+str(MIN_PRINTABLE_ASCII)+"="+str(final_score)+ " " + ascii_symbol)

        processed_lines.append(''.join(processed_line))
    return '\n'.join(processed_lines)

# Assuming the input text is read from 'input.txt' and written to 'output.txt'
try:
    # Read from input.txt
    with open('input.txt', 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Process the text
    processed_text = process_text(input_text)

    # Write to output.txt
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(processed_text)

    print("Process completed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
