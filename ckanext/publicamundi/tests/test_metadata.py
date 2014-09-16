import zope.interface
import zope.schema
import json
import datadiff
import copy
from zope.interface.verify import verifyObject
from datadiff.tools import assert_equal

from ckanext.publicamundi.lib.json_encoder import JsonEncoder
from ckanext.publicamundi.lib.metadata import Object
from ckanext.publicamundi.lib.metadata import types
from ckanext.publicamundi.tests import fixtures

def print_as_dict(obj):
    
    assert isinstance(obj, Object)

    d1 = obj.to_dict(flat=False)
    print d1 #json.dumps(d1, indent=4)

    d2 = obj.to_dict(flat=True)
    for k in sorted(d2):
        print k, ':', d2[k]

def _test_validate(x):
    
    obj = getattr(fixtures, x)
    errors = obj.validate()
    if not errors:
        print_as_dict(obj)

def _test_convert_to_dict(x):
    
    obj = getattr(fixtures, x)
    factory = type(obj)

    d = obj.to_dict()
    obj1 = factory().from_dict(d)

    s = json.dumps(d, cls=JsonEncoder)
    s1 = json.dumps(obj1.to_dict(), cls=JsonEncoder)
    assert s == s1

    d = obj.to_dict(flat=True)
    obj2 = factory().from_dict(d, is_flat=True)
    s = json.dumps(obj.to_dict(), cls=JsonEncoder)
    s2 = json.dumps(obj2.to_dict(), cls=JsonEncoder)
    assert s == s2

def _test_schema(x):
    
    obj = getattr(fixtures, x)
    
    schema = obj.schema()
    verifyObject(schema, obj)    

    # Test basic schema introspection

    fields = obj.get_fields()
    assert set(fields.keys()) == set(zope.schema.getFieldNames(schema))
    print fields

    # Test flattenned schema with a variety of options

    opt_variations = [
        { 'serialize-keys': True, 'key-prefix': 'baobab', },
        { 'serialize-keys': True, },
        { 'serialize-keys': False, },
        {},
    ]

    for opts in opt_variations:
        flattened_fields = obj.get_flattened_fields(opts=opts)
        print flattened_fields
        d = obj.to_dict(flat=True, opts=opts) 
        assert set(d.keys()).issubset(set(flattened_fields.keys()))

    return

def _test_copying(x):

    o1 = getattr(fixtures, x)
    d1 = o1.to_dict()
    o2 = copy.deepcopy(o1)    
    d2 = o2.to_dict()

    assert_equal(d1, d2) 
    
def test_validators():
    
    yield _test_validate, 'bbox1'
    yield _test_validate, 'foo1'
    yield _test_validate, 'thesaurus_gemet_concepts'

def test_dict_converters():
    
    yield _test_convert_to_dict, 'bbox1'
    yield _test_convert_to_dict, 'foo1'
    yield _test_convert_to_dict, 'thesaurus_gemet_concepts'

def test_schema():
    
    yield _test_schema, 'bbox1'
    yield _test_schema, 'foo1'
    yield _test_schema, 'thesaurus_gemet_concepts'

def test_copying():
    
    yield _test_copying, 'bbox1'
    yield _test_copying, 'foo1'
    yield _test_copying, 'thesaurus_gemet_concepts'

if __name__  == '__main__':
    
    _test_validate('foo1')
    _test_convert_to_dict('foo1')

