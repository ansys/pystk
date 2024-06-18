IRadarClutterGeometry
=====================

.. py:class:: IRadarClutterGeometry

   object
   
   Do not use this interface, as it is deprecated. Use IAgRadarClutter interface instead. Interface which defines a radar's clutter geometry.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_model`
              - Do not use this method, as it is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Sets the current clutter geometry model by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enabled`
            * - :py:meth:`~supported_models`
            * - :py:meth:`~model`


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
    :type: "IAgRadarClutterGeometryModel"

    This property is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Gets the current clutter geometry model.


Method detail
-------------




.. py:method:: set_model(self, modelName:str) -> None

    Do not use this method, as it is deprecated. Use ScatteringPointProviderList on IAgRadarClutter instead. Sets the current clutter geometry model by name.

    :Parameters:

    **modelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


