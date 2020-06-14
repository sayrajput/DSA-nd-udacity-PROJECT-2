import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    # if no path is given.
    if not bool(path):
        return []

    # If a falsey is given for the suffix, set it to None to simplify the file suffix conditional check
    if not bool(suffix):
        suffix = None

    def _find_files(path, files):
        """Recursively walk through the filesystem to find all files that end with the given suffix."""
        for entry in os.listdir(path):
            fullpath = os.path.join(path, entry)
            if os.path.isdir(fullpath):
                files = _find_files(fullpath, files)

            elif os.path.isfile(fullpath) and (suffix is None or entry.endswith(suffix)):
                files.append(fullpath)

        return files

    return _find_files(path, [])




if __name__ == '__main__':

    def run_test(suffix, path):
        files = find_files(suffix, path)
        if len(files) == 0:
            print('No files found.\n')
            return

        for f in files:
            print(f)
        print()

    base_dir = 'C:/Users/Sumit/Downloads'
    
    run_test('', '')
    # No files found.

    run_test('.c', None)
    # No files found.

    run_test('.c', base_dir + '/testdir')

    # C:/Users/Sumit/Downloads/testdir\subdir1\a.c
    # C:/Users/Sumit/Downloads/testdir\subdir3\subsubdir1\b.c
    # C:/Users/Sumit/Downloads/testdir\subdir5\a.c
    # C:/Users/Sumit/Downloads/testdir\t1.c


    run_test('2.py', '.')
    # .\arbit_2.py
    # .\problem_2.py
    # .\simpleblockchain2.py

    run_test('', base_dir+'/testdir')
    
    # C:/Users/Sumit/Downloads/testdir\subdir1\a.c
    # C:/Users/Sumit/Downloads/testdir\subdir1\a.h
    # C:/Users/Sumit/Downloads/testdir\subdir2\.gitkeep
    # C:/Users/Sumit/Downloads/testdir\subdir3\subsubdir1\b.c
    # C:/Users/Sumit/Downloads/testdir\subdir3\subsubdir1\b.h
    # C:/Users/Sumit/Downloads/testdir\subdir4\.gitkeep
    # C:/Users/Sumit/Downloads/testdir\subdir5\a.c
    # C:/Users/Sumit/Downloads/testdir\subdir5\a.h
    # C:/Users/Sumit/Downloads/testdir\t1.c
    # C:/Users/Sumit/Downloads/testdir\t1.h

   
