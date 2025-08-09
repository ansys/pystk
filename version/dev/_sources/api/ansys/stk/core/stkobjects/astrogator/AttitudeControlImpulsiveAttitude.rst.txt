AttitudeControlImpulsiveAttitude
================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsive`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The attitude attitude control for an impulsive maneuver.

.. py:currentmodule:: AttitudeControlImpulsiveAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude.delta_v_magnitude`
              - Get or set the size of the delta-V to be applied along the X axis - as defined by the selected axes and rotation. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude.orientation`
              - Get the orientation of the attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude.reference_axes_name`
              - Ref Axes - the reference axes to be used in modeling this maneuver.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlImpulsiveAttitude


Property detail
---------------

.. py:property:: delta_v_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude.delta_v_magnitude
    :type: float

    Get or set the size of the delta-V to be applied along the X axis - as defined by the selected axes and rotation. Uses Rate Dimension.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude.orientation
    :type: IOrientation

    Get the orientation of the attitude.

.. py:property:: reference_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveAttitude.reference_axes_name
    :type: str

    Ref Axes - the reference axes to be used in modeling this maneuver.


