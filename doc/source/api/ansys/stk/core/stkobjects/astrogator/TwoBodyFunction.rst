TwoBodyFunction
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.TwoBodyFunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Two Body gravity propagator function.

.. py:currentmodule:: TwoBodyFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.gravitational_parameter_source`
              - Gets or sets the source for the gravitational parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.mu`
              - Gets or sets the gravitational parameter. Uses Gravity Param Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.min_radius_percent`
              - Gets or sets the percentage of the central body's minimum radius at which a modified force model (only the two-body force) will be used - provided there is no altitude stopping condition. Uses Percent Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import TwoBodyFunction


Property detail
---------------

.. py:property:: gravitational_parameter_source
    :canonical: ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.gravitational_parameter_source
    :type: GravParamSource

    Gets or sets the source for the gravitational parameter.

.. py:property:: mu
    :canonical: ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.mu
    :type: float

    Gets or sets the gravitational parameter. Uses Gravity Param Dimension.

.. py:property:: min_radius_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.min_radius_percent
    :type: float

    Gets or sets the percentage of the central body's minimum radius at which a modified force model (only the two-body force) will be used - provided there is no altitude stopping condition. Uses Percent Dimension.


