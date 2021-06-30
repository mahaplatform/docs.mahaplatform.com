Workflows: Adding a Dial by Menu Block
======================================

| The **Dial by Menu** block is only available when designing a workflow for a `voice campaign </users/campaigns/guides/voice/voice_campaigns.html>`_ or when managing a workflow for a `phone number </users/phone/guides/numbers/phone_numbers.html>`_
| This block allows you to play a message that informs callers/recipients of the available menu options. You will also use this block to create these menu options.
| This allows callers/recipients to navigate themselves to the menu options that will best fulfill their needs.

#. Place a **Dial by Menu** block in your workflow where desired
#. Enter a menu name
#. Click `Speak text </users/automation/guides/workflows/speak_text_block.html>`_

   * Add the menu option numbers and associated menu options to the greeting "Listen carefully to the following options" or write your own
#. Alternatively, click `Play an audio file </users/automation/guides/workflows/play_recording_block.html>`_
#. Click **Add Option**
#. Enter a number
#. Add a name
#. Click **Add**
#. To delete an option, click :icon:`times`
#. To `edit </users/general/guides/functions_of_the_grid/how_to_edit.html>`_ an option, click :icon:`pencil`
#. If desired, click **Add Option** again
#. Click **Respond to hash (#)** or **Respond to star (*)** if you would like recipients to be able to press the hash and star

   * Use these characters if you anticipate callers/recipients needing further instructions/guidance (for example "press # to hear staff directory" when dialing by name)
#. Click **Done**
#. In the workflow, you can now click :icon:`ellipsis-h` and create pathways for when a caller/recipient presses #, ``*``, or nothing, or if the extension does not answer
