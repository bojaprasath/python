# list = [1]
# for i in range(10):
#     print(list)
#     newlist = []
#     newlist.append(list[0])
#     for i in range(len(list) - 1):
#         newlist.append(list[i] + list[i + 1])
#     newlist.append(list[-1])
#     list = newlist


height = int(10)

def pascal(h, nums): # Height and array of current triangle
  if h == 1: # finished!
    return nums

  next_row = [1]# Start row

  # Iterate through the last row
  for i in range(len(nums[-1]) - 1):
    # Append each item in the last row addded to the item on the right
    next_row.append(nums[-1][i] + nums[-1][i + 1])

  next_row.append(1) # End row

  nums.append(next_row) # Add row to triangle

  return pascal (h - 1, nums) # Repeat at next row


# Start the recursion with the top of the triangle
triangle = pascal(height, [[1]])
print triangle
