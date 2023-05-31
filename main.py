
#-------------------------|
# NAND function
#-------------------------|
def NAND(a,b):
  
  if a == 1 and b == 1:
    return False
  else:
    return True
#-------------------------|
# main function
#-------------------------|
    
if __name__=="__main__":
#-------------------------|  
  #Truth Table
#-------------------------|
  print("--> False | OFF | 0" )
  print("--> True  | ON  | 1" )
  print( )
  print("-------------------------------------")
  print("|     Truth Table for NAND gate     |")  
  print("-------------------------------------")
  print("| A = False | B = False | X =",NAND(False,False)," | ")
  print("| A = False | B = True  | X =",NAND(False,True)," | ")
  print("| A = True  | B = False | X =",NAND(True,False)," | ")
  print("| A = True  | B = True  | X =",NAND(True,True),"| ")
  print("-------------------------------------")
#-------------------------|
  #Notes
#-------------------------|
  print( )
  print("* NAND gate output is FALSE only if both inputs are TRUE" )
#-------------------------|
  print( )
  print( )
a= int(input("Enter a value for input A (0,1): "));
b= int(input("Enter a value for input B (0,1): "));
print("Output X is:", NAND(a, b))