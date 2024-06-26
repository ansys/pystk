IVectorGeometryToolPointLocateInSystemWithRateResult
====================================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult

   object
   
   Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

.. py:currentmodule:: IVectorGeometryToolPointLocateInSystemWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult.position`
              - The point position in the specified coordinate system.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult.velocity`
              - The point velocity in the specified coordinate system.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointLocateInSystemWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult.position
    :type: ICartesian3Vector

    The point position in the specified coordinate system.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult.velocity
    :type: ICartesian3Vector

    The point velocity in the specified coordinate system.


