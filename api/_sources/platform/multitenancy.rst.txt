Multitenant Architecture
========================
In order to minimize overhead and maximize scalability, the Maha Platform
employs a multitenant architecture. In this architecture, all organizations
share the same hardware, database, and network.

Teams
-----
Each organization that uses the Maha Platform is referred to as a team. Each
team has its own users, its own set of installefd apps, and its own data.
Although all team data is effectively stored in the same database using the same
hardware, all team data is partitioned by ``team_id``.
