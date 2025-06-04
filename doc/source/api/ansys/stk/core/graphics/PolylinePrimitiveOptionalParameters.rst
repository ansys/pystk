PolylinePrimitiveOptionalParameters
===================================

.. py:class:: ansys.stk.core.graphics.PolylinePrimitiveOptionalParameters

   Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

.. py:currentmodule:: PolylinePrimitiveOptionalParameters

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PolylinePrimitiveOptionalParameters.set_time_intervals`
              - Define a collection of TimeIntervals defined by MinimumTime and MaximumTime in Epoch Seconds, one for each point in the Polyline.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PolylinePrimitiveOptionalParameters



Method detail
-------------

.. py:method:: set_time_intervals(self, time_intervals: list) -> None
    :canonical: ansys.stk.core.graphics.PolylinePrimitiveOptionalParameters.set_time_intervals

    Define a collection of TimeIntervals defined by MinimumTime and MaximumTime in Epoch Seconds, one for each point in the Polyline.

    :Parameters:

        **time_intervals** : :obj:`~list`


    :Returns:

        :obj:`~None`

