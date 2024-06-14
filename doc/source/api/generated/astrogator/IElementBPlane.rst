IElementBPlane
==============

.. py:class:: IElementBPlane

   IElement
   
   Properties for BPlane elements.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~right_ascension_of_b_plane`
            * - :py:meth:`~declination_of_b_plane`
            * - :py:meth:`~b_dot_r_first_b_vector`
            * - :py:meth:`~b_dot_t_second_b_vector`
            * - :py:meth:`~hyperbolic_turning_angle`
            * - :py:meth:`~orbital_c3_energy`
            * - :py:meth:`~hyperbolic_v_infinity`
            * - :py:meth:`~semi_major_axis`
            * - :py:meth:`~b_dot_t_first_b_vector`
            * - :py:meth:`~b_theta_first_b_vector`
            * - :py:meth:`~b_dot_r_second_b_vector`
            * - :py:meth:`~b_magnitude_second_b_vector`
            * - :py:meth:`~true_anomaly`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IElementBPlane


Property detail
---------------

.. py:property:: right_ascension_of_b_plane
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.right_ascension_of_b_plane
    :type: float

    Right Ascension of the B-Plane Normal.

.. py:property:: declination_of_b_plane
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.declination_of_b_plane
    :type: float

    Declination of the B-Plane Normal.

.. py:property:: b_dot_r_first_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.b_dot_r_first_b_vector
    :type: float

    B vector dotted with R vector.

.. py:property:: b_dot_t_second_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.b_dot_t_second_b_vector
    :type: float

    B vector dotted with T vector.

.. py:property:: hyperbolic_turning_angle
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.hyperbolic_turning_angle
    :type: float

    Hyperbolic turning angle.

.. py:property:: orbital_c3_energy
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.orbital_c3_energy
    :type: float

    Orbital C3 Energy.

.. py:property:: hyperbolic_v_infinity
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.hyperbolic_v_infinity
    :type: float

    Hyperbolic V infinity.

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.semi_major_axis
    :type: float

    Semi-major axis.

.. py:property:: b_dot_t_first_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.b_dot_t_first_b_vector
    :type: float

    B vector dotted with T vector used as the first quantity to define the B vector.

.. py:property:: b_theta_first_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.b_theta_first_b_vector
    :type: float

    Angle between the B vector and T vector used as the first quantity to define the B vector.

.. py:property:: b_dot_r_second_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.b_dot_r_second_b_vector
    :type: float

    B vector dotted with T vector used as the second quantity to define the B vector.

.. py:property:: b_magnitude_second_b_vector
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.b_magnitude_second_b_vector
    :type: float

    Magnitude of the B vector used as the second quantity to define the B vector.

.. py:property:: true_anomaly
    :canonical: ansys.stk.core.stkobjects.astrogator.IElementBPlane.true_anomaly
    :type: float

    True Anomaly.


