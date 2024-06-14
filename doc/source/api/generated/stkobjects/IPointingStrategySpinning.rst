IPointingStrategySpinning
=========================

.. py:class:: IPointingStrategySpinning

   object
   
   Provide the interface for a spinning pointing strategy.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~spin_axes_orientation`
            * - :py:meth:`~cone_angle`
            * - :py:meth:`~spin_rate`
            * - :py:meth:`~initial_offset_angle`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPointingStrategySpinning


Property detail
---------------

.. py:property:: spin_axes_orientation
    :canonical: ansys.stk.core.stkobjects.IPointingStrategySpinning.spin_axes_orientation
    :type: "IAgOrientation"

    Gets the spin axes orientation.

.. py:property:: cone_angle
    :canonical: ansys.stk.core.stkobjects.IPointingStrategySpinning.cone_angle
    :type: float

    Gets the cone angle.

.. py:property:: spin_rate
    :canonical: ansys.stk.core.stkobjects.IPointingStrategySpinning.spin_rate
    :type: float

    Gets the spin rate.

.. py:property:: initial_offset_angle
    :canonical: ansys.stk.core.stkobjects.IPointingStrategySpinning.initial_offset_angle
    :type: float

    Gets the initial offset angle.


