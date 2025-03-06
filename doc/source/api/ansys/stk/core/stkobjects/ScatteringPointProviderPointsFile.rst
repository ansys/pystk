ScatteringPointProviderPointsFile
=================================

.. py:class:: ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.IScatteringPointProvider`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a scattring point provider where the points are defined in an ascii text file.

.. py:currentmodule:: ScatteringPointProviderPointsFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile.filename`
              - Get or set the scattering points filename.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile.default_scattering_point_model`
              - Get the link/embed controller for managing the default scattering point model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile.scattering_points`
              - Get the collection of scattering points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScatteringPointProviderPointsFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile.filename
    :type: str

    Get or set the scattering points filename.

.. py:property:: default_scattering_point_model
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile.default_scattering_point_model
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the default scattering point model component.

.. py:property:: scattering_points
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderPointsFile.scattering_points
    :type: ScatteringPointCollection

    Get the collection of scattering points.


