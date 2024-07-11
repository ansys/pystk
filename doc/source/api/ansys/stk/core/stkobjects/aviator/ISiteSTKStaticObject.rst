ISiteSTKStaticObject
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.ISiteSTKStaticObject

   object
   
   Interface used to access the options for a STK Static Object site.

.. py:currentmodule:: ISiteSTKStaticObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteSTKStaticObject.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteSTKStaticObject.object_name`
              - Gets or sets the object name to link to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ISiteSTKStaticObject.valid_object_names`
              - Returns the valid object names.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ISiteSTKStaticObject


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKStaticObject.object_name
    :type: str

    Gets or sets the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKStaticObject.valid_object_names
    :type: list

    Returns the valid object names.


Method detail
-------------




.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.ISiteSTKStaticObject.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

