IAdvCAT
=======

.. py:class:: IAdvCAT

   object
   
   AgAdvCAT properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute`
              - Launch the close approach analysis.
            * - :py:meth:`~get_available_objects`
              - Return a collection of available objects.
            * - :py:meth:`~get_primary_chosen_objects`
              - Return a collection of primary objects.
            * - :py:meth:`~get_secondary_chosen_objects`
              - Return a collection of secondary objects.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~time_period`
            * - :py:meth:`~threshold`
            * - :py:meth:`~use_range_measure`
            * - :py:meth:`~display_ack_when_done`
            * - :py:meth:`~primary_default_class`
            * - :py:meth:`~advanced`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~primary_default_tangential`
            * - :py:meth:`~primary_default_cross_track`
            * - :py:meth:`~primary_default_normal`
            * - :py:meth:`~secondary_default_class`
            * - :py:meth:`~secondary_default_tangential`
            * - :py:meth:`~secondary_default_cross_track`
            * - :py:meth:`~secondary_default_normal`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAdvCAT


Property detail
---------------

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.time_period
    :type: IAgCrdnEventIntervalSmartInterval

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
    :type: IAgAdvCATAdvanced

    Get AdvCAT advanced properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IAdvCAT.graphics_3d
    :type: IAgAdvCATVO

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



















