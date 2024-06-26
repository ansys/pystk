SHADOW_MODEL
============

.. py:class:: ansys.stk.core.stkobjects.SHADOW_MODEL

   IntEnum


.. py:currentmodule:: SHADOW_MODEL

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~MOD_CYLINDRICAL`
              - Cylindrical: assumes the Sun to be at infinite distance so that all light coming from the Sun moves in a direction parallel to the Sun to satellite vector.

            * - :py:attr:`~MOD_DUAL_CONE`
              - Dual cone: uses the actual size and distance of the Sun to model regions of full, partial and zero sunlight.

            * - :py:attr:`~MOD_NONE`
              - None. No shadowing of the satellite is modeled.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SHADOW_MODEL


