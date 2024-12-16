SensorAltitudeCrossingSideType
==============================

.. py:class:: ansys.stk.core.stkobjects.SensorAltitudeCrossingSideType

   IntEnum


.. py:currentmodule:: SensorAltitudeCrossingSideType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown.

            * - :py:attr:`~BOTH_SIDES`
              - Both Sides - if the Direction option for altitude crossing permits front and back crossings, both are computed and displayed in the 2D Graphics window.

            * - :py:attr:`~ONE_SIDE`
              - One Side - only the first crossing that satisfies the Direction option for altitude crossing is computed and displayed in the 2D Graphics window.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorAltitudeCrossingSideType


