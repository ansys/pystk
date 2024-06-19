POLYLINE_TYPE
=============

.. py:class:: POLYLINE_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~LINES`
              - Every two positions define a line segment. Line segments are not required to be connected to each other.

            * - :py:attr:`~LINE_STRIP`
              - After the first position, each additional position defines a line segment from the previous position to the current position.

            * - :py:attr:`~POINTS`
              - Lines are drawn as points.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import POLYLINE_TYPE


