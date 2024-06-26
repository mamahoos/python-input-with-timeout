# Input with Timeout

This Python project provides a function `input_with_timeout` which allows capturing user input with a specified `timeout`. If the user does not provide input within the `timeout` period, a `TimeoutError` is raised.

## Installation
You can install this packag using the following commands:
```bash
pip install input-with-timeout
```
 or
```bash
pip install git+https://github.com/mamahoos/python-input-with-timeout
```

## Features

- Customizable `timeout` for user input.
- Cross-platform support.
- Easy integration with existing Python projects.

## Usage

To use the `input_with_timeout` function, simply import it from the module and call it with the desired prompt and `timeout` values.


```python
from input_with_timeout import input_with_timeout

try:
    user_input = input_with_timeout("Enter your input: ", timeout=10)
    print(f"Input received: '{user_input}'.")
except TimeoutError:
    print("No input received within the timeout period.")
```
## Contact
If you want to contact me you can reach me at https://t.me/mamahoos .
