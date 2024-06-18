IVectorGeometryToolAxesFixedAtEpoch
===================================

.. py:class:: IVectorGeometryToolAxesFixedAtEpoch

   object
   
   Axes based on another set fixed at a specified epoch.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~source_axes`
            * - :py:meth:`~reference_axes`
            * - :py:meth:`~epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesFixedAtEpoch


Property detail
---------------

.. py:property:: source_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFixedAtEpoch.source_axes
    :type: "IAgCrdnAxesRefTo"

    Specify a source axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFixedAtEpoch.reference_axes
    :type: "IAgCrdnAxesRefTo"

    Specify a reference axes.

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFixedAtEpoch.epoch
    :type: typing.Any

    Specify an epoch.


