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
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_constant_term`
              - Azimuth constant term (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_linear_term`
              - Azimuth linear term (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_quadratic_term`
              - Azimuth quadratic term (dimension: angle/time^2).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_cubic_term`
              - Azimuth cubic term (dimension: angle/time^3).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_quartic_term`
              - Azimuth quartic term (dimension: angle/time^4).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_sinusoidal_amplitude`
              - Azimuth sine term amplitude (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_sinusoidal_frequency`
              - Azimuth sine term frequency (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_sinusoidal_phase`
              - Azimuth sine term phase (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_constant_term`
              - Elevation constant term (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_linear_term`
              - Elevation linear term (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_quadratic_term`
              - Elevation quadratic term (dimension: angle/time^2).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_cubic_term`
              - Elevation cubic term (dimension: angle/time^3).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_quartic_term`
              - Elevation quartic term (dimension: angle/time^4).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_sinusoidal_amplitude`
              - Elevation sine term amplitude (dimension: angle).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_sinusoidal_frequency`
              - Elevation sine term frequency (dimension: angle/time).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_sinusoidal_phase`
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

.. py:property:: azimuth_polynomial_constant_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_constant_term
    :type: float

    Azimuth constant term (dimension: angle).

.. py:property:: azimuth_polynomial_linear_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_linear_term
    :type: float

    Azimuth linear term (dimension: angle/time).

.. py:property:: azimuth_polynomial_quadratic_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_quadratic_term
    :type: float

    Azimuth quadratic term (dimension: angle/time^2).

.. py:property:: azimuth_polynomial_cubic_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_cubic_term
    :type: float

    Azimuth cubic term (dimension: angle/time^3).

.. py:property:: azimuth_polynomial_quartic_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_polynomial_quartic_term
    :type: float

    Azimuth quartic term (dimension: angle/time^4).

.. py:property:: azimuth_sinusoidal_amplitude
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_sinusoidal_amplitude
    :type: float

    Azimuth sine term amplitude (dimension: angle).

.. py:property:: azimuth_sinusoidal_frequency
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_sinusoidal_frequency
    :type: float

    Azimuth sine term frequency (dimension: angle/time).

.. py:property:: azimuth_sinusoidal_phase
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.azimuth_sinusoidal_phase
    :type: float

    Azimuth sine term phase (dimension: angle).

.. py:property:: elevation_polynomial_constant_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_constant_term
    :type: float

    Elevation constant term (dimension: angle).

.. py:property:: elevation_polynomial_linear_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_linear_term
    :type: float

    Elevation linear term (dimension: angle/time).

.. py:property:: elevation_polynomial_quadratic_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_quadratic_term
    :type: float

    Elevation quadratic term (dimension: angle/time^2).

.. py:property:: elevation_polynomial_cubic_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_cubic_term
    :type: float

    Elevation cubic term (dimension: angle/time^3).

.. py:property:: elevation_polynomial_quartic_term
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_polynomial_quartic_term
    :type: float

    Elevation quartic term (dimension: angle/time^4).

.. py:property:: elevation_sinusoidal_amplitude
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_sinusoidal_amplitude
    :type: float

    Elevation sine term amplitude (dimension: angle).

.. py:property:: elevation_sinusoidal_frequency
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_sinusoidal_frequency
    :type: float

    Elevation sine term frequency (dimension: angle/time).

.. py:property:: elevation_sinusoidal_phase
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteTimeVarying.elevation_sinusoidal_phase
    :type: float

    Elevation sine term phase (dimension: angle).


