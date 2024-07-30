BoundingSphereFactory
=====================

.. py:class:: ansys.stk.core.graphics.BoundingSphereFactory

   Bases: 

   Create bounding spheres.

.. py:currentmodule:: BoundingSphereFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BoundingSphereFactory.initialize`
              - Create instances of BoundingSphere.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BoundingSphereFactory.maximum_radius_bounding_sphere`
              - Gets the bounding sphere of maximum possible radius.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import BoundingSphereFactory


Property detail
---------------

.. py:property:: maximum_radius_bounding_sphere
    :canonical: ansys.stk.core.graphics.BoundingSphereFactory.maximum_radius_bounding_sphere
    :type: IBoundingSphere

    Gets the bounding sphere of maximum possible radius.


Method detail
-------------

.. py:method:: initialize(self, center: list, radius: float) -> BoundingSphere
    :canonical: ansys.stk.core.graphics.BoundingSphereFactory.initialize

    Create instances of BoundingSphere.

    :Parameters:

    **center** : :obj:`~list`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~BoundingSphere`


