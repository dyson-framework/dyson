import glob
import os

from dyson.vars import merge_dict


def load_keywords(keywords_path=None):
    all_keywords = dict()

    keyword_paths = (
        os.path.abspath("/etc/dyson/keywords"),
        os.path.abspath(os.path.join(os.path.dirname(os.path.curdir), "keywords"))
    )

    if keywords_path is not None:
        all_keywords = merge_dict(load_keywords(), _load_keywords_from_path(keywords_path))
    else:
        for keyword_path in keyword_paths:
            all_keywords = merge_dict(all_keywords, _load_keywords_from_path(keyword_path))

    return all_keywords


def _load_keywords_from_path(keywords_path):
    all_keywords = dict()

    if os.path.exists(keywords_path) and os.path.isdir(keywords_path):
        for filename in glob.iglob("%s/**" % keywords_path, recursive=True):
            if os.path.isfile(filename):
                keyword_to_load = os.path.basename(os.path.splitext(filename)[0])
                all_keywords[keyword_to_load] = os.path.abspath(filename)

    return all_keywords
