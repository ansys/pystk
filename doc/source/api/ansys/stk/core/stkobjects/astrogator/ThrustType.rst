ThrustType
==========

.. py:class:: ansys.stk.core.stkobjects.astrogator.ThrustType

   IntEnum


.. py:currentmodule:: ThrustType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~AFFECTS_ACCELERATION_AND_MASS_FLOW`
              - Affects Acceleration and Mass Flow Calculations - may represent an inefficiency in the propulsion tanks and feed lines.

            * - :py:attr:`~AFFECTS_ACCELERATION_ONLY`
              - Affects Acceleration Only - an efficiency of 0.98 means that only 98% of the fuel will be spent to get 98% thrust. For example, a thrust efficiency affecting acceleration only may represent some problem in the combustion chamber.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ThrustType


