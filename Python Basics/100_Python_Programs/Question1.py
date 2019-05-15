###----------------------------------------#
##Question 1
##Level 1
##
##Question:
##Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
##between 2000 and 3200 (both included).
##The numbers obtained should be printed in a comma-separated sequence on a single line.
##
##Hints: 
##Consider use range(#begin, #end) method

## Method 1
for i in range(2000,3201):
    if i%7 == 0 and i%5 !=0:
        print(i,end=',')
## Method 2
mul = [ i for i in range(2000,3201) if i%7 ==0 and i%5 != 0]
for i in mul:
    print(i,end=',')

## Method 3
def rangedivider(x,y):
    for i in range(x,y+1):
         if i%7 == 0 and i%5 !=0:
             print(i,end=',')

def main():
    rangedivider(2000,3201)

if __name__ == '__main__':
    main()


        
