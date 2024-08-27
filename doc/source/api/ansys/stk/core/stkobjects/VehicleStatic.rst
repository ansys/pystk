VehicleStatic
=============

.. py:class:: ansys.stk.core.stkobjects.VehicleStatic

   Class defining static force model options for the HPOP propagator.

.. py:currentmodule:: VehicleStatic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStatic.satellite_mass`
              - A value for the satellite's mass to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStatic.inc_relativistic_acc`
              - Models the effects of general relativity in accordance with IERS Technical Note 32, IERS Conventions (2003).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleStatic


Property detail
---------------

.. py:property:: satellite_mass
    :canonical: ansys.stk.core.stkobjects.VehicleStatic.satellite_mass
    :type: float

    A value for the satellite's mass to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.

.. py:property:: inc_relativistic_acc
    :canonical: ansys.stk.core.stkobjects.VehicleStatic.inc_relativistic_acc
    :type: bool

    Models the effects of general relativity in accordance with IERS Technical Note 32, IERS Conventions (2003).


