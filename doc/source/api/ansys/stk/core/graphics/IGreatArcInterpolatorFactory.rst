IGreatArcInterpolatorFactory
============================

.. py:class:: IGreatArcInterpolatorFactory

   object
   
   The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default great arc interpolator. This is equivalent to constructing a great arc interpolator with a central body equal to an instance of earth central body and a granularity of 1 degree.
            * - :py:meth:`~initialize_with_central_body`
              - Initialize a great arc interpolator with the specified centralBody and a granularity of 1 degree.
            * - :py:meth:`~initialize_with_central_body_and_granularity`
              - Initialize a great arc interpolator with the specified centralBody and granularity.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGreatArcInterpolatorFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IGreatArcInterpolator"

    Initialize a default great arc interpolator. This is equivalent to constructing a great arc interpolator with a central body equal to an instance of earth central body and a granularity of 1 degree.

    :Returns:

        :obj:`~"IGreatArcInterpolator"`

.. py:method:: initialize_with_central_body(self, centralBody:str) -> "IGreatArcInterpolator"

    Initialize a great arc interpolator with the specified centralBody and a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`

    :Returns:

        :obj:`~"IGreatArcInterpolator"`

.. py:method:: initialize_with_central_body_and_granularity(self, centralBody:str, granularity:float) -> "IGreatArcInterpolator"

    Initialize a great arc interpolator with the specified centralBody and granularity.

    :Parameters:

    **centralBody** : :obj:`~str`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~"IGreatArcInterpolator"`

