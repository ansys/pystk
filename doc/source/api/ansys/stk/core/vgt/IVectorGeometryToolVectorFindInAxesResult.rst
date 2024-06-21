IVectorGeometryToolVectorFindInAxesResult
=========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesResult

   object
   
   Contains the results returned with IAgCrdnVector.FindInAxes method.

.. py:currentmodule:: IVectorGeometryToolVectorFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesResult.is_valid`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesResult.vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesResult.vector
    :type: ICartesian3Vector

    The vector in a specified axes.


