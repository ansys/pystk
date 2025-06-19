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
              - Get or set the source for the gravitational parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.mu`
              - Get or set the gravitational parameter. Uses Gravity Param Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.min_radius_percent`
              - Get or set the percentage of the central body's minimum radius at which a modified force model (only the two-body force) will be used - provided there is no altitude stopping condition. Uses Percent Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import TwoBodyFunction


Property detail
---------------

.. py:property:: gravitational_parameter_source
    :canonical: ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.gravitational_parameter_source
    :type: GravParamSource

    Get or set the source for the gravitational parameter.

.. py:property:: mu
    :canonical: ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.mu
    :type: float

    Get or set the gravitational parameter. Uses Gravity Param Dimension.

.. py:property:: min_radius_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.TwoBodyFunction.min_radius_percent
    :type: float

    Get or set the percentage of the central body's minimum radius at which a modified force model (only the two-body force) will be used - provided there is no altitude stopping condition. Uses Percent Dimension.


