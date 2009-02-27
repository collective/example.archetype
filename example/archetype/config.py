
# Archetypes imports
from Products.Archetypes.atapi import DisplayList


PROJECTNAME = "example.archetype"

# To be used in the InstantMessage priority field definition
MESSAGE_PRIORITIES = DisplayList((
    ('high', 'High Priority'),
    ('normal', 'Normal Priority'),
    ('low', 'Low Priority'),
    ))

