import pyshacl
from rdflib import Graph

ontology_file = "ontology/drip.ttl"
shapes_file = "shapes/drip-shapes.ttl"
data_file = "tests/some-coffee-maker.ttl"

# Load ontology, shapes, and instance data graphs
ontology_graph = Graph().parse(ontology_file, format="turtle")
shapes_graph = Graph().parse(shapes_file, format="turtle")
data_graph = Graph().parse(data_file, format="turtle")

# Run the SHACL validation
conforms, report_graph, report_text = pyshacl.validate(
    data_graph, shacl_graph=shapes_graph, ont_graph=ontology_graph, inference="rdfs", abort_on_error=False, debug=True
)

print("Conforms:", conforms)
print("Validation report:")
print(report_text)

