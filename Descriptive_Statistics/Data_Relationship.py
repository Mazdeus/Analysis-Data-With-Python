import pandas as pd

sample_data = {
    'name': ['A', 'B', 'C', 'D', 'E'],
    'age': [20, 22, 21, 23, 24],
    'communation_skill_score': [5, 6, 7, 8, 9],
    'quantitative_skill_score': [6, 7, 8, 9, 10]
}

df = pd.DataFrame(sample_data)

print(df.corr(numeric_only=True))

# Covariance
print(df.cov(numeric_only=True))