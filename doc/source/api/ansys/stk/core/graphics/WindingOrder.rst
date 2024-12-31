WindingOrder
============

.. py:class:: ansys.stk.core.graphics.WindingOrder

   IntEnum


.. py:currentmodule:: WindingOrder

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~COUNTER_CLOCKWISE`
              - Positions or triangles are defined in counter-clockwise order.

            * - :py:attr:`~CLOCKWISE`
              - Positions or triangles are defined in clockwise order.

            * - :py:attr:`~COMPUTE`
              - The winding order is unknown and should be computed. For best performance, only use this value if you do not know the actual winding order.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import WindingOrder


