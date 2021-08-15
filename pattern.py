height=int (input("Enter the height of the pattern:"))

if height <= 0: 
    print ("invalid entry!")
for i in range(height+1):
       
       
    for j in range(i+1-i):
        
        print(" *\t"*i,i,"\t","*\t"*i,end="")
      

    print("\r")