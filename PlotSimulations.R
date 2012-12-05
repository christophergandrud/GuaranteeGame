###############
# Create Signalling Game Simulation Plots
# Christopher Gandrud
# 5 December 2012
# Depends on Python 2.7.2 
###############

# Change working directory
setwd("/git_repositories/ContainmentGame/")

# Load Packages
library(ggplot2)
library(gridExtra)

# Run game and simulate data
system('python /git_repositories/ContainmentGame/ContainmentGame2Signals.py')

# Import simulated data
Sims <- read.csv("SimulatedData/SimData.csv")

# Create signaller combinations
Sims$Signalers[Sims$Signaler1 == -0.05 & Sims$Signaler2 == 0.05] <- "-0.05, 0.05"
Sims$Signalers[Sims$Signaler1 == -0.05 & Sims$Signaler2 == 0.15] <- "-0.05, 0.15"
Sims$Signalers[Sims$Signaler1 == -0.15 & Sims$Signaler2 == 0.05] <- "-0.15, 0.05"
Sims$Signalers[Sims$Signaler1 == -0.15 & Sims$Signaler2 == 0.15] <- "-0.15, 0.15"

#### Graph Utilities ####

# Save plot
pdf('~/Dropbox/Ireland_Korea_Research/Paper/Figures/TwoSignalers.pdf', height = 11)


# Guarantee Decision (gk)
GuarPlot <- ggplot(Sims, aes(x = Omega, y = Guarantee)) +
              facet_grid(~Signalers) +
              geom_point(color = "#E41A1C") +
              scale_x_continuous(breaks = c(0.0, 0.425, 0.85), labels = c(0, 0.425, 0.85)) +
              scale_y_continuous(limits = c(0, 1), breaks = c(0.0, 0.2, 0.425, 0.6, 0.85, 1), 
                                 labels = c(0, 0.2, 0.425, 0.6, 0.85, 1)) +
              xlab("") + ylab("Guarantee Decision \n") +
              theme_bw(base_size = 15)

# PM's Utility
PMPlot <-ggplot(Sims, aes(x = Omega, y = Upm)) +
            facet_grid(~Signalers) +
            geom_point(color = "#4DAF4A") +
            scale_x_continuous(breaks = c(0.0, 0.425, 0.85), labels = c(0, 0.425, 0.85)) +
            scale_y_continuous(breaks = c(0.0, -0.025, -0.075), labels = c(0, -0.025, -0.075)) +
            xlab("") + ylab("Prime Minister's Utility \n") +
            theme_bw(base_size = 15)

# S1's Utility
S1Plot <- ggplot(Sims, aes(x = Omega, y = Us1)) +
            facet_grid(~Signalers) +
            geom_point(color = "#1F78B4") +
            scale_x_continuous(breaks = c(0.0, 0.425, 0.85), labels = c(0, 0.425, 0.85)) +
            scale_y_continuous(breaks = c(0.00, -0.1, -0.2), labels = c(0, -0.1, -0.2)) +
            xlab("") + ylab("MoF's Utility \n") +
            theme_bw(base_size = 15)

# S2's Utility
S2Plot <- ggplot(Sims, aes(x = Omega, y = Us2)) +
            facet_grid(~Signalers) +
            geom_point(color = "#A6CEE3") +
            scale_x_continuous(breaks = c(0.0, 0.425, 0.85), labels = c(0, 0.425, 0.85)) +
            scale_y_continuous(breaks = c(0.00, -0.1, -0.2), labels = c(0, -0.1, -0.2)) +
            xlab("\n omega") + ylab("FR's Utility \n") +
            theme_bw(base_size = 15)


# Combine the Graphs
grid.arrange(GuarPlot, PMPlot, S1Plot, S2Plot, nrow = 4)

dev.off()