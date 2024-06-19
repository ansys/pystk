IStateCalcRelMotion
===================

.. py:class:: IStateCalcRelMotion

   object
   
   Properties for a Relative Motion calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~origin_at_master`
            * - :py:meth:`~reference_selection`
            * - :py:meth:`~reference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcRelMotion


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelMotion.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: origin_at_master
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelMotion.origin_at_master
    :type: bool

    True if the origin is at the reference satellite, false if the origin is at the current satellite.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelMotion.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelMotion.reference
    :type: IAgLinkToObject

    Get the reference object.


