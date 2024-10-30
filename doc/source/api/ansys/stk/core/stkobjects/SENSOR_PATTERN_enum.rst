SENSOR_PATTERN
==============

.. py:class:: ansys.stk.core.stkobjects.SENSOR_PATTERN

   IntEnum


.. py:currentmodule:: SENSOR_PATTERN

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~COMPLEX_CONIC`
              - Complex conic: defined by specified inner and outer half angles and minimum and maximum clock angles.

            * - :py:attr:`~CUSTOM`
              - Custom: import a custom sensor pattern file.

            * - :py:attr:`~HALF_POWER`
              - Half power: models a parabolic antenna.

            * - :py:attr:`~RECTANGULAR`
              - Rectangular: specify vertical and horizontal half-angles that will be used to model the field of view of an instrument.

            * - :py:attr:`~SAR`
              - SAR: synthesizes the aperture of a larger antenna than is actually present, using SAR pattern definitions designed to model the field of regard of a SAR sensor onto the surface of the earth.

            * - :py:attr:`~SIMPLE_CONIC`
              - Simple conic: defined by a specified cone angle.

            * - :py:attr:`~EOIR`
              - EOIR: defined by Band Properties.

            * - :py:attr:`~UNKNOWN`
              - Unknown/unsupported sensor pattern.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SENSOR_PATTERN


