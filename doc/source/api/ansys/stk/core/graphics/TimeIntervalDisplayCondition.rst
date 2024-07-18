TimeIntervalDisplayCondition
============================

.. py:class:: ansys.stk.core.graphics.TimeIntervalDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

.. py:currentmodule:: TimeIntervalDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.TimeIntervalDisplayCondition.minimum_time`
              - Gets or sets the minimum time of the inclusive time interval.
            * - :py:attr:`~ansys.stk.core.graphics.TimeIntervalDisplayCondition.maximum_time`
              - Gets or sets the maximum time of the inclusive time interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import TimeIntervalDisplayCondition


Property detail
---------------

.. py:property:: minimum_time
    :canonical: ansys.stk.core.graphics.TimeIntervalDisplayCondition.minimum_time
    :type: IDate

    Gets or sets the minimum time of the inclusive time interval.

.. py:property:: maximum_time
    :canonical: ansys.stk.core.graphics.TimeIntervalDisplayCondition.maximum_time
    :type: IDate

    Gets or sets the maximum time of the inclusive time interval.


