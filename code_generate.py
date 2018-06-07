
import xml.etree.ElementTree as ET
from jinja2 import Template

class Box(object):
	def __init__(self, id, value):
		self.id = id
		self.value = value

	def __str__(self):
		return 'Box(id: ' + str(self.id) + ', value: ' + str(self.value) + ')'

class Edge(object):
	def __init__(self, id, source, target):
		self.id = id
		self.source = source
		self.target = target

	def __str__(self):
		return 'Edge(id: ' + str(self.id) + ', ' + str(self.source) + ' -> ' + str(self.target) + ')'

def is_edge(attrib):
	if 'source' in attrib and 'target' in attrib and 'edge' in attrib:
		return True
	return False

def is_box(attrib):
	if 'vertex' in attrib:
		return True
	return False

if __name__ == '__main__':
	tree = ET.parse('state_machine.xml')
	root = tree.getroot()

	elems = []

	for child in root:
		for ch in child:
			if is_edge(ch.attrib):
				elems += [Edge(ch.attrib['id'], ch.attrib['source'], ch.attrib['target'])]
			elif is_box(ch.attrib):
				elems += [Box(ch.attrib['id'], ch.attrib['value'])]

	for elem in elems:
		print elem
