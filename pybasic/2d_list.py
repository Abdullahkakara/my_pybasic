  # print(list_2[2][1]) # Ata use hoi konta kon raw and kon colume a ace ta dekar jonno
# print(len(list_2)) # ai print ta use hoi koita colume ace ta dekar jonno
# print(list_2[0]) #ata use particular row ar kon kon number ta dekar jonno

# print(len(list_2[3]))

list_2 = [[1,2,3],[4,5,6,10],[7,8,9],[11,12,13,14]]
num_of_rows = len(list_2)
for row in range(num_of_rows):
   col_size = len(list_2[row])
   for col in range(col_size):
      print(list_2[row][col])

