import os

def recurse(directory: str):
    if not os.path.exists(directory):
        raise RuntimeError(f"Directory does not exist: {directory}")
    
    print(f"Scanning all items in directory: {directory}")

    dir_contents = os.listdir(directory)
    subdirs = list[str]()
    filenames = list[str]()
    for item in dir_contents:
        test_path = f"{directory}/{item}"
        if os.path.isdir(test_path):
            subdirs.append(test_path)
        elif os.path.isfile(test_path):
            if item.endswith((".cpp", ".cc", ".hpp", ".hh", ".h")):
                filenames.append(test_path)
        else:
            print(f"[WARN] Item is neither a file nor a directory: {item}")

    # Do files in current directory first
    for filename in filenames:
        try:
            parse(filename)
        except OSError:
            print(f"[ERROR] Could not open file at: {filename}")

    # Now recurse through subdirectories
    for subdir in subdirs:
        recurse(subdir)

# Rewrites file's includes
def parse(filepath: str):
    f = open(filepath, "rt")
    contents = f.read()
    lines = contents.split('\n')
    includes = get_includes(lines)

    print(includes)

# Get includes in C/C++ file
def get_includes(lines: list[str]) -> list[tuple[int, str]]:
    includes = list[tuple[int, str]]()

    for i in range(len(lines)):
        line = lines[i]
        if line.count("#include"):
            words = line.split()[1:]
            final_word = str()
            for word in words:
                final_word += word

            includes.append((i, final_word))

    return includes
