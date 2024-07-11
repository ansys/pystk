IStateCalcRelGroundTrackError
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError

   object
   
   Properties for a RelGroundTrackError calculation object.

.. py:currentmodule:: IStateCalcRelGroundTrackError

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.direction`
              - Gets or sets the direction to search for the desired value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.signed`
              - True if signed based on RxV.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.reference`
              - Get the reference object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcRelGroundTrackError


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.direction
    :type: CALC_OBJECT_DIRECTION

    Gets or sets the direction to search for the desired value.

.. py:property:: signed
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.signed
    :type: bool

    True if signed based on RxV.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelGroundTrackError.reference
    :type: ILinkToObject

    Get the reference object.


