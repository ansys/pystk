TimeToolEventArrayMerged
========================

.. py:class:: ansys.stk.core.vgt.TimeToolEventArrayMerged

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEventArray`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Defined by merging times from two other arrays by creating a union of bounding intervals from two constituent arrays. If some intervals overlap, then within overlap times from both arrays are merged together.

.. py:currentmodule:: TimeToolEventArrayMerged

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventArrayMerged.time_array_a`
              - The first time array.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventArrayMerged.time_array_b`
              - The second time array.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventArrayMerged


Property detail
---------------

.. py:property:: time_array_a
    :canonical: ansys.stk.core.vgt.TimeToolEventArrayMerged.time_array_a
    :type: ITimeToolEventArray

    The first time array.

.. py:property:: time_array_b
    :canonical: ansys.stk.core.vgt.TimeToolEventArrayMerged.time_array_b
    :type: ITimeToolEventArray

    The second time array.


