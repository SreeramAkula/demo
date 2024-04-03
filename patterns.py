# #solid Rectangle
# rows=4
# col=6
# for i in range(rows):
#     for j in range(col):
#         print("*", end=" ")
#     print("") 



#Hallow Rectangle
# rows=5
# col=3
# for j in range(col):
#     for i in range(rows):
#         if (j==0) or (j==col-1) or (i==0) or (i==rows-1) :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# #Half Pyramid
# rows=5
# for i in range(rows):
#     for j in range(i+1):
#          print("*", end=" ")
#     print("")  




#Rev Half Pyramid
rows=5
for i in range(rows):
    for j in range(rows-i):
         print("*", end=" ")
    print("") 