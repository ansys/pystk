BoundingSphere
==============

.. py:class:: ansys.stk.core.graphics.BoundingSphere

   A sphere that encapsulates an object.

.. py:currentmodule:: BoundingSphere

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BoundingSphere.center`
              - A center of the bounding sphere. The center point is specified as one-dimensional array with three elements corresponding to (X,Y,Z) cartesian coordinates.
            * - :py:attr:`~ansys.stk.core.graphics.BoundingSphere.radius`
              - A radius of the bounding sphere.



Examples
--------

Create a Bounding Sphere

.. code-block:: python

    # Scenario scenario: Scenario object
    manager = scenario.scene_manager
    sphere = manager.initializers.bounding_sphere.initialize([[-1061.22], [-5773.98], [4456.04]], 100)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import BoundingSphere


Property detail
---------------

.. py:property:: center
    :canonical: ansys.stk.core.graphics.BoundingSphere.center
    :type: list

    A center of the bounding sphere. The center point is specified as one-dimensional array with three elements corresponding to (X,Y,Z) cartesian coordinates.

.. py:property:: radius
    :canonical: ansys.stk.core.graphics.BoundingSphere.radius
    :type: float

    A radius of the bounding sphere.


