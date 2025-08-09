StateCalcReferenceRadius
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Reference Radius Calc objects.

.. py:currentmodule:: StateCalcReferenceRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius.reference_radius_source`
              - Get or set the source for the reference radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius.gravity_filename`
              - Source for the reference radius if RefRadSource is set to Gravity File.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcReferenceRadius


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: reference_radius_source
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius.reference_radius_source
    :type: ReferenceRadiusSource

    Get or set the source for the reference radius.

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcReferenceRadius.gravity_filename
    :type: str

    Source for the reference radius if RefRadSource is set to Gravity File.


