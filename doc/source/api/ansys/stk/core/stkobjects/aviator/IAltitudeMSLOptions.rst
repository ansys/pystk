IAltitudeMSLOptions
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAltitudeMSLOptions

   object
   
   Interface used to access the altitude MSL options for an Aviator procedure.

.. py:currentmodule:: IAltitudeMSLOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAltitudeMSLOptions.use_default_cruise_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAltitudeMSLOptions.msl_altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAltitudeMSLOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeMSLOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: msl_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeMSLOptions.msl_altitude
    :type: float

    Gets or sets the MSL altitude. Can only be used when the option to use the default cruise altitude is off.


