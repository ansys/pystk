CommSystem
==========

.. py:class:: ansys.stk.core.stkobjects.CommSystem

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Class defining a CommSystem object.

.. py:currentmodule:: CommSystem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.set_link_selection_criteria_type`
              - Set the link selection criteria by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.transmitters`
              - Gets the transmitter collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.receivers`
              - Gets the receiver collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.interference_sources`
              - Gets the interference source collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.calculate_interference`
              - Gets or sets the option for calculating interference.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.reference_bandwidth`
              - Gets or sets the reference bandwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.constraining_role`
              - Gets or sets the constraining role.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.time_period`
              - Allows configuring the time period.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.step_size`
              - Gets or sets the step size.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.save_mode`
              - Gets or sets the save mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.access_options`
              - Get the access options.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.link_selection_criteria`
              - Get the link selection criteria.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.graphics`
              - Get the 2D Graphics properties for the CommSystem.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.graphics_3d`
              - Get the 3D Graphics properties for the CommSystem.
            * - :py:attr:`~ansys.stk.core.stkobjects.CommSystem.include_receiver_interference_emitters`
              - Gets or sets whether the emitters from each receiver is included in their interference computation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CommSystem


Property detail
---------------

.. py:property:: transmitters
    :canonical: ansys.stk.core.stkobjects.CommSystem.transmitters
    :type: ObjectLinkCollection

    Gets the transmitter collection.

.. py:property:: receivers
    :canonical: ansys.stk.core.stkobjects.CommSystem.receivers
    :type: ObjectLinkCollection

    Gets the receiver collection.

.. py:property:: interference_sources
    :canonical: ansys.stk.core.stkobjects.CommSystem.interference_sources
    :type: ObjectLinkCollection

    Gets the interference source collection.

.. py:property:: calculate_interference
    :canonical: ansys.stk.core.stkobjects.CommSystem.calculate_interference
    :type: bool

    Gets or sets the option for calculating interference.

.. py:property:: reference_bandwidth
    :canonical: ansys.stk.core.stkobjects.CommSystem.reference_bandwidth
    :type: CommSystemReferenceBandwidth

    Gets or sets the reference bandwidth.

.. py:property:: constraining_role
    :canonical: ansys.stk.core.stkobjects.CommSystem.constraining_role
    :type: CommSystemConstrainingRole

    Gets or sets the constraining role.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.CommSystem.time_period
    :type: ITimeToolTimeIntervalSmartInterval

    Allows configuring the time period.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.CommSystem.step_size
    :type: float

    Gets or sets the step size.

.. py:property:: save_mode
    :canonical: ansys.stk.core.stkobjects.CommSystem.save_mode
    :type: CommSystemSaveMode

    Gets or sets the save mode.

.. py:property:: access_options
    :canonical: ansys.stk.core.stkobjects.CommSystem.access_options
    :type: CommSystemAccessOptions

    Get the access options.

.. py:property:: link_selection_criteria
    :canonical: ansys.stk.core.stkobjects.CommSystem.link_selection_criteria
    :type: ICommSystemLinkSelectionCriteria

    Get the link selection criteria.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.CommSystem.graphics
    :type: CommSystemGraphics

    Get the 2D Graphics properties for the CommSystem.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.CommSystem.graphics_3d
    :type: CommSystemGraphics3D

    Get the 3D Graphics properties for the CommSystem.

.. py:property:: include_receiver_interference_emitters
    :canonical: ansys.stk.core.stkobjects.CommSystem.include_receiver_interference_emitters
    :type: bool

    Gets or sets whether the emitters from each receiver is included in their interference computation.


Method detail
-------------
















.. py:method:: set_link_selection_criteria_type(self, value: CommSystemLinkSelectionCriteriaType) -> None
    :canonical: ansys.stk.core.stkobjects.CommSystem.set_link_selection_criteria_type

    Set the link selection criteria by name.

    :Parameters:

    **value** : :obj:`~CommSystemLinkSelectionCriteriaType`

    :Returns:

        :obj:`~None`






