IStateCalcOnePointAccess
========================

.. py:class:: IStateCalcOnePointAccess

   object
   
   Properties for an Access calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_base_selection`
              - Set the base selection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aberration_type`
            * - :py:meth:`~base_selection_type`
            * - :py:meth:`~base_selection`
            * - :py:meth:`~clock_host`
            * - :py:meth:`~signal_sense`
            * - :py:meth:`~target_object`
            * - :py:meth:`~time_delay_convergence_tolerance`
            * - :py:meth:`~use_light_time_delay`


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
    :type: IAgLinkToObject

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
    :type: IAgLinkToObject

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












