IScenSpaceEnvironment
=====================

.. py:class:: ansys.stk.core.stkobjects.IScenSpaceEnvironment

   object
   
   no helpstring provided.

.. py:currentmodule:: IScenSpaceEnvironment

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScenSpaceEnvironment.compute_saa_flux_intensity`
              - Compute SAA flux intensity at the specified Earth location. Uses Angle, Longitude, Distance, and FluxIntensity Dimensions.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScenSpaceEnvironment.radiation_environment`
              - Gets the radiation environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScenSpaceEnvironment.graphics_3d`
              - Gets the 3D Graphics settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenSpaceEnvironment


Property detail
---------------

.. py:property:: radiation_environment
    :canonical: ansys.stk.core.stkobjects.IScenSpaceEnvironment.radiation_environment
    :type: ISpaceEnvironmentRadiationEnvironment

    Gets the radiation environment settings.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IScenSpaceEnvironment.graphics_3d
    :type: ISpaceEnvironmentScenarioExtGraphics3D

    Gets the 3D Graphics settings.


Method detail
-------------



.. py:method:: compute_saa_flux_intensity(self, channel: SPACE_ENVIRONMENT_SAA_CHANNEL, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.IScenSpaceEnvironment.compute_saa_flux_intensity

    Compute SAA flux intensity at the specified Earth location. Uses Angle, Longitude, Distance, and FluxIntensity Dimensions.

    :Parameters:

    **channel** : :obj:`~SPACE_ENVIRONMENT_SAA_CHANNEL`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~float`

