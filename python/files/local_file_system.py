import os


def file_name_comparator(file_name):
    return int(file_name.split('-')[2])


def get_files_paths(root_path, scope=None):
    if scope is None:
        scope = []

    files = []

    for file_root, file_sub_directories, sub_folders in os.walk(root_path):
        for sub_directory in file_sub_directories:
            for sub_root, directories_names, files_names in os.walk("{}/{}".format(file_root, sub_directory)):
                files_names.sort(key=file_name_comparator)
                for file_name in files_names:
                    if sub_directory in scope or not scope:
                        files.append("{}/{}".format(sub_root, file_name))

    return files


def has_date_on_path(path, dates):
    for date in dates:
        if date in path:
            return True

    return False
