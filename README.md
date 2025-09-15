# FDE
Coding sample
# Thoughtful Robotic Package Sorting

This project implements a Python function to sort packages in a robotic automation factory based on their **volume** and **mass**. Packages are dispatched to different stacks according to their size and weight, following the rules provided.

## Table of Contents
- [Objective](#objective)
- [Rules](#rules)

## Objective

The goal is to write a function for a robotic arm that dispatches packages to the correct stack:

- **STANDARD**: packages that are neither bulky nor heavy.
- **SPECIAL**: packages that are either bulky or heavy.
- **REJECTED**: packages that are both bulky and heavy.

## Rules

- **Bulky**: a package is bulky if  
  - `volume >= 1,000,000 cm³` **or**  
  - any dimension >= 150 cm
- **Heavy**: a package is heavy if  
  - `mass >= 20 kg`

