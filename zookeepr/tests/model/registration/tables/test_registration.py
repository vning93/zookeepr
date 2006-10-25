from zookeepr.tests.model import *

class TestRegistrationTable(TableTest):
    """Test the ``registration`` table.

    This table stores registration details.
    """
    tables = model.registration.tables.registration
    samples = [dict(address1='a11',
                    address2='a12',
                    city='city1',
                    state='state1',
                    country='country1',
                    postcode='postcode1',
                    company='company1',
                    shell='shell1',
                    shelltext='shelltext1',
                    editor='editor1',
                    editorstring='editorstring1',
                    distro='distro1',
                    distrostring='distrostring1',
                    type='type1',
                    discount_code='discount_code1',
                    teesize='teesize1',
                    dinner=1,
                    diet='diet1',
                    special='special1',
                    opendaydrag=1,
                    partner_email='partneremail1',
                    kids_0_3=1,
                    kids_4_6=1,
                    kids_7_9=1,
                    kids_10=1,
                    accommodation='accommodation1',
                    checkin=1,
                    checkout=1,
                    lasignup=1,
                    announcesignup=1,
                    delegatesignup=1,
                    ),
               dict(address1='a11',
                    address2='a12',
                    city='city1',
                    state='state1',
                    country='country1',
                    postcode='postcode1',
                    company='company1',
                    shell='shell1',
                    shelltext='shelltext1',
                    editor='editor1',
                    editorstring='editorstring1',
                    distro='distro1',
                    distrostring='distrostring1',
                    type='type1',
                    discount_code='discount_code1',
                    teesize='teesize1',
                    dinner=1,
                    diet='diet1',
                    special='special1',
                    opendaydrag=1,
                    partner_email='partneremail1',
                    kids_0_3=1,
                    kids_4_6=1,
                    kids_7_9=1,
                    kids_10=1,
                    accommodation='accommodation1',
                    checkin=1,
                    checkout=1,
                    lasignup=1,
                    announcesignup=1,
                    delegatesignup=1,
                    ),
                ]
