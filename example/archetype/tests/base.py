"""Base class for integration tests, based on ZopeTestCase and PloneTestCase.

Note that importing this module has various side-effects: it registers a set of
products with Zope, and it sets up a sandbox Plone site with the appropriate
products installed.
"""

from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase

# Import PloneTestCase
from Products.PloneTestCase.PloneTestCase import PloneTestCase
from Products.PloneTestCase.PloneTestCase import FunctionalTestCase
from Products.PloneTestCase.PloneTestCase import setupPloneSite

from Products.PloneTestCase.layer import onsetup


# Load the ZCML for our package
import example.archetype

@onsetup
def setup_product():
    zcml.load_config('configure.zcml', example.archetype)

setup_product()

# Let Zope know about the products we require above-and-beyond a basic
# Plone install (PloneTestCase takes care of these).
#ZopeTestCase.installProduct('example.archetype')   # NOT NEEDED ???

# Set up a Plone site, and quick-install the relevant products
setupPloneSite(products=('example.archetype',))


class InstantMessageTestCase(PloneTestCase):
    """Base class for integration tests.

    This may provide specific set-up and tear-down operations, or provide
    convenience methods.
    """


class InstantMessageFunctionalTestCase(FunctionalTestCase):
    """Base class for functional integration tests.

    This may provide specific set-up and tear-down operations, or provide
    convenience methods.
    """