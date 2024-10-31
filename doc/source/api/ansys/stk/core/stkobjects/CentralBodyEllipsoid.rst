CentralBodyEllipsoid
====================

.. py:class:: ansys.stk.core.stkobjects.CentralBodyEllipsoid

   Central body's ellipsoid information.

.. py:currentmodule:: CentralBodyEllipsoid

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyEllipsoid.compute_surface_distance`
              - Compute the distance between two points on the surface of the central body. Distance is measured along a great arc path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyEllipsoid.radius_a`
              - An equatorial radius along the x-axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyEllipsoid.radius_b`
              - An equatorial radius along the y-axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyEllipsoid.radius_c`
              - The polar radius along z-axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyEllipsoid.mean_radius`
              - A mean radius of the central body (a+b+c)/3.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyEllipsoid.volumetric_radius`
              - A volumetric radius of the central body (a*b*c)^(1/3).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CentralBodyEllipsoid


Property detail
---------------

.. py:property:: radius_a
    :canonical: ansys.stk.core.stkobjects.CentralBodyEllipsoid.radius_a
    :type: float

    An equatorial radius along the x-axis.

.. py:property:: radius_b
    :canonical: ansys.stk.core.stkobjects.CentralBodyEllipsoid.radius_b
    :type: float

    An equatorial radius along the y-axis.

.. py:property:: radius_c
    :canonical: ansys.stk.core.stkobjects.CentralBodyEllipsoid.radius_c
    :type: float

    The polar radius along z-axis.

.. py:property:: mean_radius
    :canonical: ansys.stk.core.stkobjects.CentralBodyEllipsoid.mean_radius
    :type: float

    A mean radius of the central body (a+b+c)/3.

.. py:property:: volumetric_radius
    :canonical: ansys.stk.core.stkobjects.CentralBodyEllipsoid.volumetric_radius
    :type: float

    A volumetric radius of the central body (a*b*c)^(1/3).


Method detail
-------------






.. py:method:: compute_surface_distance(self, startLat: typing.Any, startLon: typing.Any, endLat: typing.Any, endLon: typing.Any) -> float
    :canonical: ansys.stk.core.stkobjects.CentralBodyEllipsoid.compute_surface_distance

    Compute the distance between two points on the surface of the central body. Distance is measured along a great arc path.

    :Parameters:

    **startLat** : :obj:`~typing.Any`
    **startLon** : :obj:`~typing.Any`
    **endLat** : :obj:`~typing.Any`
    **endLon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~float`

