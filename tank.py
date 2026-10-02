inflow=10
outflow=6
initial_level=50
time_steps=30
levels=[]
level=initial_level

for t in range(time_steps):
    level=level+(inflow-outflow)
    levels.append(level)