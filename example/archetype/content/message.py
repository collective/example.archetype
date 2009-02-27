# Zope3 imports
from zope.interface import implements

# CMF imports
from Products.CMFCore import permissions

# Archetypes imports
from Products.Archetypes import atapi

# Product imports
from example.archetype.config import PROJECTNAME
from example.archetype.config import MESSAGE_PRIORITIES
from example.archetype.interfaces import IInstantMessage


# Schema definition
schema = atapi.BaseSchema.copy() +  atapi.Schema((

  atapi.StringField('priority',
              vocabulary = MESSAGE_PRIORITIES,
              default = 'normal',
              widget = atapi.SelectionWidget(label = 'Priority'),
             ),

  atapi.TextField('body',
            searchable = 1,
            required = 1,
            allowable_content_types = ('text/plain',
                                       'text/structured',
                                       'text/html',),
            default_output_type = 'text/x-html-safe',
            widget = atapi.RichWidget(label = 'Message Body'),
           ),

))


class InstantMessage(atapi.BaseContent):
    """An Archetype for an InstantMessage application"""

    implements(IInstantMessage)

    schema = schema

    portal_type = meta_type = 'InstantMessage'
    
    _at_rename_after_creation = True
    
# Content type registration for the Archetypes machinery
atapi.registerType(InstantMessage, PROJECTNAME)
