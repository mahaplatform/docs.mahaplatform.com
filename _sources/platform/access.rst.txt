Access Control
==============
The Maha Platform uses role based access control to determine what a user
can do within a given team. This means that access is
configured at the role and a users access is determined by the roles they
have been assigned

.. image:: ../_static/images/platform-access.jpg
   :width: 700

Roles
-----
Roles are objects which have been assigned a specific set of apps and rights
and can be assigned to a specific set of users. For example, you may create a
role called 'Finance' that has access to the the finance app and is assigned the
rights to view both expense and revenue reports.

Apps
----
Each role can be assigned access to one or more apps. For example, you may
create a role called 'Marketing' which has access to the CRM, Websites, and
Campaigns apps.

Rights
------
Each app has a set of individual rights that define specific actions a user
perform within them. Rights are specific

Users
-----
Each user can be assigned to one or more roles. A user's access is determined by
the union of the apps and rights of all assigned roles.
