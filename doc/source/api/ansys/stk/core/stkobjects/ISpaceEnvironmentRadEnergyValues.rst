ISpaceEnvironmentRadEnergyValues
================================

.. py:class:: ansys.stk.core.stkobjects.ISpaceEnvironmentRadEnergyValues

   object
   
   Energy values for computing electron and proton flux.

.. py:currentmodule:: ISpaceEnvironmentRadEnergyValues

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadEnergyValues.use_default`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISpaceEnvironmentRadEnergyValues.custom`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISpaceEnvironmentRadEnergyValues


Property detail
---------------

.. py:property:: use_default
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadEnergyValues.use_default
    :type: bool

    Use default energy values.

.. py:property:: custom
    :canonical: ansys.stk.core.stkobjects.ISpaceEnvironmentRadEnergyValues.custom
    :type: ISpaceEnvironmentRadEnergyMethodSpecify

    Specify custom energy values that will override the default energy values.


