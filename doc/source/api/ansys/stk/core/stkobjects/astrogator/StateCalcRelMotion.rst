StateCalcRelMotion
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Relative Motion Calc objects.

.. py:currentmodule:: StateCalcRelMotion

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.origin_at_master`
              - True if the origin is at the reference satellite, false if the origin is at the current satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.reference`
              - Get the reference object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcRelMotion


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: origin_at_master
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.origin_at_master
    :type: bool

    True if the origin is at the reference satellite, false if the origin is at the current satellite.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelMotion.reference
    :type: ILinkToObject

    Get the reference object.


