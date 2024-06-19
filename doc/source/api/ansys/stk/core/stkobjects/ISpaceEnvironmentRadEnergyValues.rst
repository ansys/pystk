ISpaceEnvironmentRadEnergyValues
================================

.. py:class:: ISpaceEnvironmentRadEnergyValues

   object
   
   Energy values for computing electron and proton flux.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~use_default`
            * - :py:meth:`~custom`


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
    :type: IAgSpEnvRadEnergyMethodSpecify

    Specify custom energy values that will override the default energy values.


