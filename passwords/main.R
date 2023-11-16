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
