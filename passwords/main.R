install.packages("ggformula")
install.packages("mosaic")
install.packages("ggplot2")
install.packages("supernova")
library(ggformula)
library(mosaic)
library(ggplot2)
library(supernova)

# View the structure of the passwords data frame
str(passwords)

# Compare password category to its respected strength
gf_boxplot(strength ~ category, data = passwords) %>%
  gf_labs(title = "Figure 1. Password categories and their strengths")

gf_histogram( ~ strength, data = passwords) %>%
  gf_facet_grid(category ~ .) %>%
  gf_labs(title = "Figure 2. Password categories and their strengths")

# Filter all values above 10 in `strength`
strenths.filtered <- filter(passwords, strength %in% c(1:10))

gf_bar(~ category, data = strenths.filtered) %>%
  gf_facet_grid(strength ~ .) %>%
  gf_labs(title = "Figure 3. Password categories and their strengths filtered")

gf_jitter(strength ~ category, data = strenths.filtered) %>%
  gf_labs(title = "Figure 4. Password categories and their strengths filtered")
