import math
# Start off with the lists of the positiions of the 300 rectangles
num_rect = int(input("How many rectangles will you use: "))
# Interval is the interval divided by the number of rectangles
interval = 5 / num_rect
# Since we are starting at 0, we will make the range of the num of rectanglesstart at 0 and multiply it by the interval
positions_right = [interval * i for i in range(num_rect)]
# The positions on the right are starting at the interval, so we will make range start at 1
positions_left = [interval * i for i in range(1, num_rect + 1)]
# Finding the heights for the left rectangles, is just to find the y value at each interval

heights_left = [math.sqrt(16-((16*x**2)/25)) for x in positions_left]
# Finding the heights of the triangles that start on the right
heights_right = [math.sqrt(16-(16*x**2)/25) for x in positions_right]

# Finding the areas for each of the rectangles
# Getting the index and the height for each iteration and finding the position for that index and multiplying them
areas_l = [interval * height for height in heights_left]
# Areas to the right
areas_r = [interval * height for height in heights_right]

# The total areas are just the sum of all the rectangles in each list
total_area_left = sum(areas_l)
total_area_right = sum(areas_r)

print(total_area_left)
print(total_area_right)