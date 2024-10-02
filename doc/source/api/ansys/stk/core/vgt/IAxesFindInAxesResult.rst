IAxesFindInAxesResult
=====================

.. py:class:: ansys.stk.core.vgt.IAxesFindInAxesResult

   Contains the results returned with IAgCrdnAxes.FindInAxes method.

.. py:currentmodule:: IAxesFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAxesFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.IAxesFindInAxesResult.orientation`
              - The axes' orientation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAxesFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.IAxesFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.IAxesFindInAxesResult.orientation
    :type: IOrientation

    The axes' orientation.


