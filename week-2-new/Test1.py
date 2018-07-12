d1={'a':".-",'b':"-...",'c' :"-.-.",'d' :"-..",'e':".",'f' :"..-.",'g' :"--.",'h' :"....",'i':"..",'j':".---",'k':"-.-",
'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",
'x' :"-..-",'y' :"-.--",'z' :"--.."}

def transform(a):
	d2 = {}
	for i in range(0,len(a)):
		s = a[i]
		s1=""
		for j in range(0,len(s)):
			s1 = s1 + d1.get(s[j])
		d2[s1] = 1
	return len(d2)

print(transform(['gin','zen','gig','msg']))
print(transform(['a','z','g','m']))
print(transform(['bhi','vsv','sgh','vbi']))
print(transform(['a','b','c','d']))
print(transform(['hig','sip','pot']))
