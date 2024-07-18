ProcedureEnroute
================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureEnroute

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining an enroute procedure.

.. py:currentmodule:: ProcedureEnroute

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureEnroute.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureEnroute.altitude_msl_options`
              - Get the altitude MSL options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureEnroute.navigation_options`
              - Get the navigation options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureEnroute.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureEnroute.enroute_cruise_airspeed_options`
              - Get the enroute cruise airspeed options.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureEnroute


Property detail
---------------

.. py:property:: altitude_msl_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureEnroute.altitude_msl_options
    :type: IAltitudeMSLAndLevelOffOptions

    Get the altitude MSL options.

.. py:property:: navigation_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureEnroute.navigation_options
    :type: INavigationOptions

    Get the navigation options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureEnroute.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureEnroute.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the enroute cruise airspeed options.


Method detail
-------------





.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureEnroute.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

