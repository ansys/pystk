ISiteVTOLPoint
==============

.. py:class:: ISiteVTOLPoint

   object
   
   Interface used to access the options for a VTOL Point site.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~latitude`
            * - :py:meth:`~longitude`
            * - :py:meth:`~altitude`
            * - :py:meth:`~altitude_reference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteVTOLPoint


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteVTOLPoint.latitude
    :type: typing.Any

    Gets or sets the VTOL Point latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteVTOLPoint.longitude
    :type: typing.Any

    Gets or sets the VTOL Point longitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteVTOLPoint.altitude
    :type: float

    Gets or sets the altitude for the site.

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteVTOLPoint.altitude_reference
    :type: "AGL_MSL"

    Gets or sets the altitude reference.


Method detail
-------------









.. py:method:: get_as_site(self) -> "ISite"

    Get the site interface.

    :Returns:

        :obj:`~"ISite"`

