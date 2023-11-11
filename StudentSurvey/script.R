# Imports the StudentSurvey data set from the Lock5Data library
install.packages('Lock5Data')
library(Lock5withR)
install.packages("ggformula")
install.packages("mosaic")

str(StudentSurvey)
data(StudentSurvey)

gf_histogram(~ SAT, data = StudentSurvey, color = "gray", fill = "springgreen") %>%
  gf_labs(title = "Figure 1. Distribution of SAT Scores", x = "SAT Score") %>%
  gf_density()

favstats(~ SAT, data = StudentSurvey)
