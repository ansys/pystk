ITimeIntervalDisplayCondition
=============================

.. py:class:: ITimeIntervalDisplayCondition

   object
   
   Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~minimum_time`
            * - :py:meth:`~maximum_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITimeIntervalDisplayCondition


Property detail
---------------

.. py:property:: minimum_time
    :canonical: ansys.stk.core.graphics.ITimeIntervalDisplayCondition.minimum_time
    :type: "IAgDate"

    Gets or sets the minimum time of the inclusive time interval.

.. py:property:: maximum_time
    :canonical: ansys.stk.core.graphics.ITimeIntervalDisplayCondition.maximum_time
    :type: "IAgDate"

    Gets or sets the maximum time of the inclusive time interval.


