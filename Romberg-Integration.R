install.packages("pracma")
library(pracma)


f <- function(x) 1/(1+2+x)
romberg(f, 0, 2)