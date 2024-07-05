IAttitudeControlImpulsiveFile
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile

   IAttitudeControlImpulsive
   
   Properties for the File attitude control for an Impulsive Maneuver.

.. py:currentmodule:: IAttitudeControlImpulsiveFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.delta_v_magnitude`
              - Gets or sets the size of the delta-V to be applied to the orbit along the specified direction. Uses Rate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.filename`
              - Gets or sets the attitude file to use.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.file_time_offset`
              - Gets or sets the time offset can be used to adjust the time stored in the attitude file. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.full_filename`
              - Get the full path and name of the attitude file to use.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlImpulsiveFile


Property detail
---------------

.. py:property:: delta_v_magnitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.delta_v_magnitude
    :type: float

    Gets or sets the size of the delta-V to be applied to the orbit along the specified direction. Uses Rate Dimension.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.filename
    :type: str

    Gets or sets the attitude file to use.

.. py:property:: file_time_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.file_time_offset
    :type: float

    Gets or sets the time offset can be used to adjust the time stored in the attitude file. Dimensionless.

.. py:property:: full_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlImpulsiveFile.full_filename
    :type: str

    Get the full path and name of the attitude file to use.


