# Drip Ontology

## Overview
The Drip Ontology is a lightweight ontology that models a coffee maker and defines classes for its components such as heating element, pump, water reservoir, and filter basket, along with their relationships like "serves" and "has part". This resource serves as a practical guide for individuals interested in ontology development, providing an example of how to design and validate an ontology using SHACL shapes and a sample instance file in RDF/Turtle format.


## Ontology Details
The Drip Ontology defines the following classes:

- `drip:Component`: A general class representing components of a coffee maker.
- `drip:DripCoffeeMaker`: A device that automates the process of brewing coffee using a system of water heating, pumping, and dispensing over coffee grounds.
- `drip:WaterReservoir`: A component that stores water needed for brewing coffee.
- `drip:HeatingElement`: An electrical component responsible for heating water to an optimal temperature.
- `drip:Pump`: A mechanical component that moves heated water through a distribution system.
- `drip:Showerhead`: A perforated component that evenly disperses hot water over coffee grounds.
- `drip:FilterBasket`: A component that holds coffee grounds, typically lined with a filter.
- `drip:Carafe`: A glass or thermal container that collects the brewed coffee.

The ontology also defines the following properties:

- `drip:hasPart`: A property to link components of a coffee maker to the coffee maker itself.
- `drip:serves`: A property to link coffee maker components to the components they serve.

## SHACL Shapes
The SHACL shapes in the Drip Ontology repository define constraints for the following classes:

- `drip:HeatingElement`
- `drip:WaterReservoir`
- `drip:Pump`
- `drip:Showerhead`

These shapes specify that each component must serve at least one other component, as follows:

- A Heating Element must serve at least one Water Reservoir.
- A Water Reservoir must serve at least one Pump.
- A Pump must serve at least one Showerhead.
- A Showerhead must serve at least one FilterBasket.


## Tests
The tests directory contains an example instance of a coffee maker in RDF/Turtle format (`some-coffee-maker.ttl`) and a Python script to validate it against the Drip Ontology and SHACL shapes (`test_validation.py`). 

To run the SHACL validation tests on the Drip Ontology, you will need to have a Python environment set up and managed by Poetry.

Here are the steps to set up a Python environment using Poetry:

1. Open a terminal and navigate to the project's root directory.
2. Install Poetry if you haven't already, following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).
3. Install the project dependencies managed by Poetry with the following command:
```
poetry install
```
4. Run the validation script with the following command:
```
poetry run pytest
```
This will run the SHACL validation tests on the Drip Ontology and produce a validation report.

The `test_validation.py` script utilizes the pyshacl library to perform the validation. It loads the Drip Ontology, the SHACL shapes graph, and an instance data graph. The script then runs the SHACL validation on the instance data graph using the shapes graph and the ontology graph for inference. Upon completion, it provides a validation report containing any constraint violations that were found, if any.

