IComponentTimeProperties
========================

.. py:class:: ansys.stk.core.vgt.IComponentTimeProperties

   Define methods to compute time properties such as availability and special times.

.. py:currentmodule:: IComponentTimeProperties

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IComponentTimeProperties.get_availability`
              - Return a collection of availability intervals.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IComponentTimeProperties



Method detail
-------------

.. py:method:: get_availability(self) -> TimeToolIntervalCollection
    :canonical: ansys.stk.core.vgt.IComponentTimeProperties.get_availability

    Return a collection of availability intervals.

    :Returns:

        :obj:`~TimeToolIntervalCollection`

