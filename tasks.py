# Task #3.1 Write a code that takes an array and returns the second largest element of it.
# 
# arr = []
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = int(input())
#     arr.append(ele)                      
# mx = arr[0]
# secondmax = 0
# n = len(list)
# for i in range(1,n):
#     if arr[i] > mx:
#         secondmax = mx
#         mx = arr[i]
#     elif arr[i] > secondmax and mx != arr[i]:
#         secondmax = arr[i]
#     elif mx == secondmax and secondmax != arr[i]:
#           secondmax = arr[i]
 
# print("Second highest number is :",str(secondmax))

#Task #3.2
# --------------------------------------------------------------------------------------------------------------------------------
# 
# def second_largest(arr):
#     arr.sort()
#     for i in range(len(arr)-2, 0, -1):
#         if arr[i] != arr[i - 1]:
#             return arr[i]
      
# arr = []
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = int(input())
#     arr.append(ele) 
# print("The second largest element is: {0}".format((second_largest(arr))))


#----------------------------------------------------------------------------------------------------------------------------------------------------------


#Task #4 Write a code that takes a lowercase string and returns the first non-repeating character 

# def first_non_repeating_character(massage):
#     ctr = {}
#     for i in range (len(massage)):
#         if massage[i] not in ctr:
#             ctr[massage[i]] = 1     
#         else:
#             ctr[massage[i]] += 1
#     for c in ctr.keys():
#         if ctr[c] == 1:
#             return c
# string = "eeemu"
# print(first_non_repeating_character(string))