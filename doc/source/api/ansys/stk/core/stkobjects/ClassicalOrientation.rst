ClassicalOrientation
====================

.. py:class:: ansys.stk.core.stkobjects.ClassicalOrientation

   Orbit orientation in the Classical (Keplerian) system.

.. py:currentmodule:: ClassicalOrientation

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalOrientation.argument_of_periapsis`
              - Get or set the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalOrientation.ascending_node`
              - Value of Longitude of Ascending Node or Right Ascension of Ascending Node.
            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalOrientation.ascending_node_type`
              - Select Longitude of Ascending Node or Right Ascension of Ascending Node.
            * - :py:attr:`~ansys.stk.core.stkobjects.ClassicalOrientation.inclination`
              - Get or set the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ClassicalOrientation


Property detail
---------------

.. py:property:: argument_of_periapsis
    :canonical: ansys.stk.core.stkobjects.ClassicalOrientation.argument_of_periapsis
    :type: float

    Get or set the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane. Uses Angle Dimension.

.. py:property:: ascending_node
    :canonical: ansys.stk.core.stkobjects.ClassicalOrientation.ascending_node
    :type: IOrientationAscNode

    Value of Longitude of Ascending Node or Right Ascension of Ascending Node.

.. py:property:: ascending_node_type
    :canonical: ansys.stk.core.stkobjects.ClassicalOrientation.ascending_node_type
    :type: OrientationAscNode

    Select Longitude of Ascending Node or Right Ascension of Ascending Node.

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.ClassicalOrientation.inclination
    :type: float

    Get or set the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.


