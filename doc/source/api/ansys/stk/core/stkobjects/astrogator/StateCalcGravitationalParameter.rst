StateCalcGravitationalParameter
===============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   GravitationalParameter Calc objects.

.. py:currentmodule:: StateCalcGravitationalParameter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter.grav_source`
              - Gets or sets the source for the gravitational parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter.gravity_filename`
              - Source for the gravitational parameter if GravSource is set to Gravity File.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcGravitationalParameter


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: grav_source
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter.grav_source
    :type: GRAVITATIONAL_PARAMETER_SOURCE

    Gets or sets the source for the gravitational parameter.

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcGravitationalParameter.gravity_filename
    :type: str

    Source for the gravitational parameter if GravSource is set to Gravity File.


