IStateCalcDeltaDec
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec

   object
   
   Properties for a Delta Declination calculation object.

.. py:currentmodule:: IStateCalcDeltaDec

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec.reference_type`
              - Gets or sets the central body's reference type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec.reference_body`
              - Gets or sets the reference body of the component. Read only when the ReferenceType is eVACalcObjectCentralBodyReferenceParent.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcDeltaDec


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: reference_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec.reference_type
    :type: CALC_OBJECT_CENTRAL_BODY_REFERENCE

    Gets or sets the central body's reference type.

.. py:property:: reference_body
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaDec.reference_body
    :type: str

    Gets or sets the reference body of the component. Read only when the ReferenceType is eVACalcObjectCentralBodyReferenceParent.


