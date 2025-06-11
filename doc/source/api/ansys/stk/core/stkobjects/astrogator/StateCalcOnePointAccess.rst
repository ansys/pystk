StateCalcOnePointAccess
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Access Calc objects.

.. py:currentmodule:: StateCalcOnePointAccess

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.set_base_selection`
              - Set the base selection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.aberration_type`
              - Get or set the type of aberration to use, if light time delay is applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.base_selection_type`
              - Get the base selection type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.base_selection`
              - Get the base selection object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.clock_host`
              - Get or set the object whose location is associated with time.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.signal_sense`
              - Sense of the signal at the base object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.target_object`
              - Get the target object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.time_delay_convergence_tolerance`
              - Get or set the time delay convergence tolerance, if light time delay is applied. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.use_light_time_delay`
              - Tue if light time delay is applied.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcOnePointAccess


Property detail
---------------

.. py:property:: aberration_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.aberration_type
    :type: AberrationType

    Get or set the type of aberration to use, if light time delay is applied.

.. py:property:: base_selection_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.base_selection_type
    :type: BaseSelection

    Get the base selection type.

.. py:property:: base_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.base_selection
    :type: ILinkToObject

    Get the base selection object.

.. py:property:: clock_host
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.clock_host
    :type: IvClockHost

    Get or set the object whose location is associated with time.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.signal_sense
    :type: IvTimeSense

    Sense of the signal at the base object.

.. py:property:: target_object
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.target_object
    :type: ILinkToObject

    Get the target object.

.. py:property:: time_delay_convergence_tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.time_delay_convergence_tolerance
    :type: float

    Get or set the time delay convergence tolerance, if light time delay is applied. Uses Time Dimension.

.. py:property:: use_light_time_delay
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.use_light_time_delay
    :type: bool

    Tue if light time delay is applied.


Method detail
-------------



.. py:method:: set_base_selection(self, selection: BaseSelection) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcOnePointAccess.set_base_selection

    Set the base selection.

    :Parameters:

        **selection** : :obj:`~BaseSelection`


    :Returns:

        :obj:`~None`












