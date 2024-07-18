VehicleSGP4LoadFile
===================

.. py:class:: ansys.stk.core.stkobjects.VehicleSGP4LoadFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleSGP4LoadData`

   SGP4 propagator. Allows the user to load segments from file.

.. py:currentmodule:: VehicleSGP4LoadFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4LoadFile.get_ssc_nums_from_file`
              - Return an array of SSC Numbers from the file selected.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4LoadFile.get_segs_from_file`
              - Return an array of available segments from a file using the specified SSC Number.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4LoadFile.add_segs_from_file`
              - Add multiple segments from the array returned in GetSegsFromFile.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSGP4LoadFile.file`
              - File name.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSGP4LoadFile


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4LoadFile.file
    :type: str

    File name.


Method detail
-------------



.. py:method:: get_ssc_nums_from_file(self) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4LoadFile.get_ssc_nums_from_file

    Return an array of SSC Numbers from the file selected.

    :Returns:

        :obj:`~list`

.. py:method:: get_segs_from_file(self, SSCNum: str) -> list
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4LoadFile.get_segs_from_file

    Return an array of available segments from a file using the specified SSC Number.

    :Parameters:

    **SSCNum** : :obj:`~str`

    :Returns:

        :obj:`~list`

.. py:method:: add_segs_from_file(self, segments: list) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleSGP4LoadFile.add_segs_from_file

    Add multiple segments from the array returned in GetSegsFromFile.

    :Parameters:

    **segments** : :obj:`~list`

    :Returns:

        :obj:`~None`

