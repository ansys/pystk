CUSTOM_FUNCTION
===============

.. py:class:: CUSTOM_FUNCTION

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ENABLE_PAGE_DEFINITION`
              - Use attitude page definition for other STK functions - the actual attitude during the maneuver is ignored and the satellite is considered to always be in the attitude specified by the page for all other calculations in STK.

            * - :py:attr:`~ENABLE_MANEUVER_ATTITUDE`
              - Maneuver attitude will be used for the satellite during the time at the maneuver, and during the specified lead and trail times. This attitude will also show up in reports, graphs, sensor access calculations, and in the 3D Graphics window.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CUSTOM_FUNCTION


