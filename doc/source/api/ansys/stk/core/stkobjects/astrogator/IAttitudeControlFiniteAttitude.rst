IAttitudeControlFiniteAttitude
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude

   IAttitudeControlFinite
   
   Properties for the Attitude attitude control for a Finite Maneuver.

.. py:currentmodule:: IAttitudeControlFiniteAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude.attitude_update`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude.reference_axes_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude.orientation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlFiniteAttitude


Property detail
---------------

.. py:property:: attitude_update
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude.attitude_update
    :type: ATTITUDE_UPDATE

    How and when the attitude will be updated.

.. py:property:: reference_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude.reference_axes_name
    :type: str

    Ref Axes - the reference axes to be used in modeling this maneuver.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteAttitude.orientation
    :type: IOrientation

    Get the orientation of the attitude.


