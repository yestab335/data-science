# GLM MODEL:
#   Yi = b_0 + b_1(X_i) + e_i

# Linear model
linearModel <- lm(strength ~ category, data = passwords.filtered)
linearModel

# Filters all passwords ranked with '2' and subsets into new data frame
strongPassword <- subset(passwordStrengths, strength == 2)


strongPasswordLinearModel <- lm(strength, data = strongPassword)
