number_of_balls= int(input())
max_weight_of_the_ball=0
max_time_needed=0
max_quality=0
max_value=0

for ball_counter in range(number_of_balls):
    weight_of_the_ball = int(input())
    time_needed = int(input())
    quality = int(input())
    result = (weight_of_the_ball / time_needed) ** quality
    if result>max_value:
        max_weight_of_the_ball = weight_of_the_ball
        max_time_needed = time_needed
        max_quality = quality
        max_value = result
print(f"{max_weight_of_the_ball} : {max_time_needed} = {int(max_value)} ({max_quality})")
