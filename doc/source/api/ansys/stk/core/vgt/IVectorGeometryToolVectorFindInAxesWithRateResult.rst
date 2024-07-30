IVectorGeometryToolVectorFindInAxesWithRateResult
=================================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult

   object
   
   Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

.. py:currentmodule:: IVectorGeometryToolVectorFindInAxesWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult.vector`
              - The vector in a specified axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult.rate`
              - The vector rate in a specified axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorFindInAxesWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult.vector
    :type: ICartesian3Vector

    The vector in a specified axes.

.. py:property:: rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult.rate
    :type: ICartesian3Vector

    The vector rate in a specified axes.


