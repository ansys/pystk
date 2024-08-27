AttitudeControlFiniteFile
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFinite`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The file attitude control for a finite maneuver.

.. py:currentmodule:: AttitudeControlFiniteFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile.filename`
              - Gets or sets the attitude file to use.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile.file_time_offset`
              - Gets or sets the time offset can be used to adjust the time stored in the attitude file. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile.full_filename`
              - Get the full path and name of the attitude file to use.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import AttitudeControlFiniteFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile.filename
    :type: str

    Gets or sets the attitude file to use.

.. py:property:: file_time_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile.file_time_offset
    :type: float

    Gets or sets the time offset can be used to adjust the time stored in the attitude file. Dimensionless.

.. py:property:: full_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.AttitudeControlFiniteFile.full_filename
    :type: str

    Get the full path and name of the attitude file to use.


