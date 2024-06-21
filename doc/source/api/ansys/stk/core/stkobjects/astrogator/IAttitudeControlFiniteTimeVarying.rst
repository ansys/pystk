IAttitudeControlFiniteTimeVarying
=================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying

   IAttitudeControlFinite
   
   Properties for the Time Varying attitude control for a Finite Maneuver.

.. py:currentmodule:: IAttitudeControlFiniteTimeVarying

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.thrust_axes_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.body_constraint_vector`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az0`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az1`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az2`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az3`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az4`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az_a`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az_f`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az_p`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el0`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el1`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el2`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el3`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el4`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el_a`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el_f`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el_p`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlFiniteTimeVarying


Property detail
---------------

.. py:property:: thrust_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.thrust_axes_name
    :type: str

    Gets or sets the thrust axes.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.body_constraint_vector
    :type: IDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: az0
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az0
    :type: float

    Azimuth constant term (dimension: angle).

.. py:property:: az1
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az1
    :type: float

    Azimuth linear term (dimension: angle/time).

.. py:property:: az2
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az2
    :type: float

    Azimuth quadratic term (dimension: angle/time^2).

.. py:property:: az3
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az3
    :type: float

    Azimuth cubic term (dimension: angle/time^3).

.. py:property:: az4
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az4
    :type: float

    Azimuth quartic term (dimension: angle/time^4).

.. py:property:: az_a
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az_a
    :type: float

    Azimuth sine term amplitude (dimension: angle).

.. py:property:: az_f
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az_f
    :type: float

    Azimuth sine term frequency (dimension: angle/time).

.. py:property:: az_p
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.az_p
    :type: float

    Azimuth sine term phase (dimension: angle).

.. py:property:: el0
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el0
    :type: float

    Elevation constant term (dimension: angle).

.. py:property:: el1
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el1
    :type: float

    Elevation linear term (dimension: angle/time).

.. py:property:: el2
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el2
    :type: float

    Elevation quadratic term (dimension: angle/time^2).

.. py:property:: el3
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el3
    :type: float

    Elevation cubic term (dimension: angle/time^3).

.. py:property:: el4
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el4
    :type: float

    Elevation quartic term (dimension: angle/time^4).

.. py:property:: el_a
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el_a
    :type: float

    Elevation sine term amplitude (dimension: angle).

.. py:property:: el_f
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el_f
    :type: float

    Elevation sine term frequency (dimension: angle/time).

.. py:property:: el_p
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteTimeVarying.el_p
    :type: float

    Elevation sine term phase (dimension: angle).


