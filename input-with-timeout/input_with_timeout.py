from console_output import cout, endl
from typing import Union, Any
import time, builtins, types


try:
    from msvcrt import getch, kbhit
except ImportError:
    print("Currently only Windows is supported.")
    builtins.exit(1)


def input_with_timeout(prompt: Any = '', /, timeout: Union[int, float, None] = 20.0 ) -> str:
    """
    This function prompts the user for input and returns the input if received within the specified `timeout`.
    If the input is not received within the `timeout`, a TimeoutError is raised.
    
    ### Parameters:
    - prompt (Any): The text to display before waiting for input.
    - timeout (Union[int, float, None]): The maximum time to wait for input. Set to `None` for no `timeout`.

    ### Returns:
    - str: The user input if received within the specified `timeout`.

    ### Raises:
    - TimeoutError: If no input is received within the specified `timeout`.
    - TypeError: If the `timeout` is not an instance of `int`, `float`, or `None`.
    - ValueError: If the `timeout` value is less than or equal to zero.

    ### Usage:
    ```python
        # To get input with a timeout:
        result = input_with_timeout("Please enter your input: ", timeout=15.0)

        # To get input without a timeout:
        result = input_with_timeout("Please enter your input: ", timeout=None)
    """
    
    if not isinstance(timeout, (int, float, types.NoneType)):
        raise TypeError(f"timeout must be 'int' or 'float' or 'None', not {type(timeout)}.")
    elif timeout is None:
        return builtins.input(prompt)
    elif timeout <= 0:
        raise ValueError(f"timeout value must be greater than zero, timeout: {timeout}.")

    cout << prompt              # Print the prompt to the console

    CR = chr(0x0D)              # Carriage return character
    LF = chr(0x0A)              # Line feed character 
    BS = chr(0x08)              # Backspace character
    SP = chr(0x20)              # Space character 

    DELAY = 5e-2                # 50 ms
    line  = ''                  # Initialize an empty line buffer
    start = time.monotonic()
    end   = start + timeout     # Calculate the end time for the timeout

    while (time.monotonic() < end):
        if kbhit():                     # If a key has been pressed
            ch = getch().decode(encoding='utf-8')
                                        # Get the pressed character
            if ch in (CR, LF):          # If the character is a carriage return or line feed
                cout << endl            # cout << CR << LF
                return line
            
            elif ch == BS:              # Handle backspace character
                if line:                # If the line is not empty 
                    line = line[:-1]    # Remove the last character from the line
                    cout << BS << SP    # Clear the last character from the screen
                    cout << BS          # Move the cursor back

            else:
                line += ch              # Append the character to the end of the line
                cout << ch
        else:
            time.sleep(DELAY)           # Sleep for a short delay (50 ms) to prevent high CPU usage

    cout << ''.join(
        BS*len(line) + SP*len(line)     # Clear the line if timeout is reached
    ) << endl

    raise TimeoutError                  # And raise TimeoutError


if __name__ == "__main__":
    try:
        input_result = input_with_timeout("Enter your input: ", timeout=15.0)
        print(f"Input received: '{input_result}'.")
    except TimeoutError:
        print("Timeout occurred.")
