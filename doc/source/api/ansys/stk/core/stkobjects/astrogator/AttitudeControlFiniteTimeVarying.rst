AttitudeControlFiniteTimeVarying
================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The time varying attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteTimeVarying

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.thrust_axes_name`
              - Gets or sets the thrust axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.body_constraint_vector`
              - Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az0`
              - Azimuth constant term (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az1`
              - Azimuth linear term (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az2`
              - Azimuth quadratic term (dimension: angle/time^2).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az3`
              - Azimuth cubic term (dimension: angle/time^3).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az4`
              - Azimuth quartic term (dimension: angle/time^4).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az_a`
              - Azimuth sine term amplitude (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az_f`
              - Azimuth sine term frequency (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az_p`
              - Azimuth sine term phase (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el0`
              - Elevation constant term (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el1`
              - Elevation linear term (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el2`
              - Elevation quadratic term (dimension: angle/time^2).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el3`
              - Elevation cubic term (dimension: angle/time^3).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el4`
              - Elevation quartic term (dimension: angle/time^4).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el_a`
              - Elevation sine term amplitude (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el_f`
              - Elevation sine term frequency (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el_p`
              - Elevation sine term phase (dimension: angle).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlFiniteTimeVarying


Property detail
---------------

.. py:property:: thrust_axes_name
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.thrust_axes_name
    :type: str

    Gets or sets the thrust axes.

.. py:property:: body_constraint_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.body_constraint_vector
    :type: IDirection

    Defines a constraint vector in spacecraft body coordinates to complete the attitude definition.

.. py:property:: az0
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az0
    :type: float

    Azimuth constant term (dimension: angle).

.. py:property:: az1
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az1
    :type: float

    Azimuth linear term (dimension: angle/time).

.. py:property:: az2
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az2
    :type: float

    Azimuth quadratic term (dimension: angle/time^2).

.. py:property:: az3
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az3
    :type: float

    Azimuth cubic term (dimension: angle/time^3).

.. py:property:: az4
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az4
    :type: float

    Azimuth quartic term (dimension: angle/time^4).

.. py:property:: az_a
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az_a
    :type: float

    Azimuth sine term amplitude (dimension: angle).

.. py:property:: az_f
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az_f
    :type: float

    Azimuth sine term frequency (dimension: angle/time).

.. py:property:: az_p
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.az_p
    :type: float

    Azimuth sine term phase (dimension: angle).

.. py:property:: el0
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el0
    :type: float

    Elevation constant term (dimension: angle).

.. py:property:: el1
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el1
    :type: float

    Elevation linear term (dimension: angle/time).

.. py:property:: el2
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el2
    :type: float

    Elevation quadratic term (dimension: angle/time^2).

.. py:property:: el3
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el3
    :type: float

    Elevation cubic term (dimension: angle/time^3).

.. py:property:: el4
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el4
    :type: float

    Elevation quartic term (dimension: angle/time^4).

.. py:property:: el_a
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el_a
    :type: float

    Elevation sine term amplitude (dimension: angle).

.. py:property:: el_f
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el_f
    :type: float

    Elevation sine term frequency (dimension: angle/time).

.. py:property:: el_p
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.el_p
    :type: float

    Elevation sine term phase (dimension: angle).


