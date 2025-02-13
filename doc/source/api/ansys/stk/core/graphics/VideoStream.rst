VideoStream
===========

.. py:class:: ansys.stk.core.graphics.VideoStream

   Bases: :py:class:`~ansys.stk.core.graphics.IRasterStream`, :py:class:`~ansys.stk.core.graphics.IRaster`

   A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

.. py:currentmodule:: VideoStream

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.reinitialize_with_string_uri`
              - Reinitializes the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.play`
              - Begins playing the video when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.pause`
              - Pauses the video when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.stop`
              - Stop the video when the playback property is set to real time. Stopping the video will seek to the first frame and pause playback. Use the Play method to begin playing the video again.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.reset`
              - Seeks the video to its first frame and begins playing the video when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.close`
              - Close the video stream and any associated resources.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.uri`
              - Get the uri of the video.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.playback`
              - Get or set the video playback mode of the video.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.frame_rate`
              - Get or set the frame rate of the video when the playback property is set to real time. If this property is not set, the internal framerate of the video is used.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.interval_start_time`
              - Get or set the scene manager time at which the video will begin playing when the playback property is set to time interval.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.interval_end_time`
              - Get or set the scene manager time at which the video will stop playing when the playback property is set to time interval.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.start_time`
              - Get or set the start time of the video in seconds. Changing the start time property also changes the start frame property to the frame in the video that corresponds to the specified time.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.end_time`
              - Get or set the end time of the video in seconds. Changing the end time property also changes the end frame property to the frame in the video that corresponds to the specified time.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.start_frame`
              - Get or set the start frame of the video. Changing the start frame property also changes the start time property to the time in the video that corresponds to the specified frame.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.end_frame`
              - Get or set the end frame of the video. Changing the end frame property also changes the end time property to the time in the video that corresponds to the specified frame.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.loop`
              - Get or set whether the video will loop when it reaches its last frame when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.is_playing`
              - Get whether or not the video is playing. Use the play, pause, stop, and Reset methods to control the playback of the video when the playback property is set to real time.
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.packet_acquirement_yield_time`
              - Get or set the thread processing yield time for asynchronous streaming of video over common protocols like udp. Setting a high value may increase performance, but may cause frames or packets to drop, effecting visual quality...
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.packet_buffer_limit`
              - Get or set a value indicating the buffering limit for packets when processing a video stream...
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.allow_frame_drop`
              - Get or set a value indicating if frames should be dropped if video processing can not keep up with a video stream. If this is set to false, the video quality may degrade when the processing load is too high...
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.enable_audio`
              - Get or set a value indicating if the encoded audio stream should be synchronized to video playback If this is set to false, the audio stream will be disabled...
            * - :py:attr:`~ansys.stk.core.graphics.VideoStream.audio_uri`
              - Get the uri of the audio.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import VideoStream


Property detail
---------------

.. py:property:: uri
    :canonical: ansys.stk.core.graphics.VideoStream.uri
    :type: str

    Get the uri of the video.

.. py:property:: playback
    :canonical: ansys.stk.core.graphics.VideoStream.playback
    :type: VideoPlayback

    Get or set the video playback mode of the video.

.. py:property:: frame_rate
    :canonical: ansys.stk.core.graphics.VideoStream.frame_rate
    :type: float

    Get or set the frame rate of the video when the playback property is set to real time. If this property is not set, the internal framerate of the video is used.

.. py:property:: interval_start_time
    :canonical: ansys.stk.core.graphics.VideoStream.interval_start_time
    :type: IDate

    Get or set the scene manager time at which the video will begin playing when the playback property is set to time interval.

.. py:property:: interval_end_time
    :canonical: ansys.stk.core.graphics.VideoStream.interval_end_time
    :type: IDate

    Get or set the scene manager time at which the video will stop playing when the playback property is set to time interval.

.. py:property:: start_time
    :canonical: ansys.stk.core.graphics.VideoStream.start_time
    :type: float

    Get or set the start time of the video in seconds. Changing the start time property also changes the start frame property to the frame in the video that corresponds to the specified time.

.. py:property:: end_time
    :canonical: ansys.stk.core.graphics.VideoStream.end_time
    :type: float

    Get or set the end time of the video in seconds. Changing the end time property also changes the end frame property to the frame in the video that corresponds to the specified time.

.. py:property:: start_frame
    :canonical: ansys.stk.core.graphics.VideoStream.start_frame
    :type: int

    Get or set the start frame of the video. Changing the start frame property also changes the start time property to the time in the video that corresponds to the specified frame.

.. py:property:: end_frame
    :canonical: ansys.stk.core.graphics.VideoStream.end_frame
    :type: int

    Get or set the end frame of the video. Changing the end frame property also changes the end time property to the time in the video that corresponds to the specified frame.

.. py:property:: loop
    :canonical: ansys.stk.core.graphics.VideoStream.loop
    :type: bool

    Get or set whether the video will loop when it reaches its last frame when the playback property is set to real time.

.. py:property:: is_playing
    :canonical: ansys.stk.core.graphics.VideoStream.is_playing
    :type: bool

    Get whether or not the video is playing. Use the play, pause, stop, and Reset methods to control the playback of the video when the playback property is set to real time.

.. py:property:: packet_acquirement_yield_time
    :canonical: ansys.stk.core.graphics.VideoStream.packet_acquirement_yield_time
    :type: int

    Get or set the thread processing yield time for asynchronous streaming of video over common protocols like udp. Setting a high value may increase performance, but may cause frames or packets to drop, effecting visual quality...

.. py:property:: packet_buffer_limit
    :canonical: ansys.stk.core.graphics.VideoStream.packet_buffer_limit
    :type: int

    Get or set a value indicating the buffering limit for packets when processing a video stream...

.. py:property:: allow_frame_drop
    :canonical: ansys.stk.core.graphics.VideoStream.allow_frame_drop
    :type: bool

    Get or set a value indicating if frames should be dropped if video processing can not keep up with a video stream. If this is set to false, the video quality may degrade when the processing load is too high...

.. py:property:: enable_audio
    :canonical: ansys.stk.core.graphics.VideoStream.enable_audio
    :type: bool

    Get or set a value indicating if the encoded audio stream should be synchronized to video playback If this is set to false, the audio stream will be disabled...

.. py:property:: audio_uri
    :canonical: ansys.stk.core.graphics.VideoStream.audio_uri
    :type: str

    Get the uri of the audio.


Method detail
-------------





























.. py:method:: reinitialize_with_string_uri(self, uri: str) -> None
    :canonical: ansys.stk.core.graphics.VideoStream.reinitialize_with_string_uri

    Reinitializes the video stream from a Uri, which can be a file, HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: play(self) -> None
    :canonical: ansys.stk.core.graphics.VideoStream.play

    Begins playing the video when the playback property is set to real time.

    :Returns:

        :obj:`~None`

.. py:method:: pause(self) -> None
    :canonical: ansys.stk.core.graphics.VideoStream.pause

    Pauses the video when the playback property is set to real time.

    :Returns:

        :obj:`~None`

.. py:method:: stop(self) -> None
    :canonical: ansys.stk.core.graphics.VideoStream.stop

    Stop the video when the playback property is set to real time. Stopping the video will seek to the first frame and pause playback. Use the Play method to begin playing the video again.

    :Returns:

        :obj:`~None`

.. py:method:: reset(self) -> None
    :canonical: ansys.stk.core.graphics.VideoStream.reset

    Seeks the video to its first frame and begins playing the video when the playback property is set to real time.

    :Returns:

        :obj:`~None`

.. py:method:: close(self) -> None
    :canonical: ansys.stk.core.graphics.VideoStream.close

    Close the video stream and any associated resources.

    :Returns:

        :obj:`~None`


