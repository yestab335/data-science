# Removed unspecified data from data set for the topic focus
passwords.filtered <- strenths.filtered[-c(7,9)]

# Initial exploration of the variation in the data set using a bar graph
gf_bar( ~ category, data = passwords.filtered, fill = ~strength) %>%
  gf_labs(title = "Figure 5. Categorical Count")

# Facet the graph between category and strength to compare
gf_bar( ~ category, data = passwords.filtered, fill = ~strength) %>%
  gf_labs(title = "Figure 6. Categorial Comparization to Strengths") %>%
  gf_facet_grid(strength ~ .)

# Layer a jitter plot on a box plot to get a better sense of the variation
gf_boxplot(strength ~ category, data = passwords.filtered) %>%
  gf_jitter(height = 0, color = "orange", alpha = 0.5) %>%
  gf_labs (title = "Figure 7. Password Strength and Aategory with Specified Values")

# Viewing new data set for better compareation
str(passwordStrengths)

# Since the sample size is too big for both R and the cloud Jupyter Notebook
# This code manipulates the sample size from 600,000+ observations to 800 observations
strongPasswordsSample <- sample_n(passwordStrengths, 800)

# Filters the new data frame sample to only select values that range from 0 - 2
strongPasswordsSample.filtered <- filter(strongPasswordsSample, strength %in% c(0:2))

# Produces the bar graph visual representation of the new sample size data frame
gf_bar( ~ strength, data = strongPasswordsSample.filtered, fill = ~strength) %>%
  gf_labs(title = "Figure 8. Password Variation in New Sampled Data Frame")
