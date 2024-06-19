ITimeToolTimeProperties
=======================

.. py:class:: ITimeToolTimeProperties

   object
   
   Define methods to compute time properties such as availability and special times.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_availability`
              - Return a collection of availability intervals.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolTimeProperties



Method detail
-------------

.. py:method:: get_availability(self) -> ITimeToolIntervalCollection
    :canonical: ansys.stk.core.vgt.ITimeToolTimeProperties.get_availability

    Return a collection of availability intervals.

    :Returns:

        :obj:`~ITimeToolIntervalCollection`

