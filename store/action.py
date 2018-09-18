from py2neo import Graph, Node, Relationship
import os

h = os.environ.get('GRAPHENEDB_HOST', 'localhost')
u = os.environ.get('NEO4J_USERNAME', 'neo4j')
p = os.environ.get('NEO4J_PASSWORD', '111111')
graph = Graph(host=h, user=u, password=p)

def get_creatures():
    '''Get a list of all named creatures.'''
    return graph.data("MATCH (creature:Creature) RETURN creature.Name AS creature_name")
