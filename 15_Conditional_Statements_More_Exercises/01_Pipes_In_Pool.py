v = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

pipe1 = p1 * hours
pipe2 = p2 * hours
pool_fullment = pipe1 + pipe2  # общо литри

if pool_fullment <= v:
    pool_percent = (pool_fullment / v) * 100
    pipe1_percent = (pipe1 / pool_fullment) * 100
    pipe2_percent = (pipe2 / pool_fullment) * 100

    print(
        f"The pool is {pool_percent:.2f}% full. "
        f"Pipe 1: {pipe1_percent:.2f}%. "
        f"Pipe 2: {pipe2_percent:.2f}%."
    )
else:
    litres_more = pool_fullment - v
    print(f"For {hours:.2f} hours the pool overflows with {litres_more:.2f} liters.")