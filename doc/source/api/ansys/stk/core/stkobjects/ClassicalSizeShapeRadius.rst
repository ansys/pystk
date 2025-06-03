ClassicalSizeShapeRadius
========================

.. py:class:: ansys.stk.core.stkobjects.ClassicalSizeShapeRadius

   Bases: :py:class:`~ansys.stk.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using Radius.

.. py:currentmodule:: ClassicalSizeShapeRadius

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalSizeShapeRadius.set_size_shape_radius`
              - Set both the Apogee Radius and the Perigee Radius. Displays an error message if the value for PerigeeRadius exceeds that for ApogeeRadius. ApogeeRadius/PerigeeRadius use Distance Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalSizeShapeRadius.apogee_radius`
              - Measured from the center of the Earth to the point of maximum radius in the orbit. You can set it together with PerigeeRadius using the SetSizeShapeRadius(ApogeeRadius, PerigeeRadius) method. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalSizeShapeRadius.perigee_radius`
              - Measured from the center of the Earth to the point of minimum radius in the orbit. You can set it together with ApogeeRadius using the SetSizeShapeRadius(ApogeeRadius, PerigeeRadius) method. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ClassicalSizeShapeRadius


Property detail
---------------

.. py:property:: apogee_radius
    :canonical: ansys.stk.core.stkobjects.ClassicalSizeShapeRadius.apogee_radius
    :type: float

    Measured from the center of the Earth to the point of maximum radius in the orbit. You can set it together with PerigeeRadius using the SetSizeShapeRadius(ApogeeRadius, PerigeeRadius) method. Uses Distance Dimension.

.. py:property:: perigee_radius
    :canonical: ansys.stk.core.stkobjects.ClassicalSizeShapeRadius.perigee_radius
    :type: float

    Measured from the center of the Earth to the point of minimum radius in the orbit. You can set it together with ApogeeRadius using the SetSizeShapeRadius(ApogeeRadius, PerigeeRadius) method. Uses Distance Dimension.


Method detail
-------------





.. py:method:: set_size_shape_radius(self, apogee_radius: float, perigee_radius: float) -> None
    :canonical: ansys.stk.core.stkobjects.ClassicalSizeShapeRadius.set_size_shape_radius

    Set both the Apogee Radius and the Perigee Radius. Displays an error message if the value for PerigeeRadius exceeds that for ApogeeRadius. ApogeeRadius/PerigeeRadius use Distance Dimension.

    :Parameters:

        **apogee_radius** : :obj:`~float`

        **perigee_radius** : :obj:`~float`


    :Returns:

        :obj:`~None`

