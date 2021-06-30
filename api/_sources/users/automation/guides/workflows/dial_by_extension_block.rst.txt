Workflows: Adding a Dial by Extension Block
===========================================

| The **Dial by Extension** block is only available when designing a workflow for a `voice campaign </users/campaigns/guides/voice/voice_campaigns.html>`_ or when managing a workflow for a `phone number </users/phone/guides/numbers/phone_numbers.html>`_
| This block allows you to play a message that informs callers/recipients of the available extensions. You will also use this block to create these extensions.
| This allows callers/recipients to navigate themselves to the extension that will best fulfill their needs.

#. Place a **Dial by Extension** block in your workflow where desired
#. Click `Speak text </users/automation/guides/workflows/speak_text_block.html>`_

   * Add the extension numbers and associated extensions to the greeting "You may dial your party's extension at any time" or write your own
#. Alternatively, click `Play an audio file </users/automation/guides/workflows/play_recording_block.html>`_
#. Click **Add Extension**
#. Enter a 3 digit extension
#. Enter a name
#. Create an announcement that will play before dialing out to recipient(s)

   * Use the following announcement "Connecting you to..." or write your own
   * Again, you can click `Speak text </users/automation/guides/workflows/speak_text_block.html>`_ or `Play an audio file </users/automation/guides/workflows/play_recording_block.html>`_
   * You can also click **No announcement** to play no message before routing to the extension
#. Click **Add Recipient**
#. Click **Dial a user**
#. Click **Choose a User** and select a user
#. Alternatively, click **Dial a phone number**
#. Enter a phone number
#. Click **Add** to add the recipient
#. If desired, click **Add Recipient** again

   * All added recipients will be called when an incoming call is routed to their extension - the call will be forwarded to the first recipient to answer
#. Click **Add** to add the extension
#. Click **Respond to hash (#)** or **Respond to star (*)** if you would like recipients to be able to press the hash and star

   * Use these characters if you anticipate callers/recipients needing further instructions/guidance (for example "press # to hear staff directory" when dialing by name)
#. Click **Done**
#. In the workflow, you can now click :icon:`ellipsis-h` and create pathways for when a caller/recipient presses #, ``*``, or nothing, or if the extension does not answer
