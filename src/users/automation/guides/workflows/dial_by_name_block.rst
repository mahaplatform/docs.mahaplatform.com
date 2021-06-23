Workflows: Adding a Dial by Name Block
======================================

| The **Dial by Name** block is only available when designing a workflow for a `voice campaign </users/campaigns/guides/voice/voice_campaigns.html>`_ or when managing a workflow for a `phone number </users/phone/guides/numbers/phone_numbers.html>`_
| This block allows you to play a message that informs callers/recipients of the available recipients.
| This allows callers/recipients to navigate themselves to the recipient that will best fulfill their needs by dialing the first three letters of their party's (the recipient) last name.

#. Place a **Dial by Name** block in your workflow where desired
#. Click `Speak text </users/automation/guides/workflows/speak_text_block.html>`_

   * Keep the greeting "Dial the first three letters of your party's last name" or write your own
#. Alternatively, click `Play an audio file </users/automation/guides/workflows/play_recording_block.html>`_
#. Click **Add Recipient**
#. Again, you can click `Speak text </users/automation/guides/workflows/speak_text_block.html>`_ or `Play an audio file </users/automation/guides/workflows/play_recording_block.html>`_

   * You can also click **No announcement** to play no message before routing to the recipient
#. Click **Choose a User** and select a user
#. Click **Add** to add the recipient
#. If desired, click **Add Recipient** again

   * All added recipients will be called when an incoming call is routed to their extension - the call will be forwarded to the first recipient to answer
#. Click **Respond to hash (#)** or **Respond to star (*)** if you would like recipients to be able to press the hash and star

   * Use these characters if you anticipate callers/recipients needing further instructions/guidance (for example "press # to hear staff directory" when dialing by name)
#. Click **Done**
#. In the workflow, you can now click :icon:`ellipsis-h` and create pathways for when a caller/recipient presses #, *, or nothing, or if the extension does not answer
