import hashlib

# code = "❌❌❌❌❌❌❌❌"
# hej = "ffykfhsq"
# i = 0
# for inte_i in range(8):
# 	print(code)
# 	while 1:
# 		test = hashlib.md5((hej+str(i)).encode('utf-8')).hexdigest()
# 		i += 1
# 		if not int(test[:5],16):
# 			print(test[5], end="", flush=True)
# 			break

# print()


code = ["X","X","X","X","X","X","X","X",]
hej = "ffykfhsq"
i = 0
for inte_i in range(8):
	
	while 1:
		test = hashlib.md5((hej+str(i)).encode('utf-8')).hexdigest()
		#print(''.join(code) + '\t' + test, end='\r')
		i += 1
		if not int(test[:5],16):
			#print("😬")
			try:
				if code[int(test[5])] == 'X':
					code[int(test[5])] = test[6]
					print(''.join(code))
				else:
					1/0
			except Exception:
				pass
			else:
				break

