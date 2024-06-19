IPolylinePrimitiveOptionalParameters
====================================

.. py:class:: IPolylinePrimitiveOptionalParameters

   object
   
   Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_time_intervals`
              - Define a collection of TimeIntervals defined by MinimumTime and MaximumTime in Epoch Seconds, one for each point in the Polyline.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPolylinePrimitiveOptionalParameters



Method detail
-------------

.. py:method:: set_time_intervals(self, timeIntervals: list) -> None
    :canonical: ansys.stk.core.graphics.IPolylinePrimitiveOptionalParameters.set_time_intervals

    Define a collection of TimeIntervals defined by MinimumTime and MaximumTime in Epoch Seconds, one for each point in the Polyline.

    :Parameters:

    **timeIntervals** : :obj:`~list`

    :Returns:

        :obj:`~None`

