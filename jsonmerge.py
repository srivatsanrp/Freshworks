"""
Merge two or more JSON documents.

Usage:
    jsonmerge.py [-i, --indent=N] <file.json>...

Options:
    -i
        Indent with the default width of 4 spaces.

    --indent=N
        Indent with the specified number of spaces.
"""
import json
import itertools
import sys

import docopt


MISSING = object()


def json_merge_all(json_objects):
    merged = reduce(json_merge, json_objects, MISSING)
   
    if merged == MISSING:
        raise ValueError("json_objects was empty")
    return merged


def json_merge(a, b):
  
    if isinstance(a, dict) and isinstance(b, dict):
        return dict(
            (k, json_merge(a_val, b_val))
            for k, a_val, b_val in dictzip_longest(a, b, fillvalue=MISSING)
        )
    elif isinstance(a, list) and isinstance(b, list):
       
        return list(itertools.chain(a, b))

   
    if b is MISSING:
        assert a is not MISSING
        return a
    return b


def dictzip_longest(*dicts, **kwargs):

    fillvalue = kwargs.get("fillvalue", None)
    keys = reduce(set.union, [set(d.keys()) for d in dicts], set())
    return [tuple([k] + [d.get(k, fillvalue) for d in dicts]) for k in keys]


if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    indent = None
    if args.get("-i") or args.get("--indent") is not None:
        try:
            indent = int(args.get("--indent"))
        except:
            indent = 4

    json_objects = [json.load(open(f)) for f in args["<file.json>"]]
    merged = json_merge_all(json_objects)

    json.dump(merged, sys.stdout, indent=indent)
