ICommSystem
===========

.. py:class:: ICommSystem

   object
   
   Provide access to the properties and methods defining an CommSystem object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_link_selection_criteria_type`
              - Set the link selection criteria by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~transmitters`
            * - :py:meth:`~receivers`
            * - :py:meth:`~interference_sources`
            * - :py:meth:`~calculate_interference`
            * - :py:meth:`~reference_bandwidth`
            * - :py:meth:`~constraining_role`
            * - :py:meth:`~time_period`
            * - :py:meth:`~step_size`
            * - :py:meth:`~save_mode`
            * - :py:meth:`~access_options`
            * - :py:meth:`~link_selection_criteria`
            * - :py:meth:`~graphics`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~include_receiver_interference_emitters`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICommSystem


Property detail
---------------

.. py:property:: transmitters
    :canonical: ansys.stk.core.stkobjects.ICommSystem.transmitters
    :type: IAgObjectLinkCollection

    Gets the transmitter collection.

.. py:property:: receivers
    :canonical: ansys.stk.core.stkobjects.ICommSystem.receivers
    :type: IAgObjectLinkCollection

    Gets the receiver collection.

.. py:property:: interference_sources
    :canonical: ansys.stk.core.stkobjects.ICommSystem.interference_sources
    :type: IAgObjectLinkCollection

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
    :type: IAgCrdnEventIntervalSmartInterval

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
    :type: IAgCommSystemAccessOptions

    Get the access options.

.. py:property:: link_selection_criteria
    :canonical: ansys.stk.core.stkobjects.ICommSystem.link_selection_criteria
    :type: IAgCommSystemLinkSelectionCriteria

    Get the link selection criteria.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ICommSystem.graphics
    :type: IAgCommSystemGraphics

    Get the 2D Graphics properties for the CommSystem.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ICommSystem.graphics_3d
    :type: IAgCommSystemVO

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






