GreatArcInterpolatorFactory
===========================

.. py:class:: ansys.stk.core.graphics.GreatArcInterpolatorFactory

   Bases: 

   The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

.. py:currentmodule:: GreatArcInterpolatorFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize`
              - Initialize a default great arc interpolator. This is equivalent to constructing a great arc interpolator with a central body equal to an instance of earth central body and a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize_with_central_body`
              - Initialize a great arc interpolator with the specified centralBody and a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize_with_central_body_and_granularity`
              - Initialize a great arc interpolator with the specified centralBody and granularity.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import GreatArcInterpolatorFactory



Method detail
-------------

.. py:method:: initialize(self) -> GreatArcInterpolator
    :canonical: ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize

    Initialize a default great arc interpolator. This is equivalent to constructing a great arc interpolator with a central body equal to an instance of earth central body and a granularity of 1 degree.

    :Returns:

        :obj:`~GreatArcInterpolator`

.. py:method:: initialize_with_central_body(self, centralBody: str) -> GreatArcInterpolator
    :canonical: ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize_with_central_body

    Initialize a great arc interpolator with the specified centralBody and a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~GreatArcInterpolator`

.. py:method:: initialize_with_central_body_and_granularity(self, centralBody: str, granularity: float) -> GreatArcInterpolator
    :canonical: ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize_with_central_body_and_granularity

    Initialize a great arc interpolator with the specified centralBody and granularity.

    :Parameters:

    **centralBody** : :obj:`~str`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~GreatArcInterpolator`

