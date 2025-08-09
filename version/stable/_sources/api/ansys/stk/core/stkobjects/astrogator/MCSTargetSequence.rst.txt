MCSTargetSequence
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   The Target Sequence segment.

.. py:currentmodule:: MCSTargetSequence

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.apply_profiles`
              - Apply Changes - applies the current values of search profiles' controls and the changes specified by the segment configuration profiles to the segments within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_profiles`
              - Reset - resets the controls of the search profiles to the segments' values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.apply_profile`
              - Apply Changes - applies the current values of specified profile to the segments within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_profile`
              - Reset - resets the current values of specified profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.apply_profile_by_name`
              - Apply Changes - applies the current values of specified profile to the segments within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_profile_by_name`
              - Reset - resets the current values of specified profile.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.action`
              - Whether to run the sequence nominally or using profiles.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.when_profiles_finish`
              - When Profiles Converge - the action to be carried out if targeting has converged.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.continue_on_failure`
              - Continue if profiles don't converge - if true, the target sequence continues if a profile fails to converge; otherwise, the MCS will stop upon the failure of a search profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.segments`
              - Return the segments contained within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.profiles`
              - Return the profiles used within the target sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_inner_targeters`
              - If true, inner target sequences will have their profiles reset before each run.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import MCSTargetSequence


Property detail
---------------

.. py:property:: action
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.action
    :type: TargetSequenceAction

    Whether to run the sequence nominally or using profiles.

.. py:property:: when_profiles_finish
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.when_profiles_finish
    :type: ProfilesFinish

    When Profiles Converge - the action to be carried out if targeting has converged.

.. py:property:: continue_on_failure
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.continue_on_failure
    :type: bool

    Continue if profiles don't converge - if true, the target sequence continues if a profile fails to converge; otherwise, the MCS will stop upon the failure of a search profile.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.segments
    :type: MCSSegmentCollection

    Return the segments contained within the target sequence.

.. py:property:: profiles
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.profiles
    :type: ProfileCollection

    Return the profiles used within the target sequence.

.. py:property:: reset_inner_targeters
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_inner_targeters
    :type: bool

    If true, inner target sequences will have their profiles reset before each run.


Method detail
-------------









.. py:method:: apply_profiles(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.apply_profiles

    Apply Changes - applies the current values of search profiles' controls and the changes specified by the segment configuration profiles to the segments within the target sequence.

    :Returns:

        :obj:`~None`

.. py:method:: reset_profiles(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_profiles

    Reset - resets the controls of the search profiles to the segments' values.

    :Returns:

        :obj:`~None`

.. py:method:: apply_profile(self, profile: IProfile) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.apply_profile

    Apply Changes - applies the current values of specified profile to the segments within the target sequence.

    :Parameters:

        **profile** : :obj:`~IProfile`


    :Returns:

        :obj:`~None`

.. py:method:: reset_profile(self, profile: IProfile) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_profile

    Reset - resets the current values of specified profile.

    :Parameters:

        **profile** : :obj:`~IProfile`


    :Returns:

        :obj:`~None`

.. py:method:: apply_profile_by_name(self, profile: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.apply_profile_by_name

    Apply Changes - applies the current values of specified profile to the segments within the target sequence.

    :Parameters:

        **profile** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: reset_profile_by_name(self, profile: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.MCSTargetSequence.reset_profile_by_name

    Reset - resets the current values of specified profile.

    :Parameters:

        **profile** : :obj:`~str`


    :Returns:

        :obj:`~None`



