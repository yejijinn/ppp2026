import math

print("각도  /  라디안  /  sin  /  cos  /  tan")
print("-" * 40)

for deg in range(0, 91):
    r = math.radians(deg)    
    s = math.sin(r)
    c = math.cos(r)
    t = math.tan(r)

    print(f"{deg}  /  {r:.4f}  /  {s:.4f}  /  {c:.4f}  /  {t:.4f}")