"""Main product initializer
"""

# Archetypes & CMF imports
from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore import utils

# Product imports
from config import PROJECTNAME
# Import the content types modules
from content import *
# Import the content types permissions
from permissions import ADD_CONTENT_PERMISSIONS

# Define a message factory for when this product is internationalised.
# This will be imported with the special name "_" in most modules. Strings
# like _(u"message") will then be extracted by i18n tools for translation.

from zope.i18nmessageid import MessageFactory
messageFactory = MessageFactory('example.archetype')


def initialize(context):
    
    content_types, constructors, ftis = process_types(
             listTypes(PROJECTNAME), 
             PROJECTNAME)

    allTypes = zip(content_types, constructors)
    for atype, constructor in allTypes:
        kind = "%s: %s" % (PROJECTNAME, atype.portal_type)
        utils.ContentInit(kind,            
                          content_types      = (atype,),
                          permission         = ADD_CONTENT_PERMISSIONS[atype.portal_type],
                          extra_constructors = (constructor,),            
                          fti                = ftis,
                          ).initialize(context)
