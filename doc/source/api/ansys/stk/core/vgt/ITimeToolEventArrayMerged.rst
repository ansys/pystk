ITimeToolEventArrayMerged
=========================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventArrayMerged

   object
   
   Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

.. py:currentmodule:: ITimeToolEventArrayMerged

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayMerged.time_array_a`
              - The first time array.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArrayMerged.time_array_b`
              - The second time array.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArrayMerged


Property detail
---------------

.. py:property:: time_array_a
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayMerged.time_array_a
    :type: ITimeToolEventArray

    The first time array.

.. py:property:: time_array_b
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayMerged.time_array_b
    :type: ITimeToolEventArray

    The second time array.


