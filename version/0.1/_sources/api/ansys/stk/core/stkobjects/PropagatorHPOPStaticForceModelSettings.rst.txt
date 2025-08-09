PropagatorHPOPStaticForceModelSettings
======================================

.. py:class:: ansys.stk.core.stkobjects.PropagatorHPOPStaticForceModelSettings

   Class defining static force model options for the HPOP propagator.

.. py:currentmodule:: PropagatorHPOPStaticForceModelSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPStaticForceModelSettings.satellite_mass`
              - A value for the satellite's mass to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPStaticForceModelSettings.include_relativistic_acceleration`
              - Models the effects of general relativity in accordance with IERS Technical Note 32, IERS Conventions (2003).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorHPOPStaticForceModelSettings


Property detail
---------------

.. py:property:: satellite_mass
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPStaticForceModelSettings.satellite_mass
    :type: float

    A value for the satellite's mass to be used in atmospheric drag and solar radiation pressure calculations. Uses Mass Dimension.

.. py:property:: include_relativistic_acceleration
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPStaticForceModelSettings.include_relativistic_acceleration
    :type: bool

    Models the effects of general relativity in accordance with IERS Technical Note 32, IERS Conventions (2003).


