IPerformanceModel
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IPerformanceModel

   Interface for a performance model of an Aviator vehicle.

.. py:currentmodule:: IPerformanceModel

Examples
--------

Create a new performance model for an aircraft

.. code-block:: python

    # AircraftModel aviatorAircraft: Aviator Aircraft object
    # Get the acceleration type
    acceleration = aviatorAircraft.acceleration
    # Get the names of the current acceleration models
    modelNames = acceleration.child_names
    # Check how many models there are
    modelCount = len(modelNames)
    # Get the child types (for example AGI Basic Acceleration Model, Advanced Acceleration Model)
    modelTypes = acceleration.child_types
    # Create a new performance model of type "Advanced Acceleration Model"
    newPerformanceModel = acceleration.add_child_of_type("Advanced Acceleration Model", "Model Name")
    # Save the changes to the catalog
    aviatorAircraft.save()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IPerformanceModel



