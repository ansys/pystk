BURNOUT_OPTIONS
===============

.. py:class:: BURNOUT_OPTIONS

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FIXED_VELOCITY`
              - Use Fixed Velocity - the inclination of the final state of the launch segment is determined by the arc between the launch and insertion positions, and the horizontal flight path angle is set to zero.

            * - :py:attr:`~INERTIAL_VELOCITY`
              - Use Inertial Velocity - the final state of the launch segment is solely and completely determined by the burnout position and velocity.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BURNOUT_OPTIONS


