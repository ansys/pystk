IGammaCorrectionFilter
======================

.. py:class:: IGammaCorrectionFilter

   object
   
   Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~gamma`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGammaCorrectionFilter


Property detail
---------------

.. py:property:: gamma
    :canonical: ansys.stk.core.graphics.IGammaCorrectionFilter.gamma
    :type: float

    Gets or sets the gamma value for the filter. The value must be between .2 and 5. The default gamma value is 2.2.


