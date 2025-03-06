AttitudeControlImpulsiveFile
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsive`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The file attitude control for an impulsive maneuver.

.. py:currentmodule:: AttitudeControlImpulsiveFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.delta_v_magnitude`
              - Get or set the size of the delta-V to be applied to the orbit along the specified direction. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.filename`
              - Get or set the attitude file to use.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.file_time_offset`
              - Get or set the time offset can be used to adjust the time stored in the attitude file. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.full_filename`
              - Get the full path and name of the attitude file to use.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlImpulsiveFile


Property detail
---------------

.. py:property:: delta_v_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.delta_v_magnitude
    :type: float

    Get or set the size of the delta-V to be applied to the orbit along the specified direction. Uses Rate Dimension.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.filename
    :type: str

    Get or set the attitude file to use.

.. py:property:: file_time_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.file_time_offset
    :type: float

    Get or set the time offset can be used to adjust the time stored in the attitude file. Dimensionless.

.. py:property:: full_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.full_filename
    :type: str

    Get the full path and name of the attitude file to use.


