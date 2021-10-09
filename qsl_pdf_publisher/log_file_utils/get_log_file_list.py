"""
get_log_file_list module
"""
import glob
import os
import typing
from qsl_pdf_publisher.log_file_utils.log_file import LogFile



def get_log_file_list(search_directory: str) -> typing.Tuple[LogFile, ...]:
    """
    get log File list
    """
    log_file_list = []
    file_patterns = ('*.adi', '*.adif')

    for file_pattern in file_patterns:
        filepaths = glob.glob(os.path.join(search_directory, file_pattern))
        for filepath in filepaths:
            log_file_list.append(LogFile(
                basename=os.path.basename(filepath),
                path=filepath
            ))

    return tuple(log_file_list)
