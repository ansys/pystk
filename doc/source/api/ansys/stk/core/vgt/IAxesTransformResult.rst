IAxesTransformResult
====================

.. py:class:: ansys.stk.core.vgt.IAxesTransformResult

   Contains the results returned with IAgCrdnAxes.TransformFrom method.

.. py:currentmodule:: IAxesTransformResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAxesTransformResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.IAxesTransformResult.vector`
              - The output vector in the current axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAxesTransformResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IAxesTransformResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IAxesTransformResult.vector
    :type: ICartesian3Vector

    The output vector in the current axes.


