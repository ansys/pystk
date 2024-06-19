IAircraftCategory
=================

.. py:class:: IAircraftCategory

   object
   
   Interface used to access the Aircraft Category in the Aviator Catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aircraft_models`
            * - :py:meth:`~missile_models`
            * - :py:meth:`~rotorcraft_models`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftCategory


Property detail
---------------

.. py:property:: aircraft_models
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftCategory.aircraft_models
    :type: IAgAvtrAircraftModels

    Get the user aircraft models.

.. py:property:: missile_models
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftCategory.missile_models
    :type: IAgAvtrMissileModels

    Get the user missile models.

.. py:property:: rotorcraft_models
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftCategory.rotorcraft_models
    :type: IAgAvtrRotorcraftModels

    Get the user rotorcraft models.


