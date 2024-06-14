ISTKXApplicationPartnerAccess
=============================

.. py:class:: ISTKXApplicationPartnerAccess

   object
   
   Access to the application object model for business partners.

.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~grant_partner_access`
              - Provide object model root for authorized business partners.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import ISTKXApplicationPartnerAccess



Method detail
-------------

.. py:method:: grant_partner_access(self, vendor:str, product:str, key:str) -> "ISTKXApplication"

    Provide object model root for authorized business partners.

    :Parameters:

    **vendor** : :obj:`~str`
    **product** : :obj:`~str`
    **key** : :obj:`~str`

    :Returns:

        :obj:`~"ISTKXApplication"`

