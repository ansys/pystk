IVectorGeometryToolAxesFindInAxesResult
=======================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesResult

   Contains the results returned with IAgCrdnAxes.FindInAxes method.

.. py:currentmodule:: IVectorGeometryToolAxesFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesFindInAxesResult.orientation`
              - The axes' orientation.


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
    :type: IOrientation

    The axes' orientation.


