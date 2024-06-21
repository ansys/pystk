INTERSECTION_TYPE
=================

.. py:class:: ansys.stk.core.stkobjects.INTERSECTION_TYPE

   IntEnum


.. py:currentmodule:: INTERSECTION_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CENTRAL_BODY`
              - Central body: modifies the field of view of the sensor to account for its intersections with the central body.

            * - :py:attr:`~NONE`
              - None: does not modify the field of view of the sensor by ignoring any possible intersections.

            * - :py:attr:`~TERRAIN`
              - Terrain: modifies the field of view of the sensor to account for its intersections with the central body and terrain, defined by its North, South, East and West boundaries.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import INTERSECTION_TYPE


