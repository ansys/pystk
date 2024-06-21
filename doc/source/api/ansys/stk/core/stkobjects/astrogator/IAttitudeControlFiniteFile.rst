IAttitudeControlFiniteFile
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile

   IAttitudeControlFinite
   
   Properties for the File attitude control for a Finite Maneuver.

.. py:currentmodule:: IAttitudeControlFiniteFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile.filename`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile.file_time_offset`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile.full_filename`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAttitudeControlFiniteFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile.filename
    :type: str

    Gets or sets the attitude file to use.

.. py:property:: file_time_offset
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile.file_time_offset
    :type: float

    Gets or sets the time offset can be used to adjust the time stored in the attitude file. Dimensionless.

.. py:property:: full_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IAttitudeControlFiniteFile.full_filename
    :type: str

    Get the full path and name of the attitude file to use.


