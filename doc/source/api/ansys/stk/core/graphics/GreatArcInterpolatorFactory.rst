GreatArcInterpolatorFactory
===========================

.. py:class:: ansys.stk.core.graphics.GreatArcInterpolatorFactory

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


Examples
--------

Compute interpolated positions along a great arc

.. code-block:: python

    # Scenario scenario: Scenario object
    # Create a array of LLA values and interoplate them over the specified
    # central body
    positionArray = [[35.017], [-118.540], [0], [44.570], [-96.474], [0], [31.101], [-82.619], [0]]
    manager = scenario.scene_manager
    # Interpolate points over great arc
    interpolator = manager.initializers.great_arc_interpolator.initialize_with_central_body("Earth")
    interpolator.granularity = 0.1
    result = interpolator.interpolate(positionArray)


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

.. py:method:: initialize_with_central_body(self, central_body: str) -> GreatArcInterpolator
    :canonical: ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize_with_central_body

    Initialize a great arc interpolator with the specified centralBody and a granularity of 1 degree.

    :Parameters:

    **central_body** : :obj:`~str`

    :Returns:

        :obj:`~GreatArcInterpolator`

.. py:method:: initialize_with_central_body_and_granularity(self, central_body: str, granularity: float) -> GreatArcInterpolator
    :canonical: ansys.stk.core.graphics.GreatArcInterpolatorFactory.initialize_with_central_body_and_granularity

    Initialize a great arc interpolator with the specified centralBody and granularity.

    :Parameters:

    **central_body** : :obj:`~str`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~GreatArcInterpolator`

