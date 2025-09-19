ProjectionFactory
=================

.. py:class:: ansys.stk.core.graphics.ProjectionFactory

   A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

.. py:currentmodule:: ProjectionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ProjectionFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectionFactory.initialize_from_projection`
              - Initialize a new instance from another projection.
            * - :py:attr:`~ansys.stk.core.graphics.ProjectionFactory.initialize_with_data`
              - Initialize a new instance.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ProjectionFactory



Method detail
-------------

.. py:method:: initialize(self) -> IProjection
    :canonical: ansys.stk.core.graphics.ProjectionFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IProjection`

.. py:method:: initialize_from_projection(self, projection: IProjection) -> IProjection
    :canonical: ansys.stk.core.graphics.ProjectionFactory.initialize_from_projection

    Initialize a new instance from another projection.

    :Parameters:

        **projection** : :obj:`~IProjection`


    :Returns:

        :obj:`~IProjection`

.. py:method:: initialize_with_data(self, position: list, orientation: IOrientation, field_of_view_horizontal: float, field_of_view_vertical: float, near_plane: float, far_plane: float) -> IProjection
    :canonical: ansys.stk.core.graphics.ProjectionFactory.initialize_with_data

    Initialize a new instance.

    :Parameters:

        **position** : :obj:`~list`

        **orientation** : :obj:`~IOrientation`

        **field_of_view_horizontal** : :obj:`~float`

        **field_of_view_vertical** : :obj:`~float`

        **near_plane** : :obj:`~float`

        **far_plane** : :obj:`~float`


    :Returns:

        :obj:`~IProjection`

