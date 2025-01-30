DisplayTimesType
================

.. py:class:: ansys.stk.core.stkobjects.DisplayTimesType

   IntEnum


.. py:currentmodule:: DisplayTimesType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown display type.

            * - :py:attr:`~ALWAYS_OFF`
              - Graphics for the object never display.

            * - :py:attr:`~ALWAYS_ON`
              - Graphics for the object always display.

            * - :py:attr:`~DURING_ACCESS`
              - Graphics for the object display during access to specified objects.

            * - :py:attr:`~INTERVALS`
              - Graphics for the object display during user-defined intervals.

            * - :py:attr:`~DURING_CHAIN_ACCESS`
              - Graphics for the object display during chain access.

            * - :py:attr:`~TIME_COMPONENT`
              - Graphics for the object display during the intervals provided by an interval or interval list time component.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DisplayTimesType


