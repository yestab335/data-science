# Initial exploration of the variation in the dataset using a bar graph
gf_bar( ~ category, data = strenths.filtered, fill = ~strength) %>%
  gf_labs(title = "Figure 5. Categorical count")

# Facet the graph between category and strength to compare
gf_bar( ~ category, data = strenths.filtered, fill = ~strength) %>%
  gf_labs(title = "Figure 6. Categorial comparization to strengths") %>%
  gf_facet_grid(strength ~ .)