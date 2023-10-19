# user input
v_pool_volume = int(input())
p1_first_pipe_volume = int(input())
p2_second_pipe_volume = int(input())
h_hours = float(input())

# logic
first_pipe_contributuion = p1_first_pipe_volume * h_hours
second__pipe_contributopn = p2_second_pipe_volume * h_hours
volume_filled = first_pipe_contributuion + second__pipe_contributopn

# code output
if v_pool_volume >= volume_filled:
    print(f"The pool is {volume_filled / v_pool_volume * 100:.2f}% full. "
          f"Pipe 1: {first_pipe_contributuion / volume_filled * 100:.2f}%. "
          f"Pipe 2: {second__pipe_contributopn / volume_filled * 100:.2f}%.")
else:
    print(f"For {h_hours} hours the pool overflows with {volume_filled - v_pool_volume} liters.")
