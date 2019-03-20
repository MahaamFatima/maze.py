#Q1find cube in python
number=float(input("Enter any numeric value: "))
cube=number**3
print("The cube of the given number {0} :{1}".format(number,cube))

#Q2programtofindafactorial
def factorial(number):
  if number==1:
   return 1
  else:
   return number*factorial(number-1)
output=factorial(4)
print(output) 

# Q3patterncount
def count_substring(string,sub_string):
count=0
for x in range(len(string)-len(sub_string)+1):
    if(string[x:x+len(sub_string)] == sub_string):
        count+=1
return count
count_substring('(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')) ')
count_substring(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f'))

#Q4 maze input
print("Enter no of rows and columns")
row=int(input("Enter the no of rows in a maze"))
column=int(input("Enter the no of column in a maze"))
m=[[int(input()) for x in range(column)] for y in range(row)]
print(m)

#Q5 matrix define
def pathfind(way):
  row=0
  column=0
  print("Path : ")

  while row<=4 and column<=6 and row>=0 and column>=0:
  
   if(column+1 <= 6 and way[row][column+1]==0   and column>=0  or way[row][column+1]==3):
        if(way[row][column+1]==3):
          print(print("Right :)"))
          break
        column=column+1  
        way[row][column]=2
        print("Right",end=(''))

   elif (way[row][column-1]==0 and row>=0 and column-1 >=0 or way[row][column-1]==3):
        if(way[row][column-1]==3):
          print(print("Left:)"))
          break
        column=column-1  
        way[row][column]=2
        print("Left",end=(''))

   elif way[row-1][column]==0 and row-1>=0 and column >=0 or way[row-1][column]==3:
         if(way[row-1][column]==3):
          print(print("Up:)"))
          break
         row=row-1 
         way[row][column]=2
         print("Up",end=(''))
         
   elif(way[row+1][column]==0 and row+1 <= 4 and column <=6 or way[row+1][column]==3):
         if(way[row+1][column]==3):
          print(print("Down:)"))
          break
         row=row+1 
         way[row][column]=2
         print("Down",end=(''))

pathfind(way)