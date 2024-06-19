IStateCalcRelGroundTrackError
=============================

.. py:class:: IStateCalcRelGroundTrackError

   object
   
   Properties for a RelGroundTrackError calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~direction`
            * - :py:meth:`~signed`
            * - :py:meth:`~reference_selection`
            * - :py:meth:`~reference`


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
    :type: IAgLinkToObject

    Get the reference object.


