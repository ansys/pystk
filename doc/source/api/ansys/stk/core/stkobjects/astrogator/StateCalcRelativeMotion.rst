StateCalcRelativeMotion
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Relative Motion Calc objects.

.. py:currentmodule:: StateCalcRelativeMotion

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.origin_at_chief`
              - True if the origin is at the reference satellite, false if the origin is at the current satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.reference_selection`
              - Get or set the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.reference`
              - Get the reference object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcRelativeMotion


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: origin_at_chief
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.origin_at_chief
    :type: bool

    True if the origin is at the reference satellite, false if the origin is at the current satellite.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.reference_selection
    :type: CalculationObjectReference

    Get or set the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeMotion.reference
    :type: ILinkToObject

    Get the reference object.


