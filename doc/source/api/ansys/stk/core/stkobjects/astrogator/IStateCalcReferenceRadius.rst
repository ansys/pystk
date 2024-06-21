IStateCalcReferenceRadius
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius

   object
   
   Properties for a Reference Radius calculation object.

.. py:currentmodule:: IStateCalcReferenceRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius.central_body_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius.reference_radius_source`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius.gravity_filename`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcReferenceRadius


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: reference_radius_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius.reference_radius_source
    :type: REFERENCE_RADIUS_SOURCE

    Gets or sets the source for the reference radius.

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcReferenceRadius.gravity_filename
    :type: str

    Source for the reference radius if RefRadSource is set to Gravity File.


