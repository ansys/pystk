PlanetCommonTasks
=================

.. py:class:: ansys.stk.core.stkobjects.PlanetCommonTasks

   Class defining the Planet Common class.

.. py:currentmodule:: PlanetCommonTasks

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetCommonTasks.set_position_source_file`
              - Specify a planet ephemeris file, with a .pe extension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetCommonTasks.set_position_source_central_body`
              - Specify the planet using a central body and a desired ephemeris source.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PlanetCommonTasks



Method detail
-------------

.. py:method:: set_position_source_file(self, file: str) -> PlanetPositionFile
    :canonical: ansys.stk.core.stkobjects.PlanetCommonTasks.set_position_source_file

    Specify a planet ephemeris file, with a .pe extension.

    :Parameters:

    **file** : :obj:`~str`

    :Returns:

        :obj:`~PlanetPositionFile`

.. py:method:: set_position_source_central_body(self, central_body: str, ephem_source: EphemSourceType) -> PlanetPositionCentralBody
    :canonical: ansys.stk.core.stkobjects.PlanetCommonTasks.set_position_source_central_body

    Specify the planet using a central body and a desired ephemeris source.

    :Parameters:

    **central_body** : :obj:`~str`
    **ephem_source** : :obj:`~EphemSourceType`

    :Returns:

        :obj:`~PlanetPositionCentralBody`

