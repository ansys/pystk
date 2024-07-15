RadarCrossSectionFrequencyBand
==============================

.. py:class:: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand

   Bases: 

   Class defining a inheritable radar cross section frequency band.

.. py:currentmodule:: RadarCrossSectionFrequencyBand

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.set_compute_strategy`
              - Set the current compute strategy by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.minimum_frequency`
              - Gets or sets the frequency band minimum frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.maximum_frequency`
              - Gets or sets the frequency band maximum frequency.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.swerling_case`
              - Gets or sets the band Swerling case.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.supported_compute_strategies`
              - Gets an array of supported compute strategy names.
            * - :py:attr:`~ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.compute_strategy`
              - Gets the current compute strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RadarCrossSectionFrequencyBand


Property detail
---------------

.. py:property:: minimum_frequency
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.minimum_frequency
    :type: float

    Gets or sets the frequency band minimum frequency.

.. py:property:: maximum_frequency
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.maximum_frequency
    :type: float

    Gets or sets the frequency band maximum frequency.

.. py:property:: swerling_case
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.swerling_case
    :type: RADAR_SWERLING_CASE

    Gets or sets the band Swerling case.

.. py:property:: supported_compute_strategies
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.supported_compute_strategies
    :type: list

    Gets an array of supported compute strategy names.

.. py:property:: compute_strategy
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.compute_strategy
    :type: IRadarCrossSectionComputeStrategy

    Gets the current compute strategy.


Method detail
-------------







.. py:method:: set_compute_strategy(self, computeStrategyName: str) -> None
    :canonical: ansys.stk.core.stkobjects.RadarCrossSectionFrequencyBand.set_compute_strategy

    Set the current compute strategy by name.

    :Parameters:

    **computeStrategyName** : :obj:`~str`

    :Returns:

        :obj:`~None`


