###直角三角形，共5行。第1行，1颗星*，第2行，2颗星*，第5行，5颗星*
A = 0
while A < 6 :
    B = 1
    while B <= A:
        print ('*',end='\t')
        B += 1
    print('')    
    A +=1