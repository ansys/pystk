SiteSTKAreaTarget
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ISite`

   Class defining a STK Area Target site.

.. py:currentmodule:: SiteSTKAreaTarget

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget.get_as_site`
              - Get the site interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget.object_name`
              - Get or set the object name to link to.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget.valid_object_names`
              - Return the valid object names.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import SiteSTKAreaTarget


Property detail
---------------

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget.object_name
    :type: str

    Get or set the object name to link to.

.. py:property:: valid_object_names
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget.valid_object_names
    :type: list

    Return the valid object names.


Method detail
-------------




.. py:method:: get_as_site(self) -> ISite
    :canonical: ansys.stk.core.stkobjects.aviator.SiteSTKAreaTarget.get_as_site

    Get the site interface.

    :Returns:

        :obj:`~ISite`

