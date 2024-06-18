IContrastFilter
===============

.. py:class:: IContrastFilter

   object
   
   Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~adjustment`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IContrastFilter


Property detail
---------------

.. py:property:: adjustment
    :canonical: ansys.stk.core.graphics.IContrastFilter.adjustment
    :type: float

    Gets or sets the contrast adjustment value for the filter. The value must be between -1 and 1, corresponding to least contrast to most contrast.


