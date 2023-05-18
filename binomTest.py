# from scipy.stats import binom_test

# # Observed counts
# observed_fatal_april20 = 340
# observed_nonfatal_april20 = 353

# # Combined counts from April 13 and April 27
# combined_fatal_control = 253 + 255
# combined_nonfatal_control = 307 + 296

# # Total counts for both groups
# total_fatal = observed_fatal_april20 + combined_fatal_control
# total_nonfatal = observed_nonfatal_april20 + combined_nonfatal_control

# # Hypothesized probability
# hypothesized_prob = 0.5

# # Perform the binomial test
# p_value = binom_test(observed_fatal_april20, total_fatal, hypothesized_prob)

# print("Binomial Test Results:")
# print("Observed Fatal Count (April 20):", observed_fatal_april20)
# print("Combined Fatal Count (April 13 + April 27):", combined_fatal_control)
# print("Total Fatal Count:", total_fatal)
# print("Hypothesized Probability:", hypothesized_prob)
# print("P-value:", p_value)

from scipy.stats import binomtest

observed_successes = 1390
total_trials = 1390 + 1047
hypothesized_probability = (1257 + 1205) / (1257 + 962 + 1205 + 963)

print(hypothesized_probability)

p_value = binomtest(observed_successes, total_trials, hypothesized_probability)
print("p-value for treatment group (April 20):", p_value)

p_value = binomtest(observed_successes, total_trials, hypothesized_probability, alternative='greater')
print("p-value for treatment group (April 20):", p_value)

p_value = binomtest(observed_successes, total_trials, hypothesized_probability, alternative='less')
print("p-value for treatment group (April 20):", p_value)
