IRadarClutterGeometry
=====================

.. py:class:: ansys.stk.core.stkobjects.IRadarClutterGeometry

   object
   
   Do not use this interface, as it is deprecated. Use IAgRadarClutter interface instead. Interface which defines a radar's clutter geometry.

.. py:currentmodule:: IRadarClutterGeometry

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutterGeometry.set_model`
              - Do not use this method, as it is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Sets the current clutter geometry model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutterGeometry.enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutterGeometry.supported_models`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarClutterGeometry.model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarClutterGeometry


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometry.enabled
    :type: bool

    This property is deprecated. Use Enabled on IAgRadarClutter instead. Gets or sets whether clutter geometry is enabled or disabled.

.. py:property:: supported_models
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometry.supported_models
    :type: list

    This property is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Gets an array of supported model names.

.. py:property:: model
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometry.model
    :type: IRadarClutterGeometryModel

    This property is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Gets the current clutter geometry model.


Method detail
-------------




.. py:method:: set_model(self, modelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarClutterGeometry.set_model

    Do not use this method, as it is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Sets the current clutter geometry model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


