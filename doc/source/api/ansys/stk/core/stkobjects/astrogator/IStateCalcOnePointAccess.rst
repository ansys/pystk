IStateCalcOnePointAccess
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess

   object
   
   Properties for an Access calculation object.

.. py:currentmodule:: IStateCalcOnePointAccess

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.set_base_selection`
              - Set the base selection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.aberration_type`
              - Gets or sets the type of aberration to use, if light time delay is applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.base_selection_type`
              - Get the base selection type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.base_selection`
              - Get the base selection object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.clock_host`
              - Gets or sets the object whose location is associated with time.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.signal_sense`
              - Sense of the signal at the base object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.target_object`
              - Get the target object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.time_delay_convergence_tolerance`
              - Gets or sets the time delay convergence tolerance, if light time delay is applied. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.use_light_time_delay`
              - Tue if light time delay is applied.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcOnePointAccess


Property detail
---------------

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.aberration_type
    :type: ABERRATION_TYPE

    Gets or sets the type of aberration to use, if light time delay is applied.

.. py:property:: base_selection_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.base_selection_type
    :type: BASE_SELECTION

    Get the base selection type.

.. py:property:: base_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.base_selection
    :type: ILinkToObject

    Get the base selection object.

.. py:property:: clock_host
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.clock_host
    :type: IV_CLOCK_HOST

    Gets or sets the object whose location is associated with time.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.signal_sense
    :type: IV_TIME_SENSE

    Sense of the signal at the base object.

.. py:property:: target_object
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.target_object
    :type: ILinkToObject

    Get the target object.

.. py:property:: time_delay_convergence_tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.time_delay_convergence_tolerance
    :type: float

    Gets or sets the time delay convergence tolerance, if light time delay is applied. Uses Time Dimension.

.. py:property:: use_light_time_delay
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.use_light_time_delay
    :type: bool

    Tue if light time delay is applied.


Method detail
-------------



.. py:method:: set_base_selection(self, selection: BASE_SELECTION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcOnePointAccess.set_base_selection

    Set the base selection.

    :Parameters:

    **selection** : :obj:`~BASE_SELECTION`

    :Returns:

        :obj:`~None`












