BrightnessFilter
================

.. py:class:: ansys.stk.core.graphics.BrightnessFilter

   Bases: :py:class:`~ansys.stk.core.graphics.IRasterFilter`

   Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

.. py:currentmodule:: BrightnessFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BrightnessFilter.adjustment`
              - Get or set the brightness adjustment value for the filter. The value must be between -1 and 1, corresponding to least bright to most bright.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import BrightnessFilter


Property detail
---------------

.. py:property:: adjustment
    :canonical: ansys.stk.core.graphics.BrightnessFilter.adjustment
    :type: float

    Get or set the brightness adjustment value for the filter. The value must be between -1 and 1, corresponding to least bright to most bright.


