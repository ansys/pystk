IAircraftCategory
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftCategory

   object
   
   Interface used to access the Aircraft Category in the Aviator Catalog.

.. py:currentmodule:: IAircraftCategory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftCategory.aircraft_models`
              - Get the user aircraft models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftCategory.missile_models`
              - Get the user missile models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftCategory.rotorcraft_models`
              - Get the user rotorcraft models.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftCategory


Property detail
---------------

.. py:property:: aircraft_models
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftCategory.aircraft_models
    :type: IAircraftModels

    Get the user aircraft models.

.. py:property:: missile_models
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftCategory.missile_models
    :type: IMissileModels

    Get the user missile models.

.. py:property:: rotorcraft_models
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftCategory.rotorcraft_models
    :type: IRotorcraftModels

    Get the user rotorcraft models.


