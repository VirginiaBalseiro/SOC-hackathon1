#build an array of arrays containing the continent where 0 is water and 1 is land
world = [
  [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#loop over each subarray and count all the 1s (land)
def continent_counter():
   indI = 0
   indJ = 0
   count = 0
   for i in range(indI, len(world)):
    for j in range (indJ, len(world[i])):
      if world[i][j] == 1:
        if world[i][j+1] != 1 | world[i][j-1] != 1 & world[i+1][j] != 1:            
          count = count
        else:
          count = count + 1
      else: 
        indI = world[i]
        indJ = world[i][j];
        return count
        continent_counter()

print(continent_counter())

#loop over the array and when you find a 1, check the tiles left, right, and below to see if they are also 1. If any of them indeed is 1, add +1 to count

#count = 0

#for i in range(len(world)):
#  for j in range (len(world[i])):
#    if world[i][j] ==1:
#        if world[i][(j+1)% len(world)] ==1 | world[(i+1)% len(world)][j] ==1 | world[(i+1)% len(world)][j-1] ==1 | world[(i+1)% len(world)][(j+1)% len(world)] ==1:
#            count = count + 1

#print(count)