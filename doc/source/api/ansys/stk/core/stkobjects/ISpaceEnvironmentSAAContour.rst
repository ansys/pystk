ISpaceEnvironmentSAAContour
===========================

.. py:class:: ansys.stk.core.stkobjects.ISpaceEnvironmentSAAContour

   object
   
   SAA Contour settings.

.. py:currentmodule:: ISpaceEnvironmentSAAContour

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentSAAContour.compute_saa_flux_intensity`
              - Compute SAA flux intensity at the specified time on the vehicle's channel. Uses DateFormat and FluxIntensity Dimensions.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentSAAContour.channel`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentSAAContour.flux_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISpaceEnvironmentSAAContour


Property detail
---------------

.. py:property:: channel
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentSAAContour.channel
    :type: SPACE_ENVIRONMENT_SAA_CHANNEL

    Energy level for SAA protons.

.. py:property:: flux_level
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentSAAContour.flux_level
    :type: SPACE_ENVIRONMENT_SAA_FLUX_LEVEL

    Flux level for SAA contour.


Method detail
-------------





.. py:method:: compute_saa_flux_intensity(self, time: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentSAAContour.compute_saa_flux_intensity

    Compute SAA flux intensity at the specified time on the vehicle's channel. Uses DateFormat and FluxIntensity Dimensions.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

