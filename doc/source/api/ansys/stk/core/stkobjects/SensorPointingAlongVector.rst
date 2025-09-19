SensorPointingAlongVector
=========================

.. py:class:: ansys.stk.core.stkobjects.SensorPointingAlongVector

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISensorPointing`

   Class defining the along vector pointing type for a Sensor.

.. py:currentmodule:: SensorPointingAlongVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingAlongVector.alignment_vector`
              - The alignment vector for along vector sensor pointing alignment.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingAlongVector.available_alignment_vectors`
              - Get the available Alignment Vectors.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingAlongVector.available_constraint_vectors`
              - Get the available Constraint Vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingAlongVector.clock_angle_offset`
              - The clock angle offset for along vector sensor pointing alignment.It is an optional value that is entered in degrees, between -360.0 and 360.0.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorPointingAlongVector.constraint_vector`
              - The constraint vector for along vector sensor pointing alignment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorPointingAlongVector


Property detail
---------------

.. py:property:: alignment_vector
    :canonical: ansys.stk.core.stkobjects.SensorPointingAlongVector.alignment_vector
    :type: str

    The alignment vector for along vector sensor pointing alignment.

.. py:property:: available_alignment_vectors
    :canonical: ansys.stk.core.stkobjects.SensorPointingAlongVector.available_alignment_vectors
    :type: list

    Get the available Alignment Vectors.

.. py:property:: available_constraint_vectors
    :canonical: ansys.stk.core.stkobjects.SensorPointingAlongVector.available_constraint_vectors
    :type: list

    Get the available Constraint Vector.

.. py:property:: clock_angle_offset
    :canonical: ansys.stk.core.stkobjects.SensorPointingAlongVector.clock_angle_offset
    :type: typing.Any

    The clock angle offset for along vector sensor pointing alignment.It is an optional value that is entered in degrees, between -360.0 and 360.0.

.. py:property:: constraint_vector
    :canonical: ansys.stk.core.stkobjects.SensorPointingAlongVector.constraint_vector
    :type: str

    The constraint vector for along vector sensor pointing alignment.


