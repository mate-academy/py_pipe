# py_pipe

You have three functions:
f0: x*x
f1: x//2
f2: x + 4

For given x and sequence of functions numbers calculate the result of composition of this functions.
Example:
(0, 1, 2) -> x = f2(f1(f0(x)))

To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

To run all style checkers and tests use commands:

`pytest `

`flake8 pipe`

`pylint pipe`

`mypy --ignore-missing-imports .`
