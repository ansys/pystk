IAttitudeControlImpulsiveAttitude
=================================

.. py:class:: IAttitudeControlImpulsiveAttitude

   IAttitudeControlImpulsive
   
   Properties for the Attitude attitude control for an Impulsive Maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~delta_v_magnitude`
            * - :py:meth:`~reference_axes_name`
            * - :py:meth:`~orientation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlImpulsiveAttitude


Property detail
---------------

.. py:property:: delta_v_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveAttitude.delta_v_magnitude
    :type: float

    Gets or sets the size of the delta-V to be applied along the X axis - as defined by the selected axes and rotation. Uses Rate Dimension.

.. py:property:: reference_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveAttitude.reference_axes_name
    :type: str

    Ref Axes - the reference axes to be used in modeling this maneuver.

.. py:property:: orientation
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveAttitude.orientation
    :type: "IAgOrientation"

    Get the orientation of the attitude.


