SiteRelativeToPrevProcedure
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a Relative to Previous Procedure site.

.. py:currentmodule:: SiteRelativeToPrevProcedure

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing_mode`
              - Gets or sets the bearing reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing`
              - Gets or sets the bearing to define the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.range`
              - Gets or sets the range from the previous procedure.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteRelativeToPrevProcedure


Property detail
---------------

.. py:property:: bearing_mode
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing_mode
    :type: RelativeAbsoluteBearing

    Gets or sets the bearing reference.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.bearing
    :type: typing.Any

    Gets or sets the bearing to define the site.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.range
    :type: float

    Gets or sets the range from the previous procedure.


Method detail
-------------







.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToPrevProcedure.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

