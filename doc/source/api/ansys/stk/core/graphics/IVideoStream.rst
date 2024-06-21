IVideoStream
============

.. py:class:: ansys.stk.core.graphics.IVideoStream

   object
   
   A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

.. py:currentmodule:: IVideoStream

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.reinitialize_with_string_uri`
              - Reinitializes the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.play`
              - Begins playing the video when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.pause`
              - Pauses the video when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.stop`
              - Stop the video when the playback property is set to real time. Stopping the video will seek to the first frame and pause playback. Use the Play method to begin playing the video again.
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.reset`
              - Seeks the video to its first frame and begins playing the video when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.close`
              - Close the video stream and any associated resources.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.uri`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.playback`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.frame_rate`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.interval_start_time`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.interval_end_time`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.start_time`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.end_time`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.start_frame`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.end_frame`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.loop`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.is_playing`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.packet_acquirement_yield_time`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.packet_buffer_limit`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.allow_frame_drop`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.enable_audio`
            * - :py:attr:`~ansys.stk.core.graphics.IVideoStream.audio_uri`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IVideoStream


Property detail
---------------

.. py:property:: uri
    :canonical: ansys.stk.core.graphics.IVideoStream.uri
    :type: str

    Gets the uri of the video.

.. py:property:: playback
    :canonical: ansys.stk.core.graphics.IVideoStream.playback
    :type: VIDEO_PLAYBACK

    Gets or sets the video playback mode of the video.

.. py:property:: frame_rate
    :canonical: ansys.stk.core.graphics.IVideoStream.frame_rate
    :type: float

    Gets or sets the frame rate of the video when the playback property is set to real time. If this property is not set, the internal framerate of the video is used.

.. py:property:: interval_start_time
    :canonical: ansys.stk.core.graphics.IVideoStream.interval_start_time
    :type: IDate

    Gets or sets the scene manager time at which the video will begin playing when the playback property is set to time interval.

.. py:property:: interval_end_time
    :canonical: ansys.stk.core.graphics.IVideoStream.interval_end_time
    :type: IDate

    Gets or sets the scene manager time at which the video will stop playing when the playback property is set to time interval.

.. py:property:: start_time
    :canonical: ansys.stk.core.graphics.IVideoStream.start_time
    :type: float

    Gets or sets the start time of the video in seconds. Changing the start time property also changes the start frame property to the frame in the video that corresponds to the specified time.

.. py:property:: end_time
    :canonical: ansys.stk.core.graphics.IVideoStream.end_time
    :type: float

    Gets or sets the end time of the video in seconds. Changing the end time property also changes the end frame property to the frame in the video that corresponds to the specified time.

.. py:property:: start_frame
    :canonical: ansys.stk.core.graphics.IVideoStream.start_frame
    :type: int

    Gets or sets the start frame of the video. Changing the start frame property also changes the start time property to the time in the video that corresponds to the specified frame.

.. py:property:: end_frame
    :canonical: ansys.stk.core.graphics.IVideoStream.end_frame
    :type: int

    Gets or sets the end frame of the video. Changing the end frame property also changes the end time property to the time in the video that corresponds to the specified frame.

.. py:property:: loop
    :canonical: ansys.stk.core.graphics.IVideoStream.loop
    :type: bool

    Gets or sets whether the video will loop when it reaches its last frame when the playback property is set to real time.

.. py:property:: is_playing
    :canonical: ansys.stk.core.graphics.IVideoStream.is_playing
    :type: bool

    Gets whether or not the video is playing. Use the play, pause, stop, and Reset methods to control the playback of the video when the playback property is set to real time.

.. py:property:: packet_acquirement_yield_time
    :canonical: ansys.stk.core.graphics.IVideoStream.packet_acquirement_yield_time
    :type: int

    Gets or sets the thread processing yield time for asynchronous streaming of video over common protocols like udp. Setting a high value may increase performance, but may cause frames or packets to drop, effecting visual quality...

.. py:property:: packet_buffer_limit
    :canonical: ansys.stk.core.graphics.IVideoStream.packet_buffer_limit
    :type: int

    Gets or sets a value indicating the buffering limit for packets when processing a video stream...

.. py:property:: allow_frame_drop
    :canonical: ansys.stk.core.graphics.IVideoStream.allow_frame_drop
    :type: bool

    Gets or sets a value indicating if frames should be dropped if video processing can not keep up with a video stream. If this is set to false, the video quality may degrade when the processing load is too high...

.. py:property:: enable_audio
    :canonical: ansys.stk.core.graphics.IVideoStream.enable_audio
    :type: bool

    Gets or sets a value indicating if the encoded audio stream should be synchronized to video playback If this is set to false, the audio stream will be disabled...

.. py:property:: audio_uri
    :canonical: ansys.stk.core.graphics.IVideoStream.audio_uri
    :type: str

    Gets the uri of the audio.


Method detail
-------------





























.. py:method:: reinitialize_with_string_uri(self, uri: str) -> None
    :canonical: ansys.stk.core.graphics.IVideoStream.reinitialize_with_string_uri

    Reinitializes the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: play(self) -> None
    :canonical: ansys.stk.core.graphics.IVideoStream.play

    Begins playing the video when the playback property is set to real time.

    :Returns:

        :obj:`~None`

.. py:method:: pause(self) -> None
    :canonical: ansys.stk.core.graphics.IVideoStream.pause

    Pauses the video when the playback property is set to real time.

    :Returns:

        :obj:`~None`

.. py:method:: stop(self) -> None
    :canonical: ansys.stk.core.graphics.IVideoStream.stop

    Stop the video when the playback property is set to real time. Stopping the video will seek to the first frame and pause playback. Use the Play method to begin playing the video again.

    :Returns:

        :obj:`~None`

.. py:method:: reset(self) -> None
    :canonical: ansys.stk.core.graphics.IVideoStream.reset

    Seeks the video to its first frame and begins playing the video when the playback property is set to real time.

    :Returns:

        :obj:`~None`

.. py:method:: close(self) -> None
    :canonical: ansys.stk.core.graphics.IVideoStream.close

    Close the video stream and any associated resources.

    :Returns:

        :obj:`~None`


