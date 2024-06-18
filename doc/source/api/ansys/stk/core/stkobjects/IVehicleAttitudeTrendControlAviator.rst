IVehicleAttitudeTrendControlAviator
===================================

.. py:class:: IVehicleAttitudeTrendControlAviator

   object
   
   Trending controls for Aviator attitude.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_trends`
            * - :py:meth:`~time_tolerance`
            * - :py:meth:`~angle_rate_tolerance`
            * - :py:meth:`~kink_angle`
            * - :py:meth:`~use_yaw_trend`
            * - :py:meth:`~use_pitch_trend`
            * - :py:meth:`~use_roll_trend`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeTrendControlAviator


Property detail
---------------

.. py:property:: compute_trends
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTrendControlAviator.compute_trends
    :type: bool

    Flag controlling whether trends in the attitude angles should be detected and included as trending control times.

.. py:property:: time_tolerance
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTrendControlAviator.time_tolerance
    :type: float

    Minimum time allowed between each trending control time. Uses Time Dimension.

.. py:property:: angle_rate_tolerance
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTrendControlAviator.angle_rate_tolerance
    :type: float

    Minimum angle rate used to detect an increasing/decreasing trend. Rates lower than this treat the angle trend as flat. Uses AngleRate Dimension.

.. py:property:: kink_angle
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTrendControlAviator.kink_angle
    :type: float

    Minimum angle between the linear trends in the samples that indicates sufficient rate change to warrant creation of a trending control time. Uses Angle Dimension.

.. py:property:: use_yaw_trend
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTrendControlAviator.use_yaw_trend
    :type: bool

    Flag controlling whether yaw is considered when computing trends in attitude angles.

.. py:property:: use_pitch_trend
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTrendControlAviator.use_pitch_trend
    :type: bool

    Flag controlling whether pitch is considered when computing trends in attitude angles.

.. py:property:: use_roll_trend
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeTrendControlAviator.use_roll_trend
    :type: bool

    Flag controlling whether roll is considered when computing trends in attitude angles.


