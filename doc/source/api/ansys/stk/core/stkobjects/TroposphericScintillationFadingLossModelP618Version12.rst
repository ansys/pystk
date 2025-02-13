TroposphericScintillationFadingLossModelP618Version12
=====================================================

.. py:class:: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12

   Bases: :py:class:`~ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a tropospheric scintillation fading loss P.618-12 model.

.. py:currentmodule:: TroposphericScintillationFadingLossModelP618Version12

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.average_time_choice`
              - Get or set the TropoScintillation average fade time choice.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.compute_deep_fade`
              - Do not use this property, as it is deprecated. The ComputeDeepFade property should not be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.fade_outage`
              - Do not use this property, as it is deprecated. Use the FadeExceeded property.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.percent_time_refractivity_gradient`
              - Get or set the percentage of time that the refractivity gradient is less than -100 N units / km.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.surface_temperature`
              - Get or set the surface temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.fade_exceeded`
              - Get or set the fade exceeded percent.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TroposphericScintillationFadingLossModelP618Version12


Property detail
---------------

.. py:property:: average_time_choice
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.average_time_choice
    :type: TroposphericScintillationAverageTimeChoiceType

    Get or set the TropoScintillation average fade time choice.

.. py:property:: compute_deep_fade
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.compute_deep_fade
    :type: bool

    Do not use this property, as it is deprecated. The ComputeDeepFade property should not be used.

.. py:property:: fade_outage
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.fade_outage
    :type: float

    Do not use this property, as it is deprecated. Use the FadeExceeded property.

.. py:property:: percent_time_refractivity_gradient
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.percent_time_refractivity_gradient
    :type: float

    Get or set the percentage of time that the refractivity gradient is less than -100 N units / km.

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.surface_temperature
    :type: float

    Get or set the surface temperature.

.. py:property:: fade_exceeded
    :canonical: ansys.stk.core.stkobjects.TroposphericScintillationFadingLossModelP618Version12.fade_exceeded
    :type: float

    Get or set the fade exceeded percent.


