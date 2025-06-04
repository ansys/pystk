ScenarioSpaceEnvironment
========================

.. py:class:: ansys.stk.core.stkobjects.ScenarioSpaceEnvironment

   SpaceEnvironment settings.

.. py:currentmodule:: ScenarioSpaceEnvironment

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioSpaceEnvironment.compute_saa_flux_intensity`
              - Compute SAA flux intensity at the specified Earth location. Uses Angle, Longitude, Distance, and FluxIntensity Dimensions.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioSpaceEnvironment.radiation_environment`
              - Get the radiation environment settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioSpaceEnvironment.graphics_3d`
              - Get the 3D Graphics settings.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioSpaceEnvironment


Property detail
---------------

.. py:property:: radiation_environment
    :canonical: ansys.stk.core.stkobjects.ScenarioSpaceEnvironment.radiation_environment
    :type: SpaceEnvironmentRadiationEnvironment

    Get the radiation environment settings.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ScenarioSpaceEnvironment.graphics_3d
    :type: SpaceEnvironmentScenarioGraphics3D

    Get the 3D Graphics settings.


Method detail
-------------



.. py:method:: compute_saa_flux_intensity(self, channel: SpaceEnvironmentSAAChannel, lat: float, lon: float, alt: float) -> float
    :canonical: ansys.stk.core.stkobjects.ScenarioSpaceEnvironment.compute_saa_flux_intensity

    Compute SAA flux intensity at the specified Earth location. Uses Angle, Longitude, Distance, and FluxIntensity Dimensions.

    :Parameters:

        **channel** : :obj:`~SpaceEnvironmentSAAChannel`

        **lat** : :obj:`~float`

        **lon** : :obj:`~float`

        **alt** : :obj:`~float`


    :Returns:

        :obj:`~float`

