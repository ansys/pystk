IVectorGeometryToolAxesTransformResult
======================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformResult

   object
   
   Contains the results returned with IAgCrdnAxes.TransformFrom method.

.. py:currentmodule:: IVectorGeometryToolAxesTransformResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTransformResult.is_valid`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesTransformResult.vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesTransformResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesTransformResult.vector
    :type: ICartesian3Vector

    The output vector in the current axes.


