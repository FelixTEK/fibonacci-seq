fib = 0 #fibonacci number
fibseq = [] #fibonacci sequence
seqamt = 0 #sequence amount
def fibonacci(seqamt):
    global fib, fibseq
    fibseq.append(fib)
    fib = 1
    seqamt = int(input())
    for i in range(seqamt):
        if len(fibseq) >= 2:
            fib = fibseq[(len(fibseq)-2)]+fibseq[(len(fibseq)-1)]
            fibseq.append(fib)
        else:
            fibseq.append(fib)
    
    print(fib%(10**9+7))
        
if __name__ == "__main__":
    fibonacci(seqamt)