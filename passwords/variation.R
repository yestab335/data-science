# Removed unspecified data from data set for the topic focus
passwords.filtered <- strenths.filtered[-c(7,9)]

# Initial exploration of the variation in the data set using a bar graph
gf_bar( ~ category, data = passwords.filtered, fill = ~strength) %>%
  gf_labs(title = "Figure 5. Categorical count")

# Facet the graph between category and strength to compare
gf_bar( ~ category, data = passwords.filtered, fill = ~strength) %>%
  gf_labs(title = "Figure 6. Categorial comparization to strengths") %>%
  gf_facet_grid(strength ~ .)

# Layer a jitter plot on a box plot to get a better sense of the variation
gf_boxplot(strength ~ category, data = passwords.filtered) %>%
  gf_jitter(height = 0, color = "orange", alpha = 0.5) %>%
  gf_labs (title = "Figure 7. Password strength and category with specified values")

# Viewing new data set for better compareation
str(passwordStrengths)

# Graph is not being produced. `Error: Formula too large. I'm looking for NULL`
gf_histogram( ~ strength | strength, data = passwordStrengths, fill = ~strength)
