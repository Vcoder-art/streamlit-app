FILE_PATH = "todos.txt"


def get_todos(file_path=FILE_PATH):
    """ This function can read file and
    return the list of to-do items.
    """
    with open(file_path, "r") as local_file:
        local_todos = local_file.readlines()
        return local_todos


def write_todos(todos_arg, file_path=FILE_PATH):
    """This function can write todos items to the file."""
    with open(file_path, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello world")