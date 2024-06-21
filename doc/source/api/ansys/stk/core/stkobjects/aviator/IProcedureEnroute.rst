IProcedureEnroute
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureEnroute

   object
   
   Interface used to access the options for an enroute procedure.

.. py:currentmodule:: IProcedureEnroute

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureEnroute.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureEnroute.altitude_msl_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureEnroute.navigation_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureEnroute.enroute_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureEnroute.enroute_cruise_airspeed_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureEnroute


Property detail
---------------

.. py:property:: altitude_msl_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureEnroute.altitude_msl_options
    :type: IAltitudeMSLAndLevelOffOptions

    Get the altitude MSL options.

.. py:property:: navigation_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureEnroute.navigation_options
    :type: INavigationOptions

    Get the navigation options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureEnroute.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureEnroute.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedOptions

    Get the enroute cruise airspeed options.


Method detail
-------------





.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureEnroute.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

