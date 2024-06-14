IVectorGeometryToolAxesFindInAxesResult
=======================================

.. py:class:: IVectorGeometryToolAxesFindInAxesResult

   object
   
   Contains the results returned with IAgCrdnAxes.FindInAxes method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~orientation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesResult.orientation
    :type: "IAgOrientation"

    The axes' orientation.


