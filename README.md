# Run

To run the tests, execute `python3 -m test.py` in your working directory

# Logic

## main.py

`main.py` includes the logic for naive and efficient implementations for LIS (longest increasing subsequence). Comments are there to explain some of the logic.

## test.py

`test.py` includes logic for testing the implementations in `main.py`. It also used to run `main.py` and recieve the testing results.

## analyze.py

`analyze.py` includes logic for plotting the data generated from `test.py`.

### Sequences

The `Sequences` class is used to generate custom the following sequence types of size `n`:

- Strictly increasing: `Sequences.strictly_increase`
- Strictly decreasing: `Sequences.strickly_decrease`
- Altnerating high/low: `Sequences.alternating_high_low`
- Zig Zag: `Sequences.zig_zag`
- Random: `Sequences.random`

### main

Executes the testing logic.
