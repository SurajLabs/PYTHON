import os
# select the directory whose content you want to list
def list_directory_contents(path='/New Folder'):
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory {path!r} does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: {path!r} is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access {path!r}.")
        return

    print(f"Contents of directory {path!r}:")
    for name in entries:
        print(name)

if __name__ == "__main__":
    directory_path = input("Enter directory path (press Enter for current directory): ").strip()
    if not directory_path:
        directory_path = '.'
    list_directory_contents(directory_path)
    

# path!r = it  represents the path as a string in a way that is suitable for debugging, including quotes around the string. This is useful for clearly showing the value of the path variable in error messages.
# This functions tells the user if the directory does not exist, is not a directory, or if there is a permission issue. It also allows the user to specify a directory path or defaults to the current directory if no input is provided.