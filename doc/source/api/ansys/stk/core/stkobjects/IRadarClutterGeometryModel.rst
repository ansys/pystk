IRadarClutterGeometryModel
==========================

.. py:class:: IRadarClutterGeometryModel

   object
   
   Do not use this interface, as it is deprecated. Use IAgScatteringPointProvider interface instead. Provides access to the properties and methods defining a radar clutter geometry model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarClutterGeometryModel


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometryModel.name
    :type: str

    This property is deprecated. Use Name on IAgScatteringPointProvider instead. Gets the radar clutter geometry model name.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometryModel.type
    :type: RADAR_CLUTTER_GEOMETRY_MODEL_TYPE

    This property is deprecated. Use PointProviderType on IAgScatteringPointProvider instead. Gets the radar clutter geometry model type enumeration.


