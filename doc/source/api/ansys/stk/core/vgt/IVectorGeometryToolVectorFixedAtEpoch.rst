IVectorGeometryToolVectorFixedAtEpoch
=====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch

   object
   
   A vector based on another vector fixed at a specified epoch.

.. py:currentmodule:: IVectorGeometryToolVectorFixedAtEpoch

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch.epoch`
              - Specify an epoch.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch.source_vector`
              - Specify a source vector.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch.reference_axes`
              - Specify a reference axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorFixedAtEpoch


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch.epoch
    :type: typing.Any

    Specify an epoch.

.. py:property:: source_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch.source_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a source vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.


