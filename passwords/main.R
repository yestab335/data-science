# Install and load the required packages
install.packages(c("ggformula", "mosaic", "ggplot2", "supernova", "coursekata"))
library(ggformula)
library(mosaic)
library(ggplot2)
library(supernova)
library(coursekata)

# View the structure of the passwords data frame
str(passwords)

# Compare password category to its respected strength
gf_boxplot(strength ~ category, data = passwords) %>%
  gf_labs(title = "Figure 1. Password Categories and their Strengths")

gf_histogram( ~ strength, data = passwords) %>%
  gf_facet_grid(category ~ .) %>%
  gf_labs(title = "Figure 2. Password Categories and their Strengths")

# Filter all values above 10 in `strength`
strenths.filtered <- filter(passwords, strength %in% c(1:10))

gf_bar(~ category, data = strenths.filtered) %>%
  gf_facet_grid(strength ~ .) %>%
  gf_labs(title = "Figure 3. Password Categories and their Strengths Filtered")

gf_jitter(strength ~ category, data = strenths.filtered) %>%
  gf_labs(title = "Figure 4. Password Categories and their Strengths Filtered")
