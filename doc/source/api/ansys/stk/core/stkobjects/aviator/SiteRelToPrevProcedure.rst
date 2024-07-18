SiteRelToPrevProcedure
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a Relative to Previous Procedure site.

.. py:currentmodule:: SiteRelToPrevProcedure

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.bearing_mode`
              - Gets or sets the bearing reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.bearing`
              - Gets or sets the bearing to define the site.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.range`
              - Gets or sets the range from the previous procedure.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteRelToPrevProcedure


Property detail
---------------

.. py:property:: bearing_mode
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.bearing_mode
    :type: REL_ABS_BEARING

    Gets or sets the bearing reference.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.bearing
    :type: typing.Any

    Gets or sets the bearing to define the site.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.range
    :type: float

    Gets or sets the range from the previous procedure.


Method detail
-------------







.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelToPrevProcedure.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

