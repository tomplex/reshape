
import fiona as _fiona
from reshape.wkt import wkt_source
from reshape.pg import postgres_source, where


def shapefile_source(path, encoding='utf-8'):
    with _fiona.open(path, encoding=encoding) as src:
        yield from src


def tabfile_source(path, encoding='latin-1'):
    yield from shapefile_source(path, encoding)


_registry = {
    'shp': shapefile_source,
    'tab': tabfile_source,
    'wkt': wkt_source,
}


def file_source(path, *args, **kwargs):
    ext = path.split('.')[-1]
    if ext in _registry:
        return _registry.get(ext)(path, *args, **kwargs)
