StkRfcmGpuProperties
====================

.. py:class:: ansys.stk.core.rfcm.StkRfcmGpuProperties

   The properties of a GPU pertaining to RF Channel Modeler.

.. py:currentmodule:: StkRfcmGpuProperties

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmGpuProperties.name`
              - Gets the GPU name.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmGpuProperties.compute_capability`
              - Gets the GPU compute capability.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmGpuProperties.device_id`
              - Gets the GPU device ID.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmGpuProperties.processor_count`
              - Gets the GPU processor count.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmGpuProperties.speed_m_hz`
              - Gets the GPU speed in MHz.
            * - :py:attr:`~ansys.stk.core.rfcm.StkRfcmGpuProperties.memory_gb`
              - Gets the GPU memory in GB.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.rfcm import StkRfcmGpuProperties


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.rfcm.StkRfcmGpuProperties.name
    :type: str

    Gets the GPU name.

.. py:property:: compute_capability
    :canonical: ansys.stk.core.rfcm.StkRfcmGpuProperties.compute_capability
    :type: str

    Gets the GPU compute capability.

.. py:property:: device_id
    :canonical: ansys.stk.core.rfcm.StkRfcmGpuProperties.device_id
    :type: int

    Gets the GPU device ID.

.. py:property:: processor_count
    :canonical: ansys.stk.core.rfcm.StkRfcmGpuProperties.processor_count
    :type: int

    Gets the GPU processor count.

.. py:property:: speed_m_hz
    :canonical: ansys.stk.core.rfcm.StkRfcmGpuProperties.speed_m_hz
    :type: float

    Gets the GPU speed in MHz.

.. py:property:: memory_gb
    :canonical: ansys.stk.core.rfcm.StkRfcmGpuProperties.memory_gb
    :type: float

    Gets the GPU memory in GB.


