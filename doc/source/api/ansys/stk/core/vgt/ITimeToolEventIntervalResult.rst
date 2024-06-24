ITimeToolEventIntervalResult
============================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalResult

   object
   
   Contains the results returned with IAgCrdnEventIntervalList.FindIntervals method.

.. py:currentmodule:: ITimeToolEventIntervalResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalResult.is_valid`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalResult.interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: interval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalResult.interval
    :type: ITimeToolInterval

    An interval.


