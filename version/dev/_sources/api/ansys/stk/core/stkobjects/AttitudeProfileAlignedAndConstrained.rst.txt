AttitudeProfileAlignedAndConstrained
====================================

.. py:class:: ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`

   Aligned and Constrained attitude profile.

.. py:currentmodule:: AttitudeProfileAlignedAndConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.aligned_vector`
              - Get the aligned vector pair. Vectors dependent on the satellite's body axes are invalid for this attitude profile; all other vectors are valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.constrained_vector`
              - Get the constrained vector pair. Vectors dependent on the satellite's body axes are invalid for this attitude profile; all other vectors are valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.displayed_aligned_vector_type`
              - Aligned vector type displayed on GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.displayed_constrained_vector_type`
              - Constrained vector type displayed on GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeProfileAlignedAndConstrained


Property detail
---------------

.. py:property:: aligned_vector
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.aligned_vector
    :type: VehicleVector

    Get the aligned vector pair. Vectors dependent on the satellite's body axes are invalid for this attitude profile; all other vectors are valid choices.

.. py:property:: constrained_vector
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.constrained_vector
    :type: VehicleVector

    Get the constrained vector pair. Vectors dependent on the satellite's body axes are invalid for this attitude profile; all other vectors are valid choices.

.. py:property:: displayed_aligned_vector_type
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.displayed_aligned_vector_type
    :type: DirectionType

    Aligned vector type displayed on GUI.

.. py:property:: displayed_constrained_vector_type
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileAlignedAndConstrained.displayed_constrained_vector_type
    :type: DirectionType

    Constrained vector type displayed on GUI.


