IUiApplicationPartnerAccess
===========================

.. py:class:: ansys.stk.core.uiapplication.IUiApplicationPartnerAccess

   Access to the application object model for business partners.

.. py:currentmodule:: IUiApplicationPartnerAccess

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.IUiApplicationPartnerAccess.grant_partner_access`
              - Provide object model root for authorized business partners.

Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import IUiApplicationPartnerAccess



Method detail
-------------

.. py:method:: grant_partner_access(self, vendor: str, product: str, key: str) -> typing.Any
    :canonical: ansys.stk.core.uiapplication.IUiApplicationPartnerAccess.grant_partner_access

    Provide object model root for authorized business partners.

    :Parameters:

        **vendor** : :obj:`~str`

        **product** : :obj:`~str`

        **key** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

