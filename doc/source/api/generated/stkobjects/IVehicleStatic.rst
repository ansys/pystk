IVehicleStatic
==============

.. py:class:: IVehicleStatic

   object
   
   Interface for additional static force model options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~satellite_mass`
            * - :py:meth:`~inc_relativistic_acc`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleStatic


Property detail
---------------

.. py:property:: satellite_mass
    :canonical: ansys.stk.core.stkobjects.IVehicleStatic.satellite_mass
    :type: float

    A value for the satellite's mass to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.

.. py:property:: inc_relativistic_acc
    :canonical: ansys.stk.core.stkobjects.IVehicleStatic.inc_relativistic_acc
    :type: bool

    Models the effects of general relativity in accordance with IERS Technical Note 32, IERS Conventions (2003).


