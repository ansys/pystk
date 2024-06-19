IVectorGeometryToolPointLocateInSystemResult
============================================

.. py:class:: IVectorGeometryToolPointLocateInSystemResult

   object
   
   Contains the results returned with IAgCrdnPoint.LocateInSystem method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~position`


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
    :type: IAgCartesian3Vector

    The point position in the specified coordinate system.


