import re


def get_code_from_link(link):
    return re.search(r"[0-9]+", link).group(0)
