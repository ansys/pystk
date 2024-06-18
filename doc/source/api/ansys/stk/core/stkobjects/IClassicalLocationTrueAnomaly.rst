IClassicalLocationTrueAnomaly
=============================

.. py:class:: IClassicalLocationTrueAnomaly

   IClassicalLocation
   
   Interface for True Anomaly, used in specifying the spacecraft's location within its orbit at epoch.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~value`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IClassicalLocationTrueAnomaly


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IClassicalLocationTrueAnomaly.value
    :type: float

    Value of True Anomaly: angle from the eccentricity vector (points toward perigee) to the satellite position vector, measured in the direction of satellite motion and in the orbit plane.Uses Angle Dimension.


