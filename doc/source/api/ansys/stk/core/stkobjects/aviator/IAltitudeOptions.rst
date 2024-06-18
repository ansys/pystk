IAltitudeOptions
================

.. py:class:: IAltitudeOptions

   object
   
   Interface used to access the altitude options for an Aviator procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_default_cruise_altitude`
            * - :py:meth:`~altitude_reference`
            * - :py:meth:`~altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAltitudeOptions


Property detail
---------------

.. py:property:: use_default_cruise_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeOptions.use_default_cruise_altitude
    :type: bool

    Opt whether to use the default cruise altitude.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeOptions.altitude_reference
    :type: "AGL_MSL"

    Gets or sets the altitude reference.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAltitudeOptions.altitude
    :type: float

    Gets or sets the altitude for the procedure.


