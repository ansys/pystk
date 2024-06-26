IClassicalOrientation
=====================

.. py:class:: ansys.stk.core.stkobjects.IClassicalOrientation

   object
   
   Interface for specifying orbit orientation in the Classical (Keplerian) system.

.. py:currentmodule:: IClassicalOrientation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalOrientation.inclination`
              - Gets or sets the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalOrientation.arg_of_perigee`
              - Gets or sets the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalOrientation.asc_node_type`
              - Select Longitude of Ascending Node or Right Ascension of Ascending Node.
            * - :py:attr:`~ansys.stk.core.stkobjects.IClassicalOrientation.asc_node`
              - Value of Longitude of Ascending Node or Right Ascension of Ascending Node.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IClassicalOrientation


Property detail
---------------

.. py:property:: inclination
    :canonical: ansys.stk.core.stkobjects.IClassicalOrientation.inclination
    :type: float

    Gets or sets the angle between the angular momentum vector (perpendicular to the plane of the orbit) and the inertial Z axis. Uses Angle Dimension.

.. py:property:: arg_of_perigee
    :canonical: ansys.stk.core.stkobjects.IClassicalOrientation.arg_of_perigee
    :type: float

    Gets or sets the angle from the ascending node to the eccentricity vector (lowest point of orbit) measured in the direction of the satellite's motion and in the orbit plane. Uses Angle Dimension.

.. py:property:: asc_node_type
    :canonical: ansys.stk.core.stkobjects.IClassicalOrientation.asc_node_type
    :type: ORIENTATION_ASC_NODE

    Select Longitude of Ascending Node or Right Ascension of Ascending Node.

.. py:property:: asc_node
    :canonical: ansys.stk.core.stkobjects.IClassicalOrientation.asc_node
    :type: IOrientationAscNode

    Value of Longitude of Ascending Node or Right Ascension of Ascending Node.


