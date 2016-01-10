#calculator
#python doesnt have switch case

print "which operation you want"
print "1=add 2=sub 3=mul 4=div"
a=input('enter operation:')		#take operation

print "enter first no..."
b=input('1st no:')      #take 1st num
print "enter second no..."
c=input('2nd no:')		#take 2nd num

print "answer is::"

#elseif lader and print answer
if a==1:
	d=b+c
	print d
elif a==2:
	d=b-c
	print d
elif a==3:
	d=b*c
	print d
elif a==4:
	d=b/c
	print d
else:
	print "no operation match"
	