###############
# Create Signalling Game Simulation Plots
# Christopher Gandrud
# 4 December 2012
# Depends on Python 2.7.2 
###############

# Change working directory
setwd("/git_repositories/ContainmentGame/")

# Load Packages
library(ggplot2)

# Run game and simulate data
system('python /git_repositories/ContainmentGame/ContainmentGame1.py')

# Import simulated data
Sims <- read.csv("SimulatedData/SimData.csv")

# Create signaller combinations
Sims$Signalers[Sims$Signaler1 == -0.1 & Sims$Signaler2 == 0.1] <- "-0.1, 0.1"
Sims$Signalers[Sims$Signaler1 == -0.1 & Sims$Signaler2 == 0.2] <- "-0.1, 0.2"
Sims$Signalers[Sims$Signaler1 == -0.2 & Sims$Signaler2 == 0.1] <- "-0.2, 0.1"
Sims$Signalers[Sims$Signaler1 == -0.2 & Sims$Signaler2 == 0.2] <- "-0.2, 0.2"

#### Graph Utilities ####
# PM's Utility
ggplot(Sims, aes(x = Omega, y = Upm)) +
        facet_grid(~Signalers) +
        geom_point(color = "#B2DF8A") +
        scale_x_continuous(breaks = c(0.0, 0.4, 0.8), labels = c(0, 0.4, 0.8)) +
        scale_y_continuous(breaks = c(0.0, -0.05, -0.1, -0.15), labels = c(0, -0.05, -0.1, -0.15)) +
        xlab("\n Omega") + ylab("Prime Minister's Utility \n") +
        ggtitle("Prime Minister's Utility \n at various levels of Omega and Signaler Preferences \n") +
        theme_bw(base_size = 15)

# S1's Utility
ggplot(Sims, aes(x = Omega, y = Us1)) +
  facet_grid(~Signalers) +
  geom_point(color = "#1F78B4") +
  scale_x_continuous(breaks = c(0.0, 0.4, 0.8), labels = c(0, 0.4, 0.8)) +
  xlab("\n Omega") + ylab("Signaler 1's Utility \n") +
  ggtitle("Signaler 1's Utility \n at various levels of Omega and Signaler Preferences \n") +
  theme_bw(base_size = 15)

# S2's Utility
ggplot(Sims, aes(x = Omega, y = Us2)) +
  facet_grid(~Signalers) +
  geom_point(color = "#A6CEE3") +
  scale_x_continuous(breaks = c(0.0, 0.4, 0.8), labels = c(0, 0.4, 0.8)) +
  xlab("\n Omega") + ylab("Signaler 2's Utility \n") +
  ggtitle("Signaler 2's Utility \n at various levels of Omega and Signaler Preferences \n") +
  theme_bw(base_size = 15)