IProfile
========

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfile

   General properties for target sequence profiles.

.. py:currentmodule:: IProfile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfile.copy`
              - Make a copy of the profile.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfile.name`
              - Gets or sets the name of the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfile.status`
              - Gets or sets the status of the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfile.user_comment`
              - A user comment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfile.mode`
              - Gets or sets the profile's mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfile.type`
              - Return the current profile type.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfile


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfile.name
    :type: str

    Gets or sets the name of the profile.

.. py:property:: status
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfile.status
    :type: str

    Gets or sets the status of the profile.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfile.user_comment
    :type: str

    A user comment.

.. py:property:: mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfile.mode
    :type: ProfileMode

    Gets or sets the profile's mode.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfile.type
    :type: Profile

    Return the current profile type.


Method detail
-------------

.. py:method:: copy(self) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfile.copy

    Make a copy of the profile.

    :Returns:

        :obj:`~IProfile`









