IEnrouteAndDelayOptions
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions

   object
   
   Interface used to access the Enroute options for an Aviator procedure.

.. py:currentmodule:: IEnrouteAndDelayOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions.delay_enroute_climb_descents`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions.use_max_speed_turns`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions.max_turn_radius_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IEnrouteAndDelayOptions


Property detail
---------------

.. py:property:: delay_enroute_climb_descents
    :canonical: ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions.delay_enroute_climb_descents
    :type: bool

    Opt whether to delay the enroute climb or descent.

.. py:property:: use_max_speed_turns
    :canonical: ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions.use_max_speed_turns
    :type: bool

    Opt whether to use the max speed turns.

.. py:property:: max_turn_radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IEnrouteAndDelayOptions.max_turn_radius_factor
    :type: float

    Gets or sets the maximum turn radius factor.


