IScatteringPointProviderPointsFile
==================================

.. py:class:: ansys.stk.core.stkobjects.IScatteringPointProviderPointsFile

   object
   
   Provide access to the properties and methods defining a scattering point provider where the scattering points are defined in a ascii text file.

.. py:currentmodule:: IScatteringPointProviderPointsFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderPointsFile.filename`
              - Gets or sets the scattering points filename.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderPointsFile.default_scattering_point_model`
              - Gets the link/embed controller for managing the default scattering point model component.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderPointsFile.scattering_points`
              - Gets the collection of scattering points.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScatteringPointProviderPointsFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderPointsFile.filename
    :type: str

    Gets or sets the scattering points filename.

.. py:property:: default_scattering_point_model
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderPointsFile.default_scattering_point_model
    :type: IComponentLinkEmbedControl

    Gets the link/embed controller for managing the default scattering point model component.

.. py:property:: scattering_points
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderPointsFile.scattering_points
    :type: IScatteringPointCollection

    Gets the collection of scattering points.


