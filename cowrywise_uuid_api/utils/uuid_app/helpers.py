import re
from typing import Optional
from uuid import UUID


def is_valid_uuid(uuid_to_test: str, version: Optional[int] = 4) -> bool:
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


def response_matches(dict_to_validate: dict[str, str]) -> bool:
    """
    Validates that a dictionary matches the following format -
    {"2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"}
    :param dict_to_validate: dictionary to be validated
    :return: True if dictionary matches the format and False otherwise
    """
    datetime_regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}')
    key = list(dict_to_validate.keys())[0]
    if datetime_regex.match(list(dict_to_validate.keys())[0]) and is_valid_uuid(dict_to_validate[key], 4):
        return True
    return False
