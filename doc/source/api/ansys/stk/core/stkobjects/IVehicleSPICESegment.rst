IVehicleSPICESegment
====================

.. py:class:: IVehicleSPICESegment

   object
   
   Interface for SPICE propagator segment.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~segment_name`
            * - :py:meth:`~segment_type`
            * - :py:meth:`~coord_axes`
            * - :py:meth:`~central_body`
            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSPICESegment


Property detail
---------------

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.IVehicleSPICESegment.segment_name
    :type: str

    Get the segment name.

.. py:property:: segment_type
    :canonical: ansys.stk.core.stkobjects.IVehicleSPICESegment.segment_type
    :type: str

    Get the segment type.

.. py:property:: coord_axes
    :canonical: ansys.stk.core.stkobjects.IVehicleSPICESegment.coord_axes
    :type: str

    Get the coordinate axes.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.IVehicleSPICESegment.central_body
    :type: str

    Get the central body.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehicleSPICESegment.start_time
    :type: typing.Any

    Get the start time. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehicleSPICESegment.stop_time
    :type: typing.Any

    Get the stop time. Uses DateFormat Dimension.


