marks = float(input())

if marks < 0 or marks > 100 :
    print('Invalid Input')
    
else:
    if marks >= 90:
        print("Garde : O" )
        
    elif marks >= 80 and marks < 90:
        print("Grade : A")
        
    elif marks >= 70 and marks < 80:
        print("Grade : B")
        
    elif marks >= 60 and marks < 70:
        print("Grade : C ")
        
    elif marks >= 35 and marks < 60:
        print("Grade : D")
        
    else:
        print("Fail")
    