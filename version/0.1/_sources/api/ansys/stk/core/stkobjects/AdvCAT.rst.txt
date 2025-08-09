AdvCAT
======

.. py:class:: ansys.stk.core.stkobjects.AdvCAT

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   AdvCAT properties.

.. py:currentmodule:: AdvCAT

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.compute`
              - Launch the close approach analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.get_available_objects`
              - Return a collection of available objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.get_primary_chosen_objects`
              - Return a collection of primary objects.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.get_secondary_chosen_objects`
              - Return a collection of secondary objects.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.time_period`
              - Get the time period for the close approach analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.threshold`
              - Distance threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.use_range_measure`
              - Enable/disable use range measure.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.display_acknowledgement_when_done`
              - Enable/disable displaying acknowledgement when done.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.primary_default_class`
              - Determine Ellipsoid Sizing method class.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.advanced`
              - Get AdvCAT advanced properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.graphics_3d`
              - Get AdvCAT advanced properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.primary_default_tangential`
              - Primary default value for Semi-major Axes Size along A.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.primary_default_cross_track`
              - Primary default value for Semi-major Axes Size along B.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.primary_default_normal`
              - Primary default value for Semi-major Axes Size along C.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.secondary_default_class`
              - Determine Ellipsoid Sizing method class.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.secondary_default_tangential`
              - Secondary default value for Semi-major Axes Size along A.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.secondary_default_cross_track`
              - Secondary default value for Semi-major Axes Size along B.
            * - :py:attr:`~ansys.stk.core.stkobjects.AdvCAT.secondary_default_normal`
              - Secondary default value for Semi-major Axes Size along C.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AdvCAT


Property detail
---------------

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.AdvCAT.time_period
    :type: ITimeToolTimeIntervalSmartInterval

    Get the time period for the close approach analysis.

.. py:property:: threshold
    :canonical: ansys.stk.core.stkobjects.AdvCAT.threshold
    :type: float

    Distance threshold.

.. py:property:: use_range_measure
    :canonical: ansys.stk.core.stkobjects.AdvCAT.use_range_measure
    :type: bool

    Enable/disable use range measure.

.. py:property:: display_acknowledgement_when_done
    :canonical: ansys.stk.core.stkobjects.AdvCAT.display_acknowledgement_when_done
    :type: bool

    Enable/disable displaying acknowledgement when done.

.. py:property:: primary_default_class
    :canonical: ansys.stk.core.stkobjects.AdvCAT.primary_default_class
    :type: AdvCATEllipsoidClassType

    Determine Ellipsoid Sizing method class.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.AdvCAT.advanced
    :type: AdvCATAdvancedSettings

    Get AdvCAT advanced properties.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.AdvCAT.graphics_3d
    :type: AdvCATGraphics3D

    Get AdvCAT advanced properties.

.. py:property:: primary_default_tangential
    :canonical: ansys.stk.core.stkobjects.AdvCAT.primary_default_tangential
    :type: float

    Primary default value for Semi-major Axes Size along A.

.. py:property:: primary_default_cross_track
    :canonical: ansys.stk.core.stkobjects.AdvCAT.primary_default_cross_track
    :type: float

    Primary default value for Semi-major Axes Size along B.

.. py:property:: primary_default_normal
    :canonical: ansys.stk.core.stkobjects.AdvCAT.primary_default_normal
    :type: float

    Primary default value for Semi-major Axes Size along C.

.. py:property:: secondary_default_class
    :canonical: ansys.stk.core.stkobjects.AdvCAT.secondary_default_class
    :type: AdvCATEllipsoidClassType

    Determine Ellipsoid Sizing method class.

.. py:property:: secondary_default_tangential
    :canonical: ansys.stk.core.stkobjects.AdvCAT.secondary_default_tangential
    :type: float

    Secondary default value for Semi-major Axes Size along A.

.. py:property:: secondary_default_cross_track
    :canonical: ansys.stk.core.stkobjects.AdvCAT.secondary_default_cross_track
    :type: float

    Secondary default value for Semi-major Axes Size along B.

.. py:property:: secondary_default_normal
    :canonical: ansys.stk.core.stkobjects.AdvCAT.secondary_default_normal
    :type: float

    Secondary default value for Semi-major Axes Size along C.


Method detail
-------------








.. py:method:: compute(self) -> None
    :canonical: ansys.stk.core.stkobjects.AdvCAT.compute

    Launch the close approach analysis.

    :Returns:

        :obj:`~None`

.. py:method:: get_available_objects(self) -> AdvCATAvailableObjectCollection
    :canonical: ansys.stk.core.stkobjects.AdvCAT.get_available_objects

    Return a collection of available objects.

    :Returns:

        :obj:`~AdvCATAvailableObjectCollection`

.. py:method:: get_primary_chosen_objects(self) -> AdvCATChosenObjectCollection
    :canonical: ansys.stk.core.stkobjects.AdvCAT.get_primary_chosen_objects

    Return a collection of primary objects.

    :Returns:

        :obj:`~AdvCATChosenObjectCollection`

.. py:method:: get_secondary_chosen_objects(self) -> AdvCATChosenObjectCollection
    :canonical: ansys.stk.core.stkobjects.AdvCAT.get_secondary_chosen_objects

    Return a collection of secondary objects.

    :Returns:

        :obj:`~AdvCATChosenObjectCollection`



















