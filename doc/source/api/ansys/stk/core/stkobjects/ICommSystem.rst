ICommSystem
===========

.. py:class:: ansys.stk.core.stkobjects.ICommSystem

   object
   
   Provide access to the properties and methods defining an CommSystem object.

.. py:currentmodule:: ICommSystem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.set_link_selection_criteria_type`
              - Set the link selection criteria by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.transmitters`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.receivers`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.interference_sources`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.calculate_interference`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.reference_bandwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.constraining_role`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.time_period`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.step_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.save_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.access_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.link_selection_criteria`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.graphics`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.graphics_3d`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICommSystem.include_receiver_interference_emitters`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICommSystem


Property detail
---------------

.. py:property:: transmitters
    :canonical: ansys.stk.core.stkobjects.ICommSystem.transmitters
    :type: IObjectLinkCollection

    Gets the transmitter collection.

.. py:property:: receivers
    :canonical: ansys.stk.core.stkobjects.ICommSystem.receivers
    :type: IObjectLinkCollection

    Gets the receiver collection.

.. py:property:: interference_sources
    :canonical: ansys.stk.core.stkobjects.ICommSystem.interference_sources
    :type: IObjectLinkCollection

    Gets the interference source collection.

.. py:property:: calculate_interference
    :canonical: ansys.stk.core.stkobjects.ICommSystem.calculate_interference
    :type: bool

    Gets or sets the option for calculating interference.

.. py:property:: reference_bandwidth
    :canonical: ansys.stk.core.stkobjects.ICommSystem.reference_bandwidth
    :type: COMM_SYSTEM_REFERENCE_BANDWIDTH

    Gets or sets the reference bandwidth.

.. py:property:: constraining_role
    :canonical: ansys.stk.core.stkobjects.ICommSystem.constraining_role
    :type: COMM_SYSTEM_CONSTRAINING_ROLE

    Gets or sets the constraining role.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.ICommSystem.time_period
    :type: ITimeToolEventIntervalSmartInterval

    Allows configuring the time period.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.ICommSystem.step_size
    :type: float

    Gets or sets the step size.

.. py:property:: save_mode
    :canonical: ansys.stk.core.stkobjects.ICommSystem.save_mode
    :type: COMM_SYSTEM_SAVE_MODE

    Gets or sets the save mode.

.. py:property:: access_options
    :canonical: ansys.stk.core.stkobjects.ICommSystem.access_options
    :type: ICommSystemAccessOptions

    Get the access options.

.. py:property:: link_selection_criteria
    :canonical: ansys.stk.core.stkobjects.ICommSystem.link_selection_criteria
    :type: ICommSystemLinkSelectionCriteria

    Get the link selection criteria.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ICommSystem.graphics
    :type: ICommSystemGraphics

    Get the 2D Graphics properties for the CommSystem.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ICommSystem.graphics_3d
    :type: ICommSystemGraphics3D

    Get the 3D Graphics properties for the CommSystem.

.. py:property:: include_receiver_interference_emitters
    :canonical: ansys.stk.core.stkobjects.ICommSystem.include_receiver_interference_emitters
    :type: bool

    Gets or sets whether the emitters from each receiver is included in their interference computation.


Method detail
-------------
















.. py:method:: set_link_selection_criteria_type(self, val: COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.ICommSystem.set_link_selection_criteria_type

    Set the link selection criteria by name.

    :Parameters:

    **val** : :obj:`~COMM_SYSTEM_LINK_SELECTION_CRITERIA_TYPE`

    :Returns:

        :obj:`~None`






