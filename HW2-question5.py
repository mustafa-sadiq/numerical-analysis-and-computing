import numpy as np

print("Mustafa Sadiq (ms3035)")
print("Answer to question 5")
print("--------------------\n")

def horners (poly, n, t):
    answer = poly[n]
    derivative = 0
    for i in range(0, n):
        derivative = answer + t * derivative
        answer = poly[n - 1 - i] + t * answer
    return answer, derivative

print ("p(t) = -1 + 2t - 6t^2 + 2t^3, t0 = 3")
poly = np.array([-1, 2, -6 , 2])
n = len(poly) - 1
t = 3
result, derivative = horners (poly, n, t)
print ("p(t0) =", result) #5
print ("p'(t0) =", derivative) #20

print("\n")

print ("p(t) = 1 + 3t + 0t^2 + 2x^3, t0 = 2")
poly = np.array ([1, 3, 0, 2])
n = len(poly) - 1
t = 2
result, derivative = horners (poly, n, t)
print ("p(t0) =", result) #23
print ("p'(t0) =", derivative) #27
