PointMassFunction
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.PointMassFunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Point Mass function.

.. py:currentmodule:: PointMassFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PointMassFunction.grav_source`
              - Gets or sets the source for the third body's gravitational parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.PointMassFunction.mu`
              - Gets or sets the gravitational parameter. Uses Gravity Param Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import PointMassFunction


Property detail
---------------

.. py:property:: grav_source
    :canonical: ansys.stk.core.stkobjects.astrogator.PointMassFunction.grav_source
    :type: GRAV_PARAM_SOURCE

    Gets or sets the source for the third body's gravitational parameter.

.. py:property:: mu
    :canonical: ansys.stk.core.stkobjects.astrogator.PointMassFunction.mu
    :type: float

    Gets or sets the gravitational parameter. Uses Gravity Param Dimension.


