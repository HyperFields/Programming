import sys
def AddTwo(n1,n2):
	print n1+n2
	return n1+n2

args=sys.argv
print args
AddTwo(args[1],args[2])
#print AddTwo(1,1)
