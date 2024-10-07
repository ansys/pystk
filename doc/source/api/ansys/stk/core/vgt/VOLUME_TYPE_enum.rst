VOLUME_TYPE
===========

.. py:class:: ansys.stk.core.vgt.VOLUME_TYPE

   IntEnum


.. py:currentmodule:: VOLUME_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported volume.

            * - :py:attr:`~COMBINED`
              - volume type combined.

            * - :py:attr:`~LIGHTING`
              - volume type lighting.

            * - :py:attr:`~OVER_TIME`
              - volume type over time.

            * - :py:attr:`~GRID_BOUNDING_VOLUME`
              - volume type from grid (Grid Bounding Volume).

            * - :py:attr:`~SPATIAL_CALCULATION_BOUNDS`
              - volume type from calc (Spatial Calculation Bounds).

            * - :py:attr:`~VALID_TIME_AT_LOCATION`
              - volume type from time satisfaction (Valid Time At Location).

            * - :py:attr:`~CONDITION_AT_LOCATION`
              - volume type from condition (Condition At Location).

            * - :py:attr:`~ACCESS_TO_LOCATION`
              - volume type Inview (Access To Location).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VOLUME_TYPE


