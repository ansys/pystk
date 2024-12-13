TroposphericScintillationFadingLossModelP618_12
===============================================

.. py:class:: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a tropospheric scintillation fading loss P.618-12 model.

.. py:currentmodule:: TroposphericScintillationFadingLossModelP618_12

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.average_time_choice`
              - Gets or sets the TropoScintillation average fade time choice.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.compute_deep_fade`
              - This property is deprecated. The ComputeDeepFade property should not be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.fade_outage`
              - This property is deprecated. Use the FadeExceeded property.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.percent_time_refractivity_gradient`
              - Gets or sets the percentage of time that the refractivity gradient is less than -100 N units / km.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.surface_temperature`
              - Gets or sets the surface temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.fade_exceeded`
              - Gets or sets the fade exceeded percent.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TroposphericScintillationFadingLossModelP618_12


Property detail
---------------

.. py:property:: average_time_choice
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.average_time_choice
    :type: TroposphericScintillationAverageTimeChoiceType

    Gets or sets the TropoScintillation average fade time choice.

.. py:property:: compute_deep_fade
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.compute_deep_fade
    :type: bool

    This property is deprecated. The ComputeDeepFade property should not be used.

.. py:property:: fade_outage
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.fade_outage
    :type: float

    This property is deprecated. Use the FadeExceeded property.

.. py:property:: percent_time_refractivity_gradient
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.percent_time_refractivity_gradient
    :type: float

    Gets or sets the percentage of time that the refractivity gradient is less than -100 N units / km.

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.surface_temperature
    :type: float

    Gets or sets the surface temperature.

.. py:property:: fade_exceeded
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618_12.fade_exceeded
    :type: float

    Gets or sets the fade exceeded percent.


