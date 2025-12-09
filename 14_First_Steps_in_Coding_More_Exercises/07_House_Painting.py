house_height = float(input())
length_side_wall = float(input())
height_triangle_wall_on_roof = float(input())

front_and_back_walls = 2 * (house_height * house_height) - (1.2 * 2)
side_walls = 2 * (house_height * length_side_wall) - 2 * (1.5 * 1.5)
roof_area = 2 * (house_height * length_side_wall) + 2 * ((house_height * height_triangle_wall_on_roof) / 2)

total_green_paint_litres = (front_and_back_walls + side_walls) / 3.4
total_red_paint_litres = roof_area / 4.3

print(f"{total_green_paint_litres:.2f}")
print(f"{total_red_paint_litres:.2f}")