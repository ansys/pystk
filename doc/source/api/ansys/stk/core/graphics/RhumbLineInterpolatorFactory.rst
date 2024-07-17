RhumbLineInterpolatorFactory
============================

.. py:class:: ansys.stk.core.graphics.RhumbLineInterpolatorFactory

   Bases: 

   The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

.. py:currentmodule:: RhumbLineInterpolatorFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RhumbLineInterpolatorFactory.initialize`
              - Initialize a default rhumb line interpolator. This is equivalent to constructing a rhumb line interpolator with a central body equal to an instance of earth central body and a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.RhumbLineInterpolatorFactory.initialize_with_central_body`
              - Initialize a rhumb line interpolator with the specified centralBody and a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.RhumbLineInterpolatorFactory.initialize_with_central_body_and_granularity`
              - Initialize a rhumb line interpolator with the specified centralBody and granularity.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RhumbLineInterpolatorFactory



Method detail
-------------

.. py:method:: initialize(self) -> RhumbLineInterpolator
    :canonical: ansys.stk.core.graphics.RhumbLineInterpolatorFactory.initialize

    Initialize a default rhumb line interpolator. This is equivalent to constructing a rhumb line interpolator with a central body equal to an instance of earth central body and a granularity of 1 degree.

    :Returns:

        :obj:`~RhumbLineInterpolator`

.. py:method:: initialize_with_central_body(self, centralBody: str) -> RhumbLineInterpolator
    :canonical: ansys.stk.core.graphics.RhumbLineInterpolatorFactory.initialize_with_central_body

    Initialize a rhumb line interpolator with the specified centralBody and a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~RhumbLineInterpolator`

.. py:method:: initialize_with_central_body_and_granularity(self, centralBody: str, granularity: float) -> RhumbLineInterpolator
    :canonical: ansys.stk.core.graphics.RhumbLineInterpolatorFactory.initialize_with_central_body_and_granularity

    Initialize a rhumb line interpolator with the specified centralBody and granularity.

    :Parameters:

    **centralBody** : :obj:`~str`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~RhumbLineInterpolator`

