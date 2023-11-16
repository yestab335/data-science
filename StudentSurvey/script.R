# Imports the StudentSurvey data set from the Lock5Data library
install.packages('Lock5Data')
install.packages("ggformula")
install.packages("mosaic")
install.packages("ggplot2")
install.packages("supernova")
library(Lock5withR)
library(ggformula)
library(mosaic)
library(ggplot2)
library(supernova)

str(StudentSurvey)
data(StudentSurvey)

gf_histogram(~ SAT, data = StudentSurvey, color = "gray", fill = "springgreen") %>%
  gf_labs(title = "Figure 1. Distribution of SAT Scores", x = "SAT Score") %>%
  gf_density()

favstats(~ SAT, data = StudentSurvey)

# Explore the variation within the data frame
gf_point(SAT ~ GPA, data = StudentSurvey) %>%
  # Creates a blue line representing the median
  gf_lm() %>%
  gf_labs(title = "Figure 2. SAT Scores to GPA")

# Compare GPA to smoking students
gf_histogram(~ GPA, data = StudentSurvey) %>%
  gf_facet_grid(Smoke ~ .) %>%
  gf_labs(title = "Figure 3. GPA to Student Smokers")

# Creates and empty model and saves it into an R object called GPA_model
GPA_model <- lm(GPA ~ NULL, data = StudentSurvey)
GPA_model

# Saves the favstats of the variable GPA into an R object called GPA_stats
GPA_stats <- favstats(~ GPA, data = StudentSurvey)
supernova(GPA_model)

# Creates and empty model and saves it into an R object called SAT_model
SAT_model <- lm(SAT ~ NULL, data = StudentSurvey)
SAT_model

# Saves the favstats of the variable GPA into an R object called GPA_stats
SAT_stats <- favstats(~ SAT, data = StudentSurvey)
supernova(SAT_model)

gf_histogram(~ GPA, data = StudentSurvey) %>%
  gf_vline(xintercept = 3.158) %>%
  gf_labs(title = "Figure 4. Student GPA Model with Marked Average")

gf_histogram(~ SAT, data = StudentSurvey) %>%
  gf_vline(xintercept = 1204) %>%
  gf_labs(title = "Figure 5. Student SAT Model with Marked Average")
