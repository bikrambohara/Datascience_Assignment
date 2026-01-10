import random
random.seed(4090)
data =[random.randint(30, 100) for i in range(50)]
#mean, median, quartile, range, quartiles, iqr
print(data)

def mode(data):
    frequency = {}
    for i in data:
        frequency[i] = frequency.get(i,0) + 1
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency[0][0]


def mean(data):
    total = 0
    n = len(data)
    for i in data:
        total += i
    return total / n

def median(data):
    data.sort()
    n = len(data)
    if(n % 2 == 0):
        median = (data[int((n)/2)] + data[int((n-1)/2)])/2
    else:
        med_term = int((n-1)/2)
        print(med_term)
        median = data[med_term]
    return median

def quartile(data, n):
    data.sort()
    length = len(data)
    q_term = (length-1) * n/4
    term = int(q_term)
    dec = q_term - term
    # print(f"Data: {s_data} | Q_term: {q_term} | Term: {term}")
    if dec != 0:
        q = data[term] + dec * (data[term+1] - data[term])
    else:
        q = data[term]
    return q

def median(data):
    return quartile(data, 2)


mean = mean(data)
median = median(data)
mode = mode(data)
ranges = max(data) - min(data)
q1 = quartile(data, 1)
q2 = quartile(data, 2)
q3 = quartile(data, 3)
iqr = q3 - q1


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Mode: {ranges}")
print(f"Quartile 1: {q1}")
print(f"Quartile 2: {q2}")
print(f"Quartile 3: {q3}")
print(f"Interquartile range: {iqr}")