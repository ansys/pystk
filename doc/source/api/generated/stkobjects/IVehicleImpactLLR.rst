IVehicleImpactLLR
=================

.. py:class:: IVehicleImpactLLR

   object
   
   Interface for LLR (geocentric) coordinates for a missile's impact location.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~lat`
            * - :py:meth:`~lon`
            * - :py:meth:`~radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleImpactLLR


Property detail
---------------

.. py:property:: lat
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLLR.lat
    :type: float

    Geocentric impact latitude. Uses Latitude Dimension.

.. py:property:: lon
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLLR.lon
    :type: float

    Geocentric impact longitude. Uses Longitude Dimension.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.IVehicleImpactLLR.radius
    :type: float

    Geocentric impact radius. Uses Distance Dimension.


