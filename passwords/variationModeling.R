# GLM MODEL:
#   Y_i = b_0 + b_1(X_i) + e_i
#   Bad_Password_i = B_0 + b_1 (category_i) + e_i

# Empty linear model
empty_linearModel <- lm(strength ~ NULL, data = passwords.filtered)
empty_linearModel

# Regression model
passwords_model <- lm(strength ~ category, data = passwords.filtered)
passwords_model

# Predictions based off of the regression model `password_model`
passwords.filtered$predictions <- predict(passwords_model)
head(passwords.filtered)

# Visual representation of both models
gf_point(strength ~ category, data = passwords.filtered) %>%
  gf_model(passwords_model, color = "orange") %>%
  gf_model(empty_linearModel, color = "blue") %>%
  gf_labs(title = "Figure 9. Password Modeling with Linear (blue) and Regression (orange) Models")

# Filters all passwords ranked with '2' and subsets into new data frame
strongPassword <- subset(passwordStrengths, strength == 2)

strongPasswordLinearModel <- lm(strength ~ NULL, data = strongPassword)
strongPasswordLinearModel

# Anova tables
supernova(empty_linearModel)

# More details within the table itself
supernova(passwords_model)
