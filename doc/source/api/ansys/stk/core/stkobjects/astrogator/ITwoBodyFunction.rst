ITwoBodyFunction
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction

   object
   
   Properties for the Two Body gravity model - a standard point mass model.

.. py:currentmodule:: ITwoBodyFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction.grav_source`
              - Gets or sets the source for the gravitational parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction.mu`
              - Gets or sets the gravitational parameter. Uses Gravity Param Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction.min_radius_percent`
              - Gets or sets the percentage of the central body's minimum radius at which a modified force model (only the two-body force) will be used - provided there is no altitude stopping condition. Uses Percent Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ITwoBodyFunction


Property detail
---------------

.. py:property:: grav_source
    :canonical: ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction.grav_source
    :type: GRAV_PARAM_SOURCE

    Gets or sets the source for the gravitational parameter.

.. py:property:: mu
    :canonical: ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction.mu
    :type: float

    Gets or sets the gravitational parameter. Uses Gravity Param Dimension.

.. py:property:: min_radius_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.ITwoBodyFunction.min_radius_percent
    :type: float

    Gets or sets the percentage of the central body's minimum radius at which a modified force model (only the two-body force) will be used - provided there is no altitude stopping condition. Uses Percent Dimension.


