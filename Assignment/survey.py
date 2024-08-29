import statistics as stats
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

ratings = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

frequency = Counter(ratings)
print("Frequency of each rating:")
for rating, count in sorted(frequency.items()):
    print(f"Rating {rating}: {count}")

print("\nStatistical Measures:")
print(f"Minimum: {min(ratings)}")
print(f"Maximum: {max(ratings)}")
print(f"Range: {max(ratings) - min(ratings)}")
print(f"Mean: {np.mean(ratings):.2f}")
print(f"Median: {np.median(ratings)}")
print(f"Mode: {stats.mode(ratings)}")
print(f"Variance: {np.var(ratings, ddof=1):.2f}")
print(f"Standard Deviation: {np.std(ratings, ddof=1):.2f}")

total_responses = len(ratings)
percentages = {rating: (count / total_responses) * 100 for rating, count in frequency.items()}

plt.bar(frequency.keys(), frequency.values(), color='skyblue', alpha=0.7, edgecolor='black')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.title('Frequency of Product Ratings')

for rating, count in frequency.items():
    plt.text(rating, count, f'{percentages[rating]:.1f}%', ha='center', va='bottom')

plt.show()
