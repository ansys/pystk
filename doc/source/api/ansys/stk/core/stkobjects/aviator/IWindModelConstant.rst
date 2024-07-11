IWindModelConstant
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.IWindModelConstant

   object
   
   Interface used to access the options for a Constant Bearing/Speed wind model.

.. py:currentmodule:: IWindModelConstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelConstant.name`
              - Gets or sets the name of the wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelConstant.blend_time`
              - Gets or sets the blend time to transition from the previous wind model if one exists.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelConstant.wind_speed`
              - Gets or sets the constant wind speed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelConstant.wind_bearing`
              - Gets or sets the wind's true bearing.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IWindModelConstant


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelConstant.name
    :type: str

    Gets or sets the name of the wind model.

.. py:property:: blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelConstant.blend_time
    :type: float

    Gets or sets the blend time to transition from the previous wind model if one exists.

.. py:property:: wind_speed
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelConstant.wind_speed
    :type: float

    Gets or sets the constant wind speed.

.. py:property:: wind_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelConstant.wind_bearing
    :type: typing.Any

    Gets or sets the wind's true bearing.


