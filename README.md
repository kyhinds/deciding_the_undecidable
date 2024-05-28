# deciding_the_undecidable

### Author: Kyle Hinds
### Date: April 20th, 2024

## Description

This project presents an exploration into Alan Turing's Halting Problem, providing a solution using ordinal arithmetic and trigonometric recursion. It builds on the principles of Turing machines, proposing a function H that correctly decidedes the expected behavior of Q at each recursive depth. This research is grounded in the paper included in this repo "Deciding The Undecidable" (Hinds, 2024).


## Features

- **Turing Machine Models (H and Q)**: Implements conceptual machines to explore halting problems and paradoxical behaviors.

- **Algebraic and Trigonometric Functions**: Uses mathematical models to simulate Turing machine states and transitions.

- **Example Functions (`halt` and `loop`)**: Demonstrate predictable machine behaviors with `halt` always stopping and `loop` endlessly running.

- **Experimental Functions (`q_inverse`, `h_arctan`, `h_sigmoid`)**: Provide tools for analyzing the inputs in a controlled, mathematical framework.

- **`qn_cot2_cos` and `qn_tan2_sin` and other trig funtions**: Model cyclical logic states through trigonometric recursion.

- **`halting_machine` with Iterative Depth**: Explores the recursive nature of nested Q calls, revealing outcomes across multiple iterations.

- **`complex_logic`**: Explores recursive complex valued boolean logic, and introduces 2 new complex logical operators.

## Installation

Ensure Python 3.8 or later is installed. Clone and enter the project directory:

git clone <git@github.com:kyhinds/deciding_the_undecidable.git>
cd _Halting_Machine_

## Usage

Run the script from the command line by specifying functions and parameters. Here are examples for each function:

python h.py halt 2.5 3.1  # Halts immediately with results based on inputs.
python h.py loop  # Loops indefinitely.
python h.py q_inverse 1 0 1 1  # Tests Q's inverse behavior.
python h.py qn_cot2 0 0 2 2  # Observes the cyclical behavior with cotangent squared.
python h.py halting_machine -1 0 1 -- 3  # Simulates halting analysis over multiple iterations.

## Contributions

Contributions to this project are welcome. You can contribute by:

- Improving the existing codebase with optimizations or extending functionality.
- Testing the theory with new data or scenarios.
- Enhancing documentation or examples.

Please adhere to the terms of use when contributing.

## Terms of Use

This software is provided 'as-is', without any warranty. If you find this project interesting or useful, you may consider making a donation via Bitcoin to `bc1pfxhfmalgpl3v2nq9nx37w4320635dr5x587rh74klzew3gyqv47qtnpaev`. Your support is appreciated and will contribute towards future research in computer science. Code contributions are also welcome and fall under the same terms. Note that this is not a legal contract.

DOI: 10.5281/zenodo.11369637