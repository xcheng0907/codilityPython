def solution(A, K):
    # write your code in Python 2.7
    A = list(A)
    if K<0:
        print "Error: Array must not be empty, and K must be nonnegative!"
        return -1
    if len(A)==0:
		return A
		
    K = K % len(A)
    
    return( A[-K:] + A[:-K] )
    
    
    
def main():
	l = range(5)
	print "l:    ", l
	print "l->1: ", solution(l, 1)
	print "l->2: ", solution(l, 2)


if __name__ == "__main__":
	main()
