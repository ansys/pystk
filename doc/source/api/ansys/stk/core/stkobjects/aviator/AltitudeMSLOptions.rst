AltitudeMSLOptions
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.AltitudeMSLOptions

   Class defining the altitude MSL options in a procedure.

.. py:currentmodule:: AltitudeMSLOptions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLOptions.use_default_cruise_altitude`
              - Opt whether to use the default cruise altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AltitudeMSLOptions.msl_altitude`
              - Gets or sets the MSL altitude. Can only be used when the option to use the default cruise altitude is off.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AltitudeMSLOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AltitudeMSLOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: msl_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AltitudeMSLOptions.msl_altitude
    :type: float

    Gets or sets the MSL altitude. Can only be used when the option to use the default cruise altitude is off.


