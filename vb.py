import string
#Library Functions
def rangestr(inpstr,sta,sto):
	inpstr=str(inpstr)
	sta=int(sta)
	if (len(inpstr)<=0):
		return ""
	ret=""
	for i in range(sta,sto+1):
		ret+=inpstr[i]
	return ret
def right(inpstr,count):
	inpstr=str(inpstr)
	count=int(count)
	length=len(inpstr)
	if (count==0):
		return ""
	if (count<0):
		print("Count could not be nagetive")
		return None
	if (length < count):
		print("String's length is less than the count")
		return None
	else:
		ret=""
		for i in range(length-count,length):
			ret+=inpstr[i]
		return ret

def left(inpstr,count):
	inpstr=str(inpstr)
	count=int(count)
	length=len(inpstr)

	if (count==0):
		return ""
	if (count<0):
		print("Count could not be nagetive")
		return None
	if (length < count):
		print("string's length is less than the count")
		return None
	else:
		ret=""
		for i in range(0,count):
			ret+=inpstr[i]

	return ret
def trim(inpstr):
	inpstr=str(inpstr)
	inpstr=inpstr.lstrip()
	inpstr=inpstr.rstrip()
	return inpstr
def replace(inpstr,originstr,replacestr):
	inpstr=str(inpstr)
	originstr=str(originstr)
	replacestr=str(replacestr)
	return inpstr.replace(originstr,replacestr)
def isnumeric(inpstr):
	inpstr=str(inpstr)
	return inpstr.isnumeric()