IAntennaModelANSYSffdFormat
===========================

.. py:class:: IAntennaModelANSYSffdFormat

   object
   
   Provide access to the properties and methods defining an antnna pattern ANSYS ffd format model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~filename`
            * - :py:meth:`~defined_frequencies`
            * - :py:meth:`~gain_type`
            * - :py:meth:`~defined_power_value`
            * - :py:meth:`~user_gain_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelANSYSffdFormat


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IAntennaModelANSYSffdFormat.filename
    :type: str

    Gets or sets the user antenna data filename.

.. py:property:: defined_frequencies
    :canonical: ansys.stk.core.stkobjects.IAntennaModelANSYSffdFormat.defined_frequencies
    :type: str

    Gets the frequencies defined in the file.

.. py:property:: gain_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelANSYSffdFormat.gain_type
    :type: "HFSS_FFD_GAIN_TYPE"

    Gets or sets the gain type.

.. py:property:: defined_power_value
    :canonical: ansys.stk.core.stkobjects.IAntennaModelANSYSffdFormat.defined_power_value
    :type: float

    Gets the Defined Power Value for the selected GainType.

.. py:property:: user_gain_factor
    :canonical: ansys.stk.core.stkobjects.IAntennaModelANSYSffdFormat.user_gain_factor
    :type: float

    Gets or sets the User Gain Factor.


