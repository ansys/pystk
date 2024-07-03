IAdvCAT
=======

.. py:class:: ansys.stk.core.stkobjects.IAdvCAT

   object
   
   AgAdvCAT properties.

.. py:currentmodule:: IAdvCAT

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.compute`
              - Launch the close approach analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.get_available_objects`
              - Return a collection of available objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.get_primary_chosen_objects`
              - Return a collection of primary objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.get_secondary_chosen_objects`
              - Return a collection of secondary objects.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.time_period`
              - Get the time period for the close approach analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.threshold`
              - Distance threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.use_range_measure`
              - Enable/disable use range measure.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.display_ack_when_done`
              - Enable/disable displaying acknowledgement when done.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.primary_default_class`
              - Determine Ellipsoid Sizing method class.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.advanced`
              - Get AdvCAT advanced properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.graphics_3d`
              - Get AdvCAT advanced properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.primary_default_tangential`
              - Primary default value for Semi-major Axes Size along A.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.primary_default_cross_track`
              - Primary default value for Semi-major Axes Size along B.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.primary_default_normal`
              - Primary default value for Semi-major Axes Size along C.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.secondary_default_class`
              - Determine Ellipsoid Sizing method class.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.secondary_default_tangential`
              - Secondary default value for Semi-major Axes Size along A.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.secondary_default_cross_track`
              - Secondary default value for Semi-major Axes Size along B.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCAT.secondary_default_normal`
              - Secondary default value for Semi-major Axes Size along C.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAdvCAT


Property detail
---------------

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.time_period
    :type: ITimeToolEventIntervalSmartInterval

    Get the time period for the close approach analysis.

.. py:property:: threshold
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.threshold
    :type: float

    Distance threshold.

.. py:property:: use_range_measure
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.use_range_measure
    :type: bool

    Enable/disable use range measure.

.. py:property:: display_ack_when_done
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.display_ack_when_done
    :type: bool

    Enable/disable displaying acknowledgement when done.

.. py:property:: primary_default_class
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.primary_default_class
    :type: ADV_CAT_ELLIPSOID_CLASS

    Determine Ellipsoid Sizing method class.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.advanced
    :type: IAdvCATAdvanced

    Get AdvCAT advanced properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.graphics_3d
    :type: IAdvCATGraphics3D

    Get AdvCAT advanced properties.

.. py:property:: primary_default_tangential
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.primary_default_tangential
    :type: float

    Primary default value for Semi-major Axes Size along A.

.. py:property:: primary_default_cross_track
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.primary_default_cross_track
    :type: float

    Primary default value for Semi-major Axes Size along B.

.. py:property:: primary_default_normal
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.primary_default_normal
    :type: float

    Primary default value for Semi-major Axes Size along C.

.. py:property:: secondary_default_class
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.secondary_default_class
    :type: ADV_CAT_ELLIPSOID_CLASS

    Determine Ellipsoid Sizing method class.

.. py:property:: secondary_default_tangential
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.secondary_default_tangential
    :type: float

    Secondary default value for Semi-major Axes Size along A.

.. py:property:: secondary_default_cross_track
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.secondary_default_cross_track
    :type: float

    Secondary default value for Semi-major Axes Size along B.

.. py:property:: secondary_default_normal
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.secondary_default_normal
    :type: float

    Secondary default value for Semi-major Axes Size along C.


Method detail
-------------








.. py:method:: compute(self) -> None
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.compute

    Launch the close approach analysis.

    :Returns:

        :obj:`~None`

.. py:method:: get_available_objects(self) -> IAdvCATAvailableObjectCollection
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.get_available_objects

    Return a collection of available objects.

    :Returns:

        :obj:`~IAdvCATAvailableObjectCollection`

.. py:method:: get_primary_chosen_objects(self) -> IAdvCATChosenObjectCollection
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.get_primary_chosen_objects

    Return a collection of primary objects.

    :Returns:

        :obj:`~IAdvCATChosenObjectCollection`

.. py:method:: get_secondary_chosen_objects(self) -> IAdvCATChosenObjectCollection
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.get_secondary_chosen_objects

    Return a collection of secondary objects.

    :Returns:

        :obj:`~IAdvCATChosenObjectCollection`



















