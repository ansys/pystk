IProcedure
==========

.. py:class:: IProcedure

   object
   
   Interface used to access the options for a procedure. Use this interface to get the Site and Get the time options for the current procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~site`
            * - :py:meth:`~time_options`
            * - :py:meth:`~wind_model`
            * - :py:meth:`~atmosphere_model`
            * - :py:meth:`~calculation_options`
            * - :py:meth:`~refuel_dump_is_supported`
            * - :py:meth:`~refuel_dump_properties`
            * - :py:meth:`~fast_time_options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedure


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.name
    :type: str

    Gets or sets the name of the procedure.

.. py:property:: site
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.site
    :type: IAgAvtrSite

    Get the site of the current procedure.

.. py:property:: time_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.time_options
    :type: IAgAvtrProcedureTimeOptions

    Get the time options for the current procedure.

.. py:property:: wind_model
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.wind_model
    :type: IAgAvtrWindModel

    Get the wind model for the current procedure.

.. py:property:: atmosphere_model
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.atmosphere_model
    :type: IAgAvtrAtmosphereModel

    Get the mission atmosphere model.

.. py:property:: calculation_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.calculation_options
    :type: IAgAvtrCalculationOptions

    Get the calculation options for the current procedure.

.. py:property:: refuel_dump_is_supported
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_is_supported
    :type: bool

    Refuel/dump is supported for the current procedure.

.. py:property:: refuel_dump_properties
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_properties
    :type: IAgAvtrRefuelDumpProperties

    Get the refuel/dump properties for the current procedure.

.. py:property:: fast_time_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.fast_time_options
    :type: IAgAvtrProcedureFastTimeOptions

    Get the fast time options (without validation or constraints) for the current procedure.


