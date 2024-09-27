ElementBPlane
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.ElementBPlane

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IElement`

   Bplane elements.

.. py:currentmodule:: ElementBPlane

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.right_ascension_of_b_plane`
              - Right Ascension of the B-Plane Normal.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.declination_of_b_plane`
              - Declination of the B-Plane Normal.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_r_first_b_vector`
              - B vector dotted with R vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_t_second_b_vector`
              - B vector dotted with T vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.hyperbolic_turning_angle`
              - Hyperbolic turning angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.orbital_c3_energy`
              - Orbital C3 Energy.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.hyperbolic_v_infinity`
              - Hyperbolic V infinity.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.semimajor_axis`
              - Semi-major axis.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_t_first_b_vector`
              - B vector dotted with T vector used as the first quantity to define the B vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_theta_first_b_vector`
              - Angle between the B vector and T vector used as the first quantity to define the B vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_r_second_b_vector`
              - B vector dotted with T vector used as the second quantity to define the B vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_magnitude_second_b_vector`
              - Magnitude of the B vector used as the second quantity to define the B vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ElementBPlane.true_anomaly`
              - True Anomaly.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ElementBPlane


Property detail
---------------

.. py:property:: right_ascension_of_b_plane
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.right_ascension_of_b_plane
    :type: float

    Right Ascension of the B-Plane Normal.

.. py:property:: declination_of_b_plane
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.declination_of_b_plane
    :type: float

    Declination of the B-Plane Normal.

.. py:property:: b_dot_r_first_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_r_first_b_vector
    :type: float

    B vector dotted with R vector.

.. py:property:: b_dot_t_second_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_t_second_b_vector
    :type: float

    B vector dotted with T vector.

.. py:property:: hyperbolic_turning_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.hyperbolic_turning_angle
    :type: float

    Hyperbolic turning angle.

.. py:property:: orbital_c3_energy
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.orbital_c3_energy
    :type: float

    Orbital C3 Energy.

.. py:property:: hyperbolic_v_infinity
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.hyperbolic_v_infinity
    :type: float

    Hyperbolic V infinity.

.. py:property:: semimajor_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.semimajor_axis
    :type: float

    Semi-major axis.

.. py:property:: b_dot_t_first_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_t_first_b_vector
    :type: float

    B vector dotted with T vector used as the first quantity to define the B vector.

.. py:property:: b_theta_first_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_theta_first_b_vector
    :type: float

    Angle between the B vector and T vector used as the first quantity to define the B vector.

.. py:property:: b_dot_r_second_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_dot_r_second_b_vector
    :type: float

    B vector dotted with T vector used as the second quantity to define the B vector.

.. py:property:: b_magnitude_second_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.b_magnitude_second_b_vector
    :type: float

    Magnitude of the B vector used as the second quantity to define the B vector.

.. py:property:: true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.ElementBPlane.true_anomaly
    :type: float

    True Anomaly.


