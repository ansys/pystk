IStateCalcDeltaDec
==================

.. py:class:: IStateCalcDeltaDec

   object
   
   Properties for a Delta Declination calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~reference_type`
            * - :py:meth:`~reference_body`


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


