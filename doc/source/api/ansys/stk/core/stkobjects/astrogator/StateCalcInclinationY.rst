StateCalcInclinationY
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcInclinationY

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   InclinationY Calc objects.

.. py:currentmodule:: StateCalcInclinationY

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclinationY.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcInclinationY.inclination_magnitude_type`
              - Magnitude to use when computing the inclination vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcInclinationY


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcInclinationY.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: inclination_magnitude_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcInclinationY.inclination_magnitude_type
    :type: GeoStationaryInclinationMagnitude

    Magnitude to use when computing the inclination vector.


