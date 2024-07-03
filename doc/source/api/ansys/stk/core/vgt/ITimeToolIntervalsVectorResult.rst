ITimeToolIntervalsVectorResult
==============================

.. py:class:: ansys.stk.core.vgt.ITimeToolIntervalsVectorResult

   object
   
   Contains the results returned with IAgCrdnEventIntervalCollection.FindIntervalCollection method.

.. py:currentmodule:: ITimeToolIntervalsVectorResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolIntervalsVectorResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolIntervalsVectorResult.interval_collections`
              - A collection of interval collections.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolIntervalsVectorResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalsVectorResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: interval_collections
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalsVectorResult.interval_collections
    :type: ITimeToolIntervalVectorCollection

    A collection of interval collections.


