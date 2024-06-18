ITroposphericScintillationFadingLossModelP618_12
================================================

.. py:class:: ITroposphericScintillationFadingLossModelP618_12

   object
   
   Provide access to the properties and methods of a Tropospheric Scintillation loss model ITU-R P.618_12.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~average_time_choice`
            * - :py:meth:`~compute_deep_fade`
            * - :py:meth:`~fade_outage`
            * - :py:meth:`~percent_time_refractivity_gradient`
            * - :py:meth:`~surface_temperature`
            * - :py:meth:`~fade_exceeded`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITroposphericScintillationFadingLossModelP618_12


Property detail
---------------

.. py:property:: average_time_choice
    :canonical: ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModelP618_12.average_time_choice
    :type: "TROPOSPHERIC_SCINTILLATION_AVERAGE_TIME_CHOICES"

    Gets or sets the TropoScintillation average fade time choice.

.. py:property:: compute_deep_fade
    :canonical: ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModelP618_12.compute_deep_fade
    :type: bool

    This property is deprecated. The ComputeDeepFade property should not be used.

.. py:property:: fade_outage
    :canonical: ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModelP618_12.fade_outage
    :type: float

    This property is deprecated. Use the FadeExceeded property.

.. py:property:: percent_time_refractivity_gradient
    :canonical: ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModelP618_12.percent_time_refractivity_gradient
    :type: float

    Gets or sets the percentage of time that the refractivity gradient is less than -100 N units / km.

.. py:property:: surface_temperature
    :canonical: ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModelP618_12.surface_temperature
    :type: float

    Gets or sets the surface temperature.

.. py:property:: fade_exceeded
    :canonical: ansys.stk.core.stkobjects.ITroposphericScintillationFadingLossModelP618_12.fade_exceeded
    :type: float

    Gets or sets the fade exceeded percent.


