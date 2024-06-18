IGammaCorrectionFilterFactory
=============================

.. py:class:: IGammaCorrectionFilterFactory

   object
   
   Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new instance.
            * - :py:meth:`~initialize_with_gamma`
              - Initialize a new instance with the specified gamma.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGammaCorrectionFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IGammaCorrectionFilter"

    Initialize a new instance.

    :Returns:

        :obj:`~"IGammaCorrectionFilter"`

.. py:method:: initialize_with_gamma(self, gamma:float) -> "IGammaCorrectionFilter"

    Initialize a new instance with the specified gamma.

    :Parameters:

    **gamma** : :obj:`~float`

    :Returns:

        :obj:`~"IGammaCorrectionFilter"`

