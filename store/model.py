from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class Creature(GraphObject):
    '''A named creature.'''
    __primarykey__ = "Name"

    Name = Property()
