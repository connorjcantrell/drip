# Drip Ontology

## Overview
The Drip Ontology is a lightweight ontology that models a simple coffee maker. It includes classes representing various components of a coffee maker such as heating element, pump, water reservoir, and filter basket. The ontology also defines relationships between the components such as "serves" and "has part".

## Ontology Details
The Drip Ontology defines the following classes:

- drip:Component: A general class representing components of a coffee maker.
- drip:DripCoffeeMaker: A device that automates the process of brewing coffee using a system of water heating, pumping, and dispensing over coffee grounds.
- drip:WaterReservoir: A component that stores water needed for brewing coffee.
- drip:HeatingElement: An electrical component responsible for heating water to an optimal temperature.
- drip:Pump: A mechanical component that moves heated water through a distribution system.
- drip:Showerhead: A perforated component that evenly disperses hot water over coffee grounds.
- drip:FilterBasket: A component that holds coffee grounds, typically lined with a filter.
- drip:Carafe: A glass or thermal container that collects the brewed coffee.

The ontology also defines the following properties:

- drip:hasPart: A property to link components of a coffee maker to the coffee maker itself.
- drip:serves: A property to link coffee maker components to the components they serve.

## SHACL Shapes
The SHACL shapes in the Drip Ontology repository define constraints for the following classes:

drip:HeatingElement
drip:WaterReservoir
drip:Pump
drip:Showerhead
These shapes specify that each component must serve at least one other component, as follows:

A Heating Element must serve at least one Water Reservoir.
A Water Reservoir must serve at least one Pump.
A Pump must serve at least one Showerhead.
A Showerhead must serve at least one FilterBasket.
Example
The example directory contains an example instance of a coffee maker in RDF/Turtle format (some-coffee-maker.ttl) and a Python script to validate it against the Drip Ontology and SHACL shapes (validate.py). To run the validation, simply navigate to the example directory and run python3 validate.py. The output will indicate whether the instance conforms to the constraints specified in the ontology and shapes.

## Tests
To run the SHACL validation tests on the Drip Ontology, you will need to have a Python environment set up with the pyshacl library installed.

Here are the steps to set up a Python environment:

1. Open a terminal and navigate to the `example` directory.
2. Create a new Python virtual environment with the following command:
```
python3 -m venv venv
```
3. Activate the virtual environment with the following command:
```
source venv/bin/activate
```
4. Install the required dependencies with the following command:
```
pip3 install -r requirements.txt
```
This will install the pyshacl library.
5. Run the validation script with the following command:
```
python3 validate.py
```

This will run the SHACL validation tests on the Drip Ontology and produce a validation report.

The validate.py script uses the pyshacl library to perform the validation. It loads the Drip Ontology, the SHACL shapes graph, and an instance data graph. It then runs the SHACL validation on the instance data graph using the shapes graph and the ontology graph for inference. The script prints out whether or not the instance data graph conforms to the shapes graph and a validation report with any constraint violations that were found.
