IProjectionFactory
==================

.. py:class:: IProjectionFactory

   object
   
   A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new instance.
            * - :py:meth:`~initialize_with_data`
              - Initialize a new instance.
            * - :py:meth:`~initialize_from_projection`
              - Initialize a new instance from another projection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IProjectionFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IProjection"

    Initialize a new instance.

    :Returns:

        :obj:`~"IProjection"`

.. py:method:: initialize_with_data(self, position:list, orientation:"IOrientation", fieldOfViewHorizontal:float, fieldOfViewVertical:float, nearPlane:float, farPlane:float) -> "IProjection"

    Initialize a new instance.

    :Parameters:

    **position** : :obj:`~list`
    **orientation** : :obj:`~"IOrientation"`
    **fieldOfViewHorizontal** : :obj:`~float`
    **fieldOfViewVertical** : :obj:`~float`
    **nearPlane** : :obj:`~float`
    **farPlane** : :obj:`~float`

    :Returns:

        :obj:`~"IProjection"`

.. py:method:: initialize_from_projection(self, projection:"IProjection") -> "IProjection"

    Initialize a new instance from another projection.

    :Parameters:

    **projection** : :obj:`~"IProjection"`

    :Returns:

        :obj:`~"IProjection"`

