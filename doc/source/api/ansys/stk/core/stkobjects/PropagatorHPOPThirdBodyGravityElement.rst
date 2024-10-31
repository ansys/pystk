PropagatorHPOPThirdBodyGravityElement
=====================================

.. py:class:: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement

   Class defining third-body gravity options for the LOP propagator.

.. py:currentmodule:: PropagatorHPOPThirdBodyGravityElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement.source`
              - Source of 3rd-body gravity data.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement.gravity_value`
              - Gravity value (if the source is user-specified. Uses Gravity Parameter Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement.central_body`
              - Name of the central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorHPOPThirdBodyGravityElement


Property detail
---------------

.. py:property:: source
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement.source
    :type: THIRD_BODY_GRAVITY_SOURCE_TYPE

    Source of 3rd-body gravity data.

.. py:property:: gravity_value
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement.gravity_value
    :type: float

    Gravity value (if the source is user-specified. Uses Gravity Parameter Dimension.

.. py:property:: central_body
    :canonical: ansys.stk.core.stkobjects.PropagatorHPOPThirdBodyGravityElement.central_body
    :type: str

    Name of the central body.


