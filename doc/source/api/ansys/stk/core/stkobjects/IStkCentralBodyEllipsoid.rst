IStkCentralBodyEllipsoid
========================

.. py:class:: IStkCentralBodyEllipsoid

   object
   
   Provide information about the central body's equatorial and polar radii.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_surface_distance`
              - Compute the distance between two points on the surface of the central body. Distance is measured along a great arc path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~a`
            * - :py:meth:`~b`
            * - :py:meth:`~c`
            * - :py:meth:`~mean_radius`
            * - :py:meth:`~volumetric_radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkCentralBodyEllipsoid


Property detail
---------------

.. py:property:: a
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyEllipsoid.a
    :type: float

    An equatorial radius along the x-axis.

.. py:property:: b
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyEllipsoid.b
    :type: float

    An equatorial radius along the y-axis.

.. py:property:: c
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyEllipsoid.c
    :type: float

    The polar radius along z-axis.

.. py:property:: mean_radius
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyEllipsoid.mean_radius
    :type: float

    A mean radius of the central body (a+b+c)/3.

.. py:property:: volumetric_radius
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyEllipsoid.volumetric_radius
    :type: float

    A volumetric radius of the central body (a*b*c)^(1/3).


Method detail
-------------






.. py:method:: compute_surface_distance(self, startLat: typing.Any, startLon: typing.Any, endLat: typing.Any, endLon: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyEllipsoid.compute_surface_distance

    Compute the distance between two points on the surface of the central body. Distance is measured along a great arc path.

    :Parameters:

    **startLat** : :obj:`~typing.Any`
    **startLon** : :obj:`~typing.Any`
    **endLat** : :obj:`~typing.Any`
    **endLon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

