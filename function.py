def get_todos(filepath="todo.txt"):
    """
    Reads a file and returns a list of to-do items.

    Args:
        filepath (str): The path to the file containing to-do items. Defaults to "todo.txt".

    Returns:
        list: A list of strings, each representing a to-do item.
    """
    try:
        with open(filepath, "r") as file:
            todos = file.readlines()
    except FileNotFoundError:
        todos = []
    return todos

def write_todos(todos, filepath="todo.txt"):
    """
    Writes a list of to-do items to a file.

    Args:
        todos (list): A list of strings to write to the file.
        filepath (str): The path to the file. Defaults to "todo.txt".
    """
    with open(filepath, "w") as file:
        file.writelines(todos)