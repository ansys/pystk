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

            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_linear_scale`
              - Get or set the option to enable C/Im linear scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_polynomial`
              - Get the C/Im transfer function polynomial collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_table`
              - Get the C/Im transfer function table.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_type`
              - Get or set the C/Im transfer function type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.enable_c_over_im`
              - Get or set the option to enable C/Im.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.frequency_transfer_function_polynomial`
              - Get the frequency transfer function polynomial collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.operational_mode`
              - Get or set the operational mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_linear_scale`
              - Get or set the option to enable power back off linear scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_polynomial`
              - Get the power back off transfer function polynomial collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_table`
              - Get the power back off transfer function table.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_type`
              - Get or set the power back off transfer function type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReTransmitterModel.saturated_flux_density`
              - Get or set the saturated flux density.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReTransmitterModel


Property detail
---------------

.. py:property:: c_over_im_linear_scale
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_linear_scale
    :type: bool

    Get or set the option to enable C/Im linear scale.

.. py:property:: c_over_im_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_polynomial
    :type: TransferFunctionPolynomialCollection

    Get the C/Im transfer function polynomial collection.

.. py:property:: c_over_im_transfer_function_table
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_table
    :type: TransferFunctionInputBackOffVsCOverImTable

    Get the C/Im transfer function table.

.. py:property:: c_over_im_transfer_function_type
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_type
    :type: TransferFunctionType

    Get or set the C/Im transfer function type.

.. py:property:: enable_c_over_im
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.enable_c_over_im
    :type: bool

    Get or set the option to enable C/Im.

.. py:property:: frequency_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.frequency_transfer_function_polynomial
    :type: TransferFunctionPolynomialCollection

    Get the frequency transfer function polynomial collection.

.. py:property:: operational_mode
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.operational_mode
    :type: ReTransmitterOpMode

    Get or set the operational mode.

.. py:property:: power_back_off_linear_scale
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_linear_scale
    :type: bool

    Get or set the option to enable power back off linear scale.

.. py:property:: power_back_off_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_polynomial
    :type: TransferFunctionPolynomialCollection

    Get the power back off transfer function polynomial collection.

.. py:property:: power_back_off_transfer_function_table
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_table
    :type: TransferFunctionInputBackOffOutputBackOffTable

    Get the power back off transfer function table.

.. py:property:: power_back_off_transfer_function_type
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_type
    :type: TransferFunctionType

    Get or set the power back off transfer function type.

.. py:property:: saturated_flux_density
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.saturated_flux_density
    :type: float

    Get or set the saturated flux density.


