IBoundingSphereFactory
======================

.. py:class:: IBoundingSphereFactory

   object
   
   Create instances of the bounding sphere type.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Create instances of BoundingSphere.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~maximum_radius_bounding_sphere`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBoundingSphereFactory


Property detail
---------------

.. py:property:: maximum_radius_bounding_sphere
    :canonical: ansys.stk.core.graphics.IBoundingSphereFactory.maximum_radius_bounding_sphere
    :type: IAgStkGraphicsBoundingSphere

    Gets the bounding sphere of maximum possible radius.


Method detail
-------------

.. py:method:: initialize(self, center: list, radius: float) -> IBoundingSphere
    :canonical: ansys.stk.core.graphics.IBoundingSphereFactory.initialize

    Create instances of BoundingSphere.

    :Parameters:

    **center** : :obj:`~list`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~IBoundingSphere`


