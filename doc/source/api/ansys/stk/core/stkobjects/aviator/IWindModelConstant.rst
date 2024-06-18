IWindModelConstant
==================

.. py:class:: IWindModelConstant

   object
   
   Interface used to access the options for a Constant Bearing/Speed wind model.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~blend_time`
            * - :py:meth:`~wind_speed`
            * - :py:meth:`~wind_bearing`


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


