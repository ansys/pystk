VEHICLE_SGP4_AUTO_UPDATE_SOURCE
===============================

.. py:class:: VEHICLE_SGP4_AUTO_UPDATE_SOURCE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~SGP4_AUTO_UPDATE_SOURCE_UNKNOWN`
              - Unknown or unsupported TLE source.

            * - :py:attr:`~SGP4_AUTO_UPDATE_SOURCE_ONLINE`
              - Retrieve TLEs from an online source (AGI server).

            * - :py:attr:`~SGP4_AUTO_UPDATE_ONLINE_SPACE_TRACK`
              - Retrieve TLEs from the space track. Not currently supported.

            * - :py:attr:`~SGP4_AUTO_UPDATE_SOURCE_FILE`
              - Retrieve TLEs from a file.

            * - :py:attr:`~SGP4_AUTO_UPDATE_NONE`
              - Manually specify/import TLEs, no auto-updates will be performed during propagation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_SGP4_AUTO_UPDATE_SOURCE


