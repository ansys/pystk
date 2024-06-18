IVectorGeometryToolVectorFixedAtEpoch
=====================================

.. py:class:: IVectorGeometryToolVectorFixedAtEpoch

   object
   
   A vector based on another vector fixed at a specified epoch.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~epoch`
            * - :py:meth:`~source_vector`
            * - :py:meth:`~reference_axes`


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
    :type: "IAgCrdnVectorRefTo"

    Specify a source vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFixedAtEpoch.reference_axes
    :type: "IAgCrdnAxesRefTo"

    Specify a reference axes.


