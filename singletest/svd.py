from numpy import *

def test():
	Base = array([[1.92028349427775,0.938200267748656,8.61139811393332,6.71431139674026,3.47712671277525,2.62145317727807,2.42785357820962,3.59228210401861],[1.38874202829155,5.25404403859336,4.84853333552102,7.41257943454207,1.49997253831683,0.444540922782385,4.42402313001943,7.36340074301202],[6.96266337082995,5.30344218392863,3.93456361215266,5.20052467390387,5.86092067231462,7.54933267231179,6.87796085120107,3.94707475278763]])
	U, S, V = linalg.svd(Base) 
	print U
	print '----'
	print S
	print '----'
	print V

if __name__=='__main__':
	test()