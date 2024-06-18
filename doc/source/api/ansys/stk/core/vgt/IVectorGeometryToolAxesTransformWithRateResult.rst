IVectorGeometryToolAxesTransformWithRateResult
==============================================

.. py:class:: IVectorGeometryToolAxesTransformWithRateResult

   object
   
   Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~vector`
            * - :py:meth:`~velocity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.vector
    :type: "IAgCartesian3Vector"

    The output vector in the current axes.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformWithRateResult.velocity
    :type: "IAgCartesian3Vector"

    The vector velocity.


