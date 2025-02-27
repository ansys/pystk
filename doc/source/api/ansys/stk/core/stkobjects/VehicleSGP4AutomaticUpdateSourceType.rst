VehicleSGP4AutomaticUpdateSourceType
====================================

.. py:class:: ansys.stk.core.stkobjects.VehicleSGP4AutomaticUpdateSourceType

   IntEnum


.. py:currentmodule:: VehicleSGP4AutomaticUpdateSourceType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported TLE source.

            * - :py:attr:`~ONLINE`
              - Retrieve TLEs from an online source (AGI server).

            * - :py:attr:`~ONLINE_SPACE_TRACK`
              - Retrieve TLEs from the space track. Not currently supported.

            * - :py:attr:`~FILE`
              - Retrieve TLEs from a file.

            * - :py:attr:`~NONE`
              - Manually specify/import TLEs, no auto-updates will be performed during propagation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSGP4AutomaticUpdateSourceType


