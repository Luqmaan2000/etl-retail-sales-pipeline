# %%
#------------ Import Libraries ---------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

np.random.seed(42)
# %%
# ----------- Simulate A/B Test Dataset ------------------

n_users = 1000
groups = np.random.choice(['A','B'], size = n_users)

conversions = np.where(
    groups == 'A',
    np.random.binomial(1,0.12,size=n_users),
    np.random.binomial(1,0.15,size=n_users)
)

df=pd.DataFrame({
    'user_id': range(1,n_users + 1),
    'group': groups,
    'converted': conversions
})

# %%
# ----------- Summary & Conversion Rates -------------
summary = df.groupby('group')['converted'].mean().reset_index()
print('Conversion rates:\n', summary)
# %%
# ---------- Visualise conversion differences ------------

plt.figure(figsize=(10,6))
plt.bar(summary['group'],summary['converted'],linewidth=1.2, color = ['maroon','skyblue'])


plt.xlabel('Group')
plt.ylabel('Conversion Rate')

plt.title('Conversion Rate by Group')

plt.grid(axis='y',linestyle='--',alpha = 0.4)
plt.tight_layout()
plt.show()
# %%
# ------ Z - Test for proportions ----------
# %%
success = df.groupby('group')['converted'].sum().values
n_obs = df.groupby('group')['converted'].count().values

z_stat,p_val = proportions_ztest(count=success,nobs=n_obs,alternative='larger')

print("Z-statistic:", round(z_stat, 3))
print("P-value:", round(p_val, 4))

if p_val<0.05:
    print("Statistical significance: Group B outperforms Group A")
else:
    print("No strong evidence for improvement")
# %%
