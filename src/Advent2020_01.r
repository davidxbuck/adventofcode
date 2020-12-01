library(gtools)
library(tibble)
library(dplyr)
library(stringr)
inp <- paste(readLines('~/Documents/CodeRepositories/AdventofCode/inputs2020/Advent2020_01.txt'), collapse = ",")
inp <- strsplit(inp, split = ",")
inp <- as.integer(inp[[1]])

combos <- as_tibble(gtools::combinations(n = 200, r = 2, v = inp, repeats.allowed = FALSE))
combos <- combos %>%
  rowwise() %>%
  mutate(total = sum(c(V1, V2))) %>%
  filter(total == 2020) %>%
  mutate(product = V1 * V2)

print(stringr::str_interp("AoC 2020 Day 1, Part 1 answer is (${V1}, ${V2}) is ${product}", combos[1,]))

combos <- as_tibble(gtools::combinations(n = 200, r = 3, v = inp, repeats.allowed = FALSE))
combos <- combos %>%
  rowwise() %>%
  mutate(total = sum(c(V1, V2, V3))) %>%
  filter(total == 2020) %>%
  mutate(product = V1 * V2 * V3)

print(stringr::str_interp("AoC 2020 Day 1, Part 2 answer is (${V1}, ${V2}, ${V3}) is ${product}", combos[1,]))
