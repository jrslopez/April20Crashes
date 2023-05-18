from scipy.stats import chi2_contingency

# Define the observed counts for each group
observed = [
    [543, 666],    # Treatment group (April 20): [fatal, non-fatal]
    [486, 645],     # Control group (April 13): [fatal, non-fatal]
    [458, 516]      # Control group (April 27): [fatal, non-fatal]
]

# Perform the chi-square test
chi2, p_value, dof, expected = chi2_contingency(observed)

# Compare the obtained p-value to the significance level
significance_level = 0.05

print('p value is:', p_value)
print(chi2)
