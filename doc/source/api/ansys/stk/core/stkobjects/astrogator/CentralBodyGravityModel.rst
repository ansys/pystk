CentralBodyGravityModel
=======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel

   Central Body Gravity Model.

.. py:currentmodule:: CentralBodyGravityModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.gravitational_param`
              - Gets or sets the gravitational parameter to be used for purposes of this gravity model. Uses Gravitational Param Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.reference_distance`
              - Distance from the center of mass of the central body to its surface. Typically defaults to the Maximum Radius entered in the Shape frame of the Central Body parameters window. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.j2`
              - Gets or sets the J2 property. Taking into account first order Earth oblateness effects. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.j3`
              - Gets or sets the J3 property. Taking into account first order longitudinal variations of the Earth's shape. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.j4`
              - Gets or sets the J4 property. Taking into account first and second order Earth oblateness effects. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CentralBodyGravityModel


Property detail
---------------

.. py:property:: gravitational_param
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.gravitational_param
    :type: float

    Gets or sets the gravitational parameter to be used for purposes of this gravity model. Uses Gravitational Param Dimension.

.. py:property:: reference_distance
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.reference_distance
    :type: float

    Distance from the center of mass of the central body to its surface. Typically defaults to the Maximum Radius entered in the Shape frame of the Central Body parameters window. Uses Distance Dimension.

.. py:property:: j2
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.j2
    :type: float

    Gets or sets the J2 property. Taking into account first order Earth oblateness effects. Dimensionless.

.. py:property:: j3
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.j3
    :type: float

    Gets or sets the J3 property. Taking into account first order longitudinal variations of the Earth's shape. Dimensionless.

.. py:property:: j4
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyGravityModel.j4
    :type: float

    Gets or sets the J4 property. Taking into account first and second order Earth oblateness effects. Dimensionless.


