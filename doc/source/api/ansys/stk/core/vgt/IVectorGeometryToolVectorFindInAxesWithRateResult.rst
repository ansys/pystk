IVectorGeometryToolVectorFindInAxesWithRateResult
=================================================

.. py:class:: IVectorGeometryToolVectorFindInAxesWithRateResult

   object
   
   Contains the results returned with IAgCrdnVector.FindInAxesWithRate method.

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
            * - :py:meth:`~rate`


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
    :type: "IAgCartesian3Vector"

    The vector in a specified axes.

.. py:property:: rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorFindInAxesWithRateResult.rate
    :type: "IAgCartesian3Vector"

    The vector rate in a specified axes.


