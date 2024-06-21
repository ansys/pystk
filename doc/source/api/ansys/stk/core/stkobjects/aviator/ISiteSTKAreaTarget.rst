ISiteSTKAreaTarget
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.ISiteSTKAreaTarget

   object
   
   Interface used to access the options for a STK Area Target site.

.. py:currentmodule:: ISiteSTKAreaTarget

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteSTKAreaTarget.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteSTKAreaTarget.object_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteSTKAreaTarget.valid_object_names`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteSTKAreaTarget


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKAreaTarget.object_name
    :type: str

    Gets or sets the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKAreaTarget.valid_object_names
    :type: list

    Returns the valid object names.


Method detail
-------------




.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKAreaTarget.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

