from typing import Any, Union
import builtins, multiprocessing


def input_and_save(prompt, result_dict) -> None:
    """
    This function reads a line from the standard input and saves it to a dictionary.

    ### Parameters:
    - prompt (Any): The object to display before waiting for input.
    - result_dict (multiprocessing.managers.DictProxy): The dictionary where the result will be stored.

    ### Returns:
    - None

    ### Side Effects:
    - Modifies the `result_dict` to include the user's input with the key 'result'.
    """
    stdin = open(file=0)               # Open the standard input
    print(prompt, end="", flush=True)  # Print the prompt
    result = stdin.readline().rstrip() # Read a line from the standard input and remove trailing newline
    result_dict['result'] = result     # Save the result to the dictionary


def input_with_timeout(prompt: Any = '', /, timeout: Union[int, float, None] = 20.0) -> str:
    """\
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

    ### Example:
    ```python
        # To get input with a timeout:
        result = input_with_timeout("Please enter your input: ", timeout=15.0)

        # To get input without a timeout:
        result = input_with_timeout("Please enter your input: ", timeout=None)
    """

    # Check the type and value of the timeout
    if not (isinstance(timeout, (int, float)) or timeout is None):
        raise TypeError(f"timeout must be 'int' or 'float' or 'None', not {type(timeout)}.")
    elif timeout is None:       # If no timeout is specified, use the built-in input function
        return builtins.input(prompt)  
    elif timeout <= 0:          # If the timeout is not positive, raise an error
        raise ValueError(f"timeout value must be greater than zero, timeout: {timeout}.")  

    manager = multiprocessing.Manager()  # Create a manager object
    result_dict = manager.dict()        # Create a dictionary in the manager's namespace

    # Create a new process that will call the input_and_save function
    process = multiprocessing.Process(target=input_and_save, args=(prompt, result_dict))
    process.start()          # Start the new process
    process.join(timeout)  # Wait for the process to finish or for the timeout to expire
    process.terminate()  # Terminate the process

            # If the process finished before the timeout, return the result
    if 'result' in result_dict:
        return result_dict['result']
    else:   # If the process did not finish before the timeout, raise an error
        raise TimeoutError("Timeout occurred.")  


if __name__ == "__main__":
    try:
        name = input_with_timeout('Enter your name: ', 10)
        print('Bonjour', name, '!')
    except TimeoutError as e:
        print("\n""{}: {}".format(type(e).__name__, str(e)))