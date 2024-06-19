IRadarCrossSectionFrequencyBand
===============================

.. py:class:: IRadarCrossSectionFrequencyBand

   object
   
   Provide access to the properties and methods defining radar cross section frequency band.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_compute_strategy`
              - Set the current compute strategy by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~minimum_frequency`
            * - :py:meth:`~maximum_frequency`
            * - :py:meth:`~swerling_case`
            * - :py:meth:`~supported_compute_strategies`
            * - :py:meth:`~compute_strategy`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionFrequencyBand


Property detail
---------------

.. py:property:: minimum_frequency
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBand.minimum_frequency
    :type: float

    Gets or sets the frequency band minimum frequency.

.. py:property:: maximum_frequency
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBand.maximum_frequency
    :type: float

    Gets or sets the frequency band maximum frequency.

.. py:property:: swerling_case
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBand.swerling_case
    :type: RADAR_SWERLING_CASE

    Gets or sets the band Swerling case.

.. py:property:: supported_compute_strategies
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBand.supported_compute_strategies
    :type: list

    Gets an array of supported compute strategy names.

.. py:property:: compute_strategy
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBand.compute_strategy
    :type: IAgRadarCrossSectionComputeStrategy

    Gets the current compute strategy.


Method detail
-------------







.. py:method:: set_compute_strategy(self, computeStrategyName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionFrequencyBand.set_compute_strategy

    Set the current compute strategy by name.

    :Parameters:

    **computeStrategyName** : :obj:`~str`

    :Returns:

        :obj:`~None`


