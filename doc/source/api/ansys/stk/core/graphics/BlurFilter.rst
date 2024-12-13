BlurFilter
==========

.. py:class:: ansys.stk.core.graphics.BlurFilter

   Bases: :py:class:`~ansys.stk.core.graphics.IConvolutionFilter`, :py:class:`~ansys.stk.core.graphics.IRasterFilter`

   Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

.. py:currentmodule:: BlurFilter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.BlurFilter.method`
              - Gets or sets the method used to blur the source raster.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import BlurFilter


Property detail
---------------

.. py:property:: method
    :canonical: ansys.stk.core.graphics.BlurFilter.method
    :type: BlurMethod

    Gets or sets the method used to blur the source raster.


