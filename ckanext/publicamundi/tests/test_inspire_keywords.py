import zope.interface
import zope.schema
import copy
import json
import datetime
from ckanext.publicamundi.lib.metadata.types import *
from ckanext.publicamundi.lib.metadata.types.inspire import *
from ckanext.publicamundi.lib.metadata.base import *
from ckanext.publicamundi.tests.helpers import assert_faulty_keys
from ckanext.publicamundi.lib.metadata.types import *
from ckanext.publicamundi.tests.fixtures import * 
#from ckanext.publicamundi.tests.fixtures import * 


##
## Inspire Keyword fixtures
##

# Terms missing
thes1 = Thesaurus(
        name = "inspire_data_themes", 
        title = u"Inspire Data Themes", 
        reference_date = datetime.date(2000,1,1),
        date_type = 'creation',
        )

#Empty terms
thes2 = Thesaurus(
        name = "inspire_data_themes", 
        title = u"Inspire Data Themes", 
        reference_date = datetime.date(2000,1,1),
        date_type = 'creation',
        terms = []
        )

# Wrong name
thes3 = Thesaurus(
        name = "inspire_data_theme", 
        title = u"Inspire Data Themes", 
        reference_date = datetime.date(2000,1,1),
        date_type = 'creation',
        terms = []
        )

#Correct thesaurus
thes4 = Thesaurus(
        name = "inspire_data_themes", 
        title = u"Inspire Data Themes", 
        reference_date = datetime.date(2000,1,1),
        date_type = 'creation',
        terms = ["addresses"]
        )

def test_thes1():
    ''' INSPIRE thesaurus terms missing'''
    assert_faulty_keys(thes1,set(['terms']))

def test_thes2():
    ''' INSPIRE thesaurus empty terms'''
    assert_faulty_keys(thes2,set(['terms']))

def test_thes3():
    ''' INSPIRE thesaurus wrong name'''
    assert_faulty_keys(thes3,set(['name']))

def test_thes4():
    ''' INSPIRE correct thesaurus'''
    assert_faulty_keys(thes4,None)




# Keywords not included in any of the vocabularies
insp1 = InspireMetadata(
    contact = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact")],
    datestamp = datetime.date.today(),
    languagecode = "el",
    title = u"Title",
    identifier = [u"12314213123"],
    abstract = u"abstracttttttt",
    locator = ["http://www.google.com","http://publicamundi.eu"],
    resource_language = ["el"],
    topic_category = ["biota"],
    keywords = [Thesaurus(terms = ["addresses123","accident"], 
        name = "inspire_data_themes", 
        title = u"Inspire Data Themes", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),
        
        Thesaurus(terms = ["addresses", "accident2"], 
        name = "gemet_concepts", 
        title = u"Gemet Concepts", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),
        ],
    bounding_box = [GeographicBoundingBox(nblat = 0.0, sblat = 0.0, wblng= 0.0, eblng = 0.0)], 
    temporal_extent = [TemporalExtent(start = datetime.date(2012,1,1),end = datetime.date(2014,1,1))],
    creation_date = datetime.date(2012,1,1),
    publication_date = datetime.date(2013,1,1),
    revision_date = datetime.date(2014,1,1),
    lineage = u"lineaage",
    denominator = [0,1,2,3],
    spatial_resolution = [SpatialResolution(uom = u"meters")],
    conformity = [Conformity(title = u"specifications blabla",date = datetime.date.today(),date_type = "creation",degree = "conformant")],
    access_constraints = [u"lalala1",u"lalala2"],
    limitations = [u"limit1",u"limit2"],
    responsible_party = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact"),ResponsibleParty(organization = u"Org2",email = [u"email2@asd.gr"],role = "pointofcontact")])

#Missing inspire data theme keyword (invariant)
insp2 = InspireMetadata(
    contact = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact")],
    datestamp = datetime.date.today(),
    languagecode = "el",
    title = u"Title",
    identifier = [u"12314213123"],
    abstract = u"abstracttttttt",
    locator = ["http://www.google.com","http://publicamundi.eu"],
    resource_language = ["el"],
    topic_category = ["biota"],
    keywords = [Thesaurus(terms = ["accident"], 
        name = "gemet_concepts", 
        title = u"Gemet Concepts", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),

        Thesaurus(terms = ["time_(chronology)"], 
        name = "gemet_groups", 
        title = u"Gemet Groups", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),
        ],
    bounding_box = [GeographicBoundingBox(nblat = 0.0, sblat = 0.0, wblng= 0.0, eblng = 0.0)], 
    temporal_extent = [TemporalExtent(start = datetime.date(2012,1,1),end = datetime.date(2014,1,1))],
    creation_date = datetime.date(2012,1,1),
    publication_date = datetime.date(2013,1,1),
    revision_date = datetime.date(2014,1,1),
    lineage = u"lineaage",
    denominator = [0,1,2,3],
    spatial_resolution = [SpatialResolution(uom = u"meters")],
    conformity = [Conformity(title = u"specifications blabla",date = datetime.date.today(),date_type = "creation",degree = "conformant")],
    access_constraints = [u"lalala1",u"lalala2"],
    limitations = [u"limit1",u"limit2"],
    responsible_party = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact"),ResponsibleParty(organization = u"Org2",email = [u"email2@asd.gr"],role = "pointofcontact")])

# Keywords not from relevant vocabulary (invariant)
insp3 = InspireMetadata(
    contact = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact")],
    datestamp = datetime.date.today(),
    languagecode = "el",
    title = u"Title",
    identifier = [u"12314213123"],
    abstract = u"abstracttttttt",
    locator = ["http://www.google.com","http://publicamundi.eu"],
    resource_language = ["el"],
    topic_category = ["biota"],
    keywords = [Thesaurus(terms = ["addresses","accident"], 
        name = "inspire_data_themes", 
        title = u"Inspire Data Themes", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),
        
        Thesaurus(terms = ["addresses", "accident"], 
        name = "gemet_concepts", 
        title = u"Gemet Concepts", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),

        Thesaurus(terms = ["time_(chronology)"], 
        name = "gemet_groups", 
        title = u"Gemet Groups", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),
        ],
    bounding_box = [GeographicBoundingBox(nblat = 0.0, sblat = 0.0, wblng= 0.0, eblng = 0.0)], 
    temporal_extent = [TemporalExtent(start = datetime.date(2012,1,1),end = datetime.date(2014,1,1))],
    creation_date = datetime.date(2012,1,1),
    publication_date = datetime.date(2013,1,1),
    revision_date = datetime.date(2014,1,1),
    lineage = u"lineaage",
    denominator = [0,1,2,3],
    spatial_resolution = [SpatialResolution(uom = u"meters")],
    conformity = [Conformity(title = u"specifications blabla",date = datetime.date.today(),date_type = "creation",degree = "conformant")],
    access_constraints = [u"lalala1",u"lalala2"],
    limitations = [u"limit1",u"limit2"],
    responsible_party = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact"),ResponsibleParty(organization = u"Org2",email = [u"email2@asd.gr"],role = "pointofcontact")])

insp4 = InspireMetadata(contact = [ResponsibleParty(organization = u"Org",
                                                    email = [u"email@asd.gr"],
                                                    role = "pointofcontact")],
    datestamp = datetime.date.today(),
    languagecode = "el",
    title = u"Title",
    identifier = [u"12314213123"],
    abstract = u"abstracttttttt",
    locator = ["http://www.google.com","http://publicamundi.eu"],
    resource_language = ["el"],
    topic_category = ["biota"],
    bounding_box = [GeographicBoundingBox(nblat = 0.0, sblat = 0.0, wblng= 0.0, eblng = 0.0)], 
    temporal_extent = [TemporalExtent(start = datetime.date(2012,1,1),end = datetime.date(2014,1,1))],
    creation_date = datetime.date(2012,1,1),
    publication_date = datetime.date(2013,1,1),
    revision_date = datetime.date(2014,1,1),
    lineage = u"lineaage",
    denominator = [0,1,2,3],
    spatial_resolution = [SpatialResolution(uom = u"meters")],
    conformity = [Conformity(title = u"specifications blabla",date = datetime.date.today(),date_type = "creation",degree = "conformant")],
    access_constraints = [u"lalala1",u"lalala2"],
    limitations = [u"limit1",u"limit2"],
    responsible_party = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact"),ResponsibleParty(organization = u"Org2",email = [u"email2@asd.gr"],role = "pointofcontact")])

insp5 = InspireMetadata(contact = [ResponsibleParty(organization = u"Org",
                                                    email = [u"email@asd.gr"],
                                                    role = "pointofcontact")],
    datestamp = datetime.date.today(),
    languagecode = "el",
    title = u"Title",
    identifier = [u"12314213123"],
    abstract = u"abstracttttttt",
    locator = ["http://www.google.com","http://publicamundi.eu"],
    resource_language = ["el"],
    topic_category = ["biota"],
    keywords = [Thesaurus(terms = ["addresses"], 
        name = "inspire_data_themes", 
        title = u"Inspire Data Themes", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),
        
        Thesaurus(terms = ["accident"], 
        name = "gemet_concepts", 
        title = u"Gemet Concepts", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),

        Thesaurus(terms = ["time_(chronology)"], 
        name = "gemet_groups", 
        title = u"Gemet Groups", 
        reference_date = datetime.date(2000,1,1), 
        date_type = 'creation'),
        ],

    bounding_box = [GeographicBoundingBox(nblat = 0.0, sblat = 0.0, wblng= 0.0, eblng = 0.0)], 
    temporal_extent = [TemporalExtent(start = datetime.date(2012,1,1),end = datetime.date(2014,1,1))],
    creation_date = datetime.date(2012,1,1),
    publication_date = datetime.date(2013,1,1),
    revision_date = datetime.date(2014,1,1),
    lineage = u"lineaage",
    denominator = [0,1,2,3],
    spatial_resolution = [SpatialResolution(uom = u"meters")],
    conformity = [Conformity(title = u"specifications blabla",date = datetime.date.today(),date_type = "creation",degree = "conformant")],
    access_constraints = [u"lalala1",u"lalala2"],
    limitations = [u"limit1",u"limit2"],
    responsible_party = [ResponsibleParty(organization = u"Org",email = [u"email@asd.gr"],role = "pointofcontact"),ResponsibleParty(organization = u"Org2",email = [u"email2@asd.gr"],role = "pointofcontact")])

def test_insp1():
    ''' INSPIRE keywords not from any of the vocabularies'''
    assert_faulty_keys(insp1,set(['keywords']))

def test_insp2():
    ''' INSPIRE keywords missing value from INSPIRE Data Themes'''
    assert_faulty_keys(insp2,set(['__after']))

def test_insp3():
    ''' INSPIRE keywords not from correct vocabulary '''
    assert_faulty_keys(insp3, set(['__after']))

def test_insp4():
    ''' INSPIRE keywords empty'''
    assert_faulty_keys(insp4, set(['keywords']))

def test_insp5():
    ''' INSPIRE correct keywords'''
    assert_faulty_keys(insp5, None)

if __name__ == '__main__':
    #print repr(insp3)
    #print 'insp 3 ='
    #print insp3
    test_insp3()
