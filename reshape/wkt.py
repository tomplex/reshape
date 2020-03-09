
import csv
import typing
import warnings

from collections import OrderedDict

from pathlib import Path


import geomet.wkt


class WKT(csv.unix_dialect):
    delimiter = '|'
    quoting = csv.QUOTE_MINIMAL


def wkt_source(path: typing.Union[str, Path], geom_field: int = -1, header: bool = True,
               fieldnames: typing.List[str] = None, encoding: str = 'utf-8') -> typing.Iterator[dict]:
    """

    Args:
        path: Path of the file to read
        geom_field: the index of the geometry field
        header: Is the first row a header
        fieldnames: Provide fieldnames for the file. Will override the header if set to True.
        encoding: defaults to utf-8

    Returns:

    """
    fh = open(path, encoding=encoding)
    reader = csv.reader(fh, dialect=WKT)

    if header:
        header = next(reader)
        header.pop(geom_field)

    if fieldnames:
        header = fieldnames

    if not header and not fieldnames:
        warnings.warn("The header flag was set to False and no fieldnames were specified, so no attributes will be "
                      "included from the file.")
        header = []

    for row in reader:
        geom = row.pop(geom_field)
        yield {
            'type': 'Feature',
            'geometry': geomet.wkt.loads(geom),
            'properties': OrderedDict(zip(header, row))
        }
