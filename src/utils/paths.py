import os

__all__ = ('get_dir_path',)


def get_dir_path(base_dir: str, uid: int, suffix: str):
    """
    Prepares file path, and returns new file name.
    """
    dir_size = 100
    depth = 5
    dir_parts = [base_dir]
    while depth > 1:
        depth -= 1
        dir_parts.append(str((uid // (dir_size ** depth)) % dir_size))

    dir_path = os.path.join(*dir_parts)

    file_name = str(uid)

    return "{}.{}".format(os.path.join(*[dir_path, file_name]), suffix)
