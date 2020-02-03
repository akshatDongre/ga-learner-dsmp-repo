# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
print(df)

p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)

tp = len(df)
print(tp)
print('================')
dc = df['purpose'].value_counts()['debt_consolidation']
print(dc)
print('================')

p_b = dc / tp
print(p_b)

p_a_b = p_b / p_a
print(p_a_b)

df1 = df

result = p_a_b == p_a
print(result)


# code ends here


# --------------
# code starts here
prob_lp=((df[df['paid.back.loan']=='Yes'].count())/len(df)).loc['paid.back.loan']
print(prob_lp)
prob_cs=((df[df['credit.policy']=='Yes'].count())/len(df)).loc['credit.policy']
print(prob_cs)
new_df=df[df['paid.back.loan']=='Yes']
new_df.head()
prob_pd_cs=(((df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')]).count())/len(new_df)).loc['paid.back.loan']
print(prob_pd_cs)
bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)


# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind="bar")
df1 = df[df['paid.back.loan'] == 'No']
df.purpose.value_counts(normalize=True).plot(kind='bar')



# code ends here


# --------------
# code starts here

import statistics

inst_median = statistics.median(df['installment'])
print(inst_median)

inst_mean = np.mean(df['installment'])
print(inst_mean)

df['installment'].hist(normed = True, bins=50)

df['log.annual.inc'].hist(density = True, bins=50)

# code ends here


