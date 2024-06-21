IClassicalSizeShapeAltitude
===========================

.. py:class:: ansys.stk.core.stkobjects.IClassicalSizeShapeAltitude

   IClassicalSizeShape
   
   Interface for specifying orbit size and shape using altitude.

.. py:currentmodule:: IClassicalSizeShapeAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalSizeShapeAltitude.apogee_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalSizeShapeAltitude.perigee_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IClassicalSizeShapeAltitude


Property detail
---------------

.. py:property:: apogee_altitude
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapeAltitude.apogee_altitude
    :type: float

    Measured from the 'surface' of the Earth to the point of maximum radius in the orbit. For this value, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance Dimension.

.. py:property:: perigee_altitude
    :canonical: ansys.stk.core.stkobjects.IClassicalSizeShapeAltitude.perigee_altitude
    :type: float

    Measured from the 'surface' of the Earth to the point of minimum radius in the orbit. For this value, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance Dimension.


