ICentralBodyShapeOblateSpheroid
===============================

.. py:class:: ICentralBodyShapeOblateSpheroid

   ICentralBodyShape
   
   Properties for the central body oblate spheroid shape.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~min_radius`
            * - :py:meth:`~max_radius`
            * - :py:meth:`~flattening_coefficient`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ICentralBodyShapeOblateSpheroid


Property detail
---------------

.. py:property:: min_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyShapeOblateSpheroid.min_radius
    :type: float

    Gets or sets the minimum radius. Uses Distance Dimension.

.. py:property:: max_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyShapeOblateSpheroid.max_radius
    :type: float

    Gets or sets the maximum radius. Uses Distance Dimension.

.. py:property:: flattening_coefficient
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyShapeOblateSpheroid.flattening_coefficient
    :type: float

    Get the flattening coefficient; automatically derived from the minimum and maximum radii. Dimensionless.


