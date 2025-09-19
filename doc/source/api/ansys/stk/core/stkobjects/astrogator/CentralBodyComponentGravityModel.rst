CentralBodyComponentGravityModel
================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel

   Central Body Gravity Model.

.. py:currentmodule:: CentralBodyComponentGravityModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.gravitational_parameter`
              - Get or set the gravitational parameter to be used for purposes of this gravity model. Uses Gravitational Param Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.j2`
              - Get or set the J2 property. Taking into account first order Earth oblateness effects. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.j3`
              - Get or set the J3 property. Taking into account first order longitudinal variations of the Earth's shape. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.j4`
              - Get or set the J4 property. Taking into account first and second order Earth oblateness effects. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.reference_distance`
              - Distance from the center of mass of the central body to its surface. Typically defaults to the Maximum Radius entered in the Shape frame of the Central Body parameters window. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CentralBodyComponentGravityModel


Property detail
---------------

.. py:property:: gravitational_parameter
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.gravitational_parameter
    :type: float

    Get or set the gravitational parameter to be used for purposes of this gravity model. Uses Gravitational Param Dimension.

.. py:property:: j2
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.j2
    :type: float

    Get or set the J2 property. Taking into account first order Earth oblateness effects. Dimensionless.

.. py:property:: j3
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.j3
    :type: float

    Get or set the J3 property. Taking into account first order longitudinal variations of the Earth's shape. Dimensionless.

.. py:property:: j4
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.j4
    :type: float

    Get or set the J4 property. Taking into account first and second order Earth oblateness effects. Dimensionless.

.. py:property:: reference_distance
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponentGravityModel.reference_distance
    :type: float

    Distance from the center of mass of the central body to its surface. Typically defaults to the Maximum Radius entered in the Shape frame of the Central Body parameters window. Uses Distance Dimension.


