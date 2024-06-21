IAttitudeControl
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControl

   object
   
   Properties for attitude options for a maneuver segment.

.. py:currentmodule:: IAttitudeControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl.lead_duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl.trail_duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl.body_axis`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl.constraint_sign`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl.constraint_vector_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl.custom_function`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControl


Property detail
---------------

.. py:property:: lead_duration
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControl.lead_duration
    :type: float

    How long before the maneuver starts the maneuver attitude. Uses Time Dimension.

.. py:property:: trail_duration
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControl.trail_duration
    :type: float

    How long to maintain that attitude after the maneuver. Uses Time Dimension.

.. py:property:: body_axis
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControl.body_axis
    :type: BODY_AXIS

    Whether the engine acceleration (the direction opposite the engine's exhaust) is aligned with positive or negative X, Y or Z body axis.

.. py:property:: constraint_sign
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControl.constraint_sign
    :type: CONSTRAINT_SIGN

    Whether the Constraint Vector is positive or negative.

.. py:property:: constraint_vector_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControl.constraint_vector_name
    :type: str

    Constraint Vector - the vector toward which this body vector is constrained.

.. py:property:: custom_function
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControl.custom_function
    :type: CUSTOM_FUNCTION

    Gets or sets the attitude definition to use for other STK functions.


