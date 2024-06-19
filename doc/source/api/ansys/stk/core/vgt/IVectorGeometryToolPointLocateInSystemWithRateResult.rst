IVectorGeometryToolPointLocateInSystemWithRateResult
====================================================

.. py:class:: IVectorGeometryToolPointLocateInSystemWithRateResult

   object
   
   Contains the results returned with IAgCrdnPoint.LocateInSystemWithRate method.

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
            * - :py:meth:`~velocity`


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
    :type: IAgCartesian3Vector

    The point position in the specified coordinate system.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLocateInSystemWithRateResult.velocity
    :type: IAgCartesian3Vector

    The point velocity in the specified coordinate system.


