PropagatorSGP4LoadFile
======================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSGP4LoadFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagatorSGP4LoadData`

   SGP4 propagator. Allows the user to load segments from file.

.. py:currentmodule:: PropagatorSGP4LoadFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.add_segments_from_file`
              - Add multiple segments from the array returned in GetSegsFromFile.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.get_ssc_numbers_from_file`
              - Return an array of SSC Numbers from the file selected.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.get_segments_from_file`
              - Return an array of available segments from a file using the specified SSC Number.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.file`
              - File name.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSGP4LoadFile


Property detail
---------------

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.file
    :type: str

    File name.


Method detail
-------------

.. py:method:: add_segments_from_file(self, segments: list) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.add_segments_from_file

    Add multiple segments from the array returned in GetSegsFromFile.

    :Parameters:

        **segments** : :obj:`~list`


    :Returns:

        :obj:`~None`



.. py:method:: get_ssc_numbers_from_file(self) -> list
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.get_ssc_numbers_from_file

    Return an array of SSC Numbers from the file selected.

    :Returns:

        :obj:`~list`

.. py:method:: get_segments_from_file(self, ssc_num: str) -> list
    :canonical: ansys.stk.core.stkobjects.PropagatorSGP4LoadFile.get_segments_from_file

    Return an array of available segments from a file using the specified SSC Number.

    :Parameters:

        **ssc_num** : :obj:`~str`


    :Returns:

        :obj:`~list`

