IReTransmitterModel
===================

.. py:class:: ansys.stk.core.stkobjects.IReTransmitterModel

   Provide access to the properties and methods defining a re-transmitter model.

.. py:currentmodule:: IReTransmitterModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.frequency_transfer_function_polynomial`
              - Gets the frequency transfer function polynomial collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_type`
              - Gets or sets the power back off transfer function type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_linear_scale`
              - Gets or sets the option to enable power back off linear scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_polynomial`
              - Gets the power back off transfer function polynomial collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_table`
              - Gets the power back off transfer function table.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.enable_c_over_im`
              - Gets or sets the option to enable C/Im.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_type`
              - Gets or sets the C/Im transfer function type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_linear_scale`
              - Gets or sets the option to enable C/Im linear scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_polynomial`
              - Gets the C/Im transfer function polynomial collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_table`
              - Gets the C/Im transfer function table.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.saturated_flux_density`
              - Gets or sets the saturated flux density.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.operational_mode`
              - Gets or sets the operational mode.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReTransmitterModel


Property detail
---------------

.. py:property:: frequency_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.frequency_transfer_function_polynomial
    :type: TransferFunctionPolynomialCollection

    Gets the frequency transfer function polynomial collection.

.. py:property:: power_back_off_transfer_function_type
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_type
    :type: TransferFunctionType

    Gets or sets the power back off transfer function type.

.. py:property:: power_back_off_linear_scale
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_linear_scale
    :type: bool

    Gets or sets the option to enable power back off linear scale.

.. py:property:: power_back_off_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_polynomial
    :type: TransferFunctionPolynomialCollection

    Gets the power back off transfer function polynomial collection.

.. py:property:: power_back_off_transfer_function_table
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_table
    :type: TransferFunctionInputBackOffOutputBackOffTable

    Gets the power back off transfer function table.

.. py:property:: enable_c_over_im
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.enable_c_over_im
    :type: bool

    Gets or sets the option to enable C/Im.

.. py:property:: c_over_im_transfer_function_type
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_type
    :type: TransferFunctionType

    Gets or sets the C/Im transfer function type.

.. py:property:: c_over_im_linear_scale
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_linear_scale
    :type: bool

    Gets or sets the option to enable C/Im linear scale.

.. py:property:: c_over_im_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_polynomial
    :type: TransferFunctionPolynomialCollection

    Gets the C/Im transfer function polynomial collection.

.. py:property:: c_over_im_transfer_function_table
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_table
    :type: TransferFunctionInputBackOffVsCOverImTable

    Gets the C/Im transfer function table.

.. py:property:: saturated_flux_density
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.saturated_flux_density
    :type: float

    Gets or sets the saturated flux density.

.. py:property:: operational_mode
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.operational_mode
    :type: ReTransmitterOpMode

    Gets or sets the operational mode.


