CRDN_VOLUME_TYPE
================

.. py:class:: ansys.stk.core.vgt.CRDN_VOLUME_TYPE

   IntEnum


.. py:currentmodule:: CRDN_VOLUME_TYPE

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

            * - :py:attr:`~FROM_GRID`
              - volume type from grid (Grid Bounding Volume).

            * - :py:attr:`~FROM_CALC`
              - volume type from calc (Spatial Calculation Bounds).

            * - :py:attr:`~FROM_TIME_SATISFACTION`
              - volume type from time satisfaction (Valid Time At Location).

            * - :py:attr:`~FROM_CONDITION`
              - volume type from condition (Condition At Location).

            * - :py:attr:`~INVIEW`
              - volume type Inview (Access To Location).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_VOLUME_TYPE


