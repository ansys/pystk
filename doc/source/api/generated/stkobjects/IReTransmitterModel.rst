IReTransmitterModel
===================

.. py:class:: IReTransmitterModel

   object
   
   Provide access to the properties and methods defining a re-transmitter model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~frequency_transfer_function_polynomial`
            * - :py:meth:`~power_back_off_transfer_function_type`
            * - :py:meth:`~power_back_off_linear_scale`
            * - :py:meth:`~power_back_off_transfer_function_polynomial`
            * - :py:meth:`~power_back_off_transfer_function_table`
            * - :py:meth:`~enable_c_over_im`
            * - :py:meth:`~c_over_im_transfer_function_type`
            * - :py:meth:`~c_over_im_linear_scale`
            * - :py:meth:`~c_over_im_transfer_function_polynomial`
            * - :py:meth:`~c_over_im_transfer_function_table`
            * - :py:meth:`~saturated_flux_density`
            * - :py:meth:`~operational_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReTransmitterModel


Property detail
---------------

.. py:property:: frequency_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.frequency_transfer_function_polynomial
    :type: "IAgTransferFunctionPolynomialCollection"

    Gets the frequency transfer function polynomial collection.

.. py:property:: power_back_off_transfer_function_type
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_type
    :type: "TRANSFER_FUNCTION_TYPE"

    Gets or sets the power back off transfer function type.

.. py:property:: power_back_off_linear_scale
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_linear_scale
    :type: bool

    Gets or sets the option to enable power back off linear scale.

.. py:property:: power_back_off_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_polynomial
    :type: "IAgTransferFunctionPolynomialCollection"

    Gets the power back off transfer function polynomial collection.

.. py:property:: power_back_off_transfer_function_table
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.power_back_off_transfer_function_table
    :type: "IAgTransferFunctionInputBackOffOutputBackOffTable"

    Gets the power back off transfer function table.

.. py:property:: enable_c_over_im
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.enable_c_over_im
    :type: bool

    Gets or sets the option to enable C/Im.

.. py:property:: c_over_im_transfer_function_type
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_type
    :type: "TRANSFER_FUNCTION_TYPE"

    Gets or sets the C/Im transfer function type.

.. py:property:: c_over_im_linear_scale
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_linear_scale
    :type: bool

    Gets or sets the option to enable C/Im linear scale.

.. py:property:: c_over_im_transfer_function_polynomial
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_polynomial
    :type: "IAgTransferFunctionPolynomialCollection"

    Gets the C/Im transfer function polynomial collection.

.. py:property:: c_over_im_transfer_function_table
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.c_over_im_transfer_function_table
    :type: "IAgTransferFunctionInputBackOffCOverImTable"

    Gets the C/Im transfer function table.

.. py:property:: saturated_flux_density
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.saturated_flux_density
    :type: float

    Gets or sets the saturated flux density.

.. py:property:: operational_mode
    :canonical: ansys.stk.core.stkobjects.IReTransmitterModel.operational_mode
    :type: "RE_TRANSMITTER_OP_MODE"

    Gets or sets the operational mode.


