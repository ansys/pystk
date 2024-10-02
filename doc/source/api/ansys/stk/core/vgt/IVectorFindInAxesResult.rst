IVectorFindInAxesResult
=======================

.. py:class:: ansys.stk.core.vgt.IVectorFindInAxesResult

   Contains the results returned with IAgCrdnVector.FindInAxes method.

.. py:currentmodule:: IVectorFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorFindInAxesResult.vector`
              - The vector in a specified axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IVectorFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.IVectorFindInAxesResult.vector
    :type: ICartesian3Vector

    The vector in a specified axes.


