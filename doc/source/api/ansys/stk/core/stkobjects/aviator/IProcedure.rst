IProcedure
==========

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedure

   object
   
   Interface used to access the options for a procedure. Use this interface to get the Site and Get the time options for the current procedure.

.. py:currentmodule:: IProcedure

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.site`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.time_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.wind_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.atmosphere_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.calculation_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_is_supported`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_properties`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.fast_time_options`


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
    :type: ISite

    Get the site of the current procedure.

.. py:property:: time_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.time_options
    :type: IProcedureTimeOptions

    Get the time options for the current procedure.

.. py:property:: wind_model
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.wind_model
    :type: IWindModel

    Get the wind model for the current procedure.

.. py:property:: atmosphere_model
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.atmosphere_model
    :type: IAtmosphereModel

    Get the mission atmosphere model.

.. py:property:: calculation_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.calculation_options
    :type: ICalculationOptions

    Get the calculation options for the current procedure.

.. py:property:: refuel_dump_is_supported
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_is_supported
    :type: bool

    Refuel/dump is supported for the current procedure.

.. py:property:: refuel_dump_properties
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_properties
    :type: IRefuelDumpProperties

    Get the refuel/dump properties for the current procedure.

.. py:property:: fast_time_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.fast_time_options
    :type: IProcedureFastTimeOptions

    Get the fast time options (without validation or constraints) for the current procedure.


