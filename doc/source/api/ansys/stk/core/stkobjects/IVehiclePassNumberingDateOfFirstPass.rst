IVehiclePassNumberingDateOfFirstPass
====================================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePassNumberingDateOfFirstPass

   IVehiclePassNumbering
   
   Date of first pass for pass numbering.

.. py:currentmodule:: IVehiclePassNumberingDateOfFirstPass

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassNumberingDateOfFirstPass.first_pass_num`
              - Gets or sets the number at which pass numbering begins. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePassNumberingDateOfFirstPass.pass_data_epoch`
              - Get the start time of the first pass.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePassNumberingDateOfFirstPass


Property detail
---------------

.. py:property:: first_pass_num
    :canonical: ansys.stk.core.stkobjects.IVehiclePassNumberingDateOfFirstPass.first_pass_num
    :type: int

    Gets or sets the number at which pass numbering begins. Dimensionless.

.. py:property:: pass_data_epoch
    :canonical: ansys.stk.core.stkobjects.IVehiclePassNumberingDateOfFirstPass.pass_data_epoch
    :type: ITimeToolEventSmartEpoch

    Get the start time of the first pass.


