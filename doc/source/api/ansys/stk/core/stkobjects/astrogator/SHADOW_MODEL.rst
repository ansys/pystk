SHADOW_MODEL
============

.. py:class:: SHADOW_MODEL

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CYLINDRICAL`
              - Cylindrical - assumes the Sun to be at infinite distance so that all light coming from the Sun moves in a direction parallel to the Sun to satellite vector.

            * - :py:attr:`~DUAL_CONE`
              - Dual Cone - uses the actual size and distance of the Sun to model regions of full, partial (penumbra) and zero (umbra) sunlight. The visible fraction of the solar disk is used to compute the acceleration during penumbra.

            * - :py:attr:`~NONE`
              - None - turns off all shadowing of the satellite.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SHADOW_MODEL


