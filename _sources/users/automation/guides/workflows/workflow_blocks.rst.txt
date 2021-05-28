Blocks for Designing a Workflow
===============================

| A workflow can be as simple or as complex as you would like. There are many structures you can use to customize the pathway a contact will take.
| Below, these structures, called **Blocks**, are defined.
| To use these blocks, you will need to have navigated to the workflow design tab. Click `here </users/automation/guides/emails/design_email.html>`_ if you are having trouble reaching this point.

#. **If/Then**: Allows for contacts enrolled in a workflow to follow separate pathways with different blocks. Contacts who satisfy your criteria follow one path and contacts who do not ("else") follow the other designated path

   * Click **Add Branch**
   * Enter name for the branch
   * Click **Add Criteria**
   * Add criteria. If desired, you can use the AND/OR conditionals (refer to the `and </users/general/guides/functions_of_the_grid/filter_and.html>`_ and `or </users/general/guides/functions_of_the_grid/filter_or.html>`_ conditionals for filtering records to learn more about this option)
   * Click **Save**
   * Click **Done**
#. **Wait**: Allows an event to be triggered on a schedule

   * Option one: Select to wait **Until a specific date and time** and enter a date and time
   * Option two: Select to wait **For a specific duration of time** and enter the duration in days, hours, and/or minutes
   * Click **Done**
#. **Set Goal**: Place this block to mark a point in the workflow where contacts who reach the goal will be recorded and displayed in the performance tab - as a contact that has been "converted"
#. **Set Variable**: A contact who reaches a set variable will retain this variable as they move through the workflow. This memory allows for more complex if/then blocks to be implemented later on in the workflow

   * Enter a name
   * Enter a value
   * Click **Done**
#. **Update Property**: Add (or change) a property of a contact

   * Click **Choose a property**
   * Select a property
   * Enter a value
   * If you would like contacts who already have a property value to take on this property value instead, check the box entitled **Overwrite value if property is already set**
   * Click **Done**
#. **Update Consent**: ???
#. **Update Lists**: Allows for contacts to be added or removed from a list

   * Select **Add to List** or **Remove from List**
   * Select a list
   * Click **Done**
#. **Update Topics**: Allows for contacts to be added or removed from a topic

   * Select **Add to List** or **Remove from List** ??lists??
   * Select a topic
   * Click **Done**
#. **Enroll in Workflow**: Allows contacts to be enrolled in another workflow

   * Click **Choose a workflow**
   * Select an existing workflow from the list or click **Add New** ?
   * Click **Done**
#. **Send Email**: Triggers an email to the contact's email address

   * Click **Choose an email**
   * Select an existing email from the list or click **Add New** ?
   * Click **Done**
#. **Send Internal Email**: When the contact reaches this point of the workflow, an email can be sent to notify a user in administration

   * Choose a recipient - a specific user or an email address
   * Create an email by filling out an email subject and body
   * Click **Done**
#. **Send Internal SMS**: When the contact reaches this point of the workflow, a text message can be sent to notify a user in administration

   * Choose a recipient - a specific user or a phone number
   * Create a text message by entering a message
   * If desired, `Add Attachment </users/general/guides/functions_of_the_grid/how_to_upload_a_file.html>`_
   * Click **Done**
