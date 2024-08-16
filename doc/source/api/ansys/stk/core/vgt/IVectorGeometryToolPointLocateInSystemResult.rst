IVectorGeometryToolPointLocateInSystemResult
============================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemResult

   Contains the results returned with IAgCrdnPoint.LocateInSystem method.

.. py:currentmodule:: IVectorGeometryToolPointLocateInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemResult.position`
              - The point position in the specified coordinate system.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointLocateInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemResult.position
    :type: ICartesian3Vector

    The point position in the specified coordinate system.


