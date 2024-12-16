AttitudeControlFiniteAttitude
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The attitude attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.attitude_update`
              - How and when the attitude will be updated.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.reference_axes_name`
              - Ref Axes - the reference axes to be used in modeling this maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.orientation`
              - Get the orientation of the attitude.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlFiniteAttitude


Property detail
---------------

.. py:property:: attitude_update
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.attitude_update
    :type: AttitudeUpdate

    How and when the attitude will be updated.

.. py:property:: reference_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.reference_axes_name
    :type: str

    Ref Axes - the reference axes to be used in modeling this maneuver.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteAttitude.orientation
    :type: IOrientation

    Get the orientation of the attitude.


