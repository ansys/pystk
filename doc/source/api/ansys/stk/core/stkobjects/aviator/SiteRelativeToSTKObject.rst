SiteRelativeToSTKObject
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a Relative to Stationary STK Object site.

.. py:currentmodule:: SiteRelativeToSTKObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.object_name`
              - Get or set the object name to link to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.valid_object_names`
              - Return the valid object names.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.bearing`
              - Get or set the bearing from the STK object.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.use_magnetic_bearing`
              - Get or set the option to use a magnetic bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.range`
              - Get or set the range from the STK object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteRelativeToSTKObject


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.object_name
    :type: str

    Get or set the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.valid_object_names
    :type: list

    Return the valid object names.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.bearing
    :type: typing.Any

    Get or set the bearing from the STK object.

.. py:property:: use_magnetic_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.use_magnetic_bearing
    :type: bool

    Get or set the option to use a magnetic bearing.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.range
    :type: float

    Get or set the range from the STK object.


Method detail
-------------










.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteRelativeToSTKObject.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

