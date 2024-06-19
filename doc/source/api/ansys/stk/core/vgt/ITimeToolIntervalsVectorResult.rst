ITimeToolIntervalsVectorResult
==============================

.. py:class:: ITimeToolIntervalsVectorResult

   object
   
   Contains the results returned with IAgCrdnEventIntervalCollection.FindIntervalCollection method.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_valid`
            * - :py:meth:`~interval_collections`


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
    :type: IAgCrdnIntervalVectorCollection

    A collection of interval collections.


