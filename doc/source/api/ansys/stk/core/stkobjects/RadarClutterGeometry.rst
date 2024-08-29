RadarClutterGeometry
====================

.. py:class:: ansys.stk.core.stkobjects.RadarClutterGeometry

   Class defining a radar clutter geometry.

.. py:currentmodule:: RadarClutterGeometry

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarClutterGeometry.set_model`
              - Do not use this method, as it is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Sets the current clutter geometry model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarClutterGeometry.enabled`
              - This property is deprecated. Use Enabled on IAgRadarClutter instead. Gets or sets whether clutter geometry is enabled or disabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarClutterGeometry.supported_models`
              - This property is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Gets an array of supported model names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarClutterGeometry.model`
              - This property is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Gets the current clutter geometry model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarClutterGeometry


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.RadarClutterGeometry.enabled
    :type: bool

    This property is deprecated. Use Enabled on IAgRadarClutter instead. Gets or sets whether clutter geometry is enabled or disabled.

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.RadarClutterGeometry.supported_models
    :type: list

    This property is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.RadarClutterGeometry.model
    :type: IRadarClutterGeometryModel

    This property is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Gets the current clutter geometry model.


Method detail
-------------




.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarClutterGeometry.set_model

    Do not use this method, as it is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Sets the current clutter geometry model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


